"""
Database info:
- localhost
- user			: ilumone
- password		: ilumone
- database name	: environ	
"""

import psycopg2

class DbConnector(object):
	def __init__(self, database, user, password, host='localhost', port='5432'):
		try: 
			self.db 	= psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
			self.cursor = self.db.cursor()
		except Exception as e:
			e.printStackTrace()
			raise Exception()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self.cursor.close()
		self.db.close()
		return

	def __checkExists(self, table_name):
		self.cursor.execute(
			"""
				SELECT EXISTS (SELECT relname FROM pg_class WHERE relname='{0}');
			""".format(table_name)
			)
		return bool(self.cursor.fetchone()[0])

	def __buildTableCountries(self):
		if(not self.__checkExists("countries")):
			print("Constructing countries table")
			self.cursor.execute(
				"""
					CREATE TABLE countries
					(
						code 	varchar(5) 		NOT NULL,
						name 	varchar(100) 	NOT NULL,
						region 	varchar(50) 	NOT NULL,
						inc_grp varchar(50),
						notes 	varchar(40000),

						PRIMARY KEY(code)
					);
				"""
				)
		return

	def __buildTableIndicators(self):
		if(not self.__checkExists("indicators")):
			print("Constructing indicators table")
			self.cursor.execute(
				"""
					CREATE TABLE indicators
					(
						code 	varchar(20)		NOT NULL,
						name 	varchar(1000) 	NOT NULL,
						notes 	varchar(40000),

						PRIMARY KEY(code)
					);
				"""
				)
		return

	def __buildTableHistoricalData(self):
		if(not self.__checkExists("historical_data")):
			print("Constructing historical_data table")
			self.cursor.execute(
				"""
					CREATE TABLE historical_data
					(
						country_code 	varchar(5)		NOT NULL,
						indicator_code 	varchar(20) 	NOT NULL,
						FOREIGN KEY(country_code) REFERENCES Countries(code),
						FOREIGN KEY(indicator_code) REFERENCES Indicators(code)
					);
				"""
				)

			for i in range(1960, 2016):
				self.cursor.execute(
					"""
						ALTER TABLE historical_data ADD COLUMN {0} FLOAT NOT NULL;
					""".format("y_" + str(i))
					)

	def construct(self):
		self.__buildTableCountries()
		self.__buildTableIndicators()
		self.__buildTableHistoricalData()
		self.db.commit()

	def fillContries(self, cnt_code, cnt_name, region, inc_grp, notes):
		self.cursor.execute(
			"""
				INSERT INTO countries VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');
			""".format(cnt_code, cnt_name, region, inc_grp, notes).encode('utf-8')
			)
		pass

	def fillCountriesChunk(self, cnt_code, cnt_name, region, inc_grp, notes, chunk_size):
		data_len 	= len(cnt_code)

		for i in xrange(0, data_len, chunk_size):
			self.cursor.execute(""" BEGIN TRANSACTION; """)
			
			for j in range(i, min(i + chunk_size, data_len)):
				self.fillContries(cnt_code[j], cnt_name[j], region[j], inc_grp[j], notes[j])

			self.cursor.execute(""" COMMIT; """)


	def fillIndicators(self, ind_code, ind_name, notes):
		self.cursor.execute(
			"""
				INSERT INTO indicators VALUES ('{0}', '{1}', '{2}');
			""".format(ind_code, ind_name, notes).encode('utf-8')
			)
		pass

	def fillIndicatorsChunk(self, ind_code, ind_name, notes, chunk_size):
		data_len 	= len(ind_code)

		for i in xrange(0, data_len, chunk_size):
			self.cursor.execute(""" BEGIN TRANSACTION; """)
			
			for j in range(i, min(i + chunk_size -1, data_len)):
				self.fillIndicators(ind_code[j], ind_name[j], notes[j])

			self.cursor.execute(""" COMMIT; """)


	def fillHD(self, cnt_code, ind_code, data):
		self.cursor.execute(
			"""
				INSERT INTO historical_data VALUES ('{0}', '{1}', {2});
			""".format(cnt_code, ind_code, ",".join(str(round(i, 3)) for i in data))
			)
		pass

	def fillHDChunk(self, cnt_code, ind_code, data, chunk_size):
		data_len 	= len(cnt_code)

		for i in xrange(0, data_len, chunk_size):
			self.cursor.execute(""" BEGIN TRANSACTION; """)

			for j in range(i, min(i + chunk_size -1, data_len)):
				self.fillHD(cnt_code[j], ind_code[j], data.ix[j])

			self.cursor.execute(""" COMMIT; """)

if __name__ == "__main__":
	with DbConnector("environ", "ilumone", "ilumone") as db:
		db.construct()