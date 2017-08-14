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
				SELECT EXISTS (SELECT * FROM information_schema.tables where table_name={0});
			""".format(table_name)
			)
		return bool(self.cursor.fetchone()[0])

	def __buildTableCountries(self):
		if(not self.__checkExists("Countries")):
			print("Constructing countries table")
			self.cursor.execute(
				"""
					CREATE TABLE Countries
					(
						code 	varchar(5) 		NOT NULL,
						name 	varchar(100) 	NOT NULL,
						region 	varchar(50) 	NOT NULL,
						inc_grp varchar(50),
						notes 	varchar(400),

						PRIMARY KEY(code),
					);
				"""
				)
		return

	def __buildTableIndicators(self):
		if(not self.__checkExists("Indicators")):
			print("Constructing indicators table")
			self.cursor.execute(
				"""
					CREATE TABLE Indicators
					(
						code 	varchar(5)		NOT NULL,
						name 	varchar(100) 	NOT NULL,
						notes 	varchar(400),

						PRIMARY KEY(code),
					);
				"""
				)
		return

	def __buildTableHistoricalData(self):
		if(not self.__checkExists("Historical_data")):
			print("Constructing historical_data table")
			self.cursor.execute(
				"""
					CREATE TABLE Historical_data
					(
						country_code 	varchar(5)		NOT NULL,
						indicator_code 	varchar(100) 	NOT NULL,
						{0}

						FOREIGN KEY(country_code) REFERENCES Countries(code),
						FOREIGN KEY(indicator_code) REFERENCES Indicators(code),
					);
				""".format(",".join([str(i) + " decimal(4,5) not null" for i in range(1960, 2016)]))
				)

	def construct(self):
		self.__buildTableCountries()
		self.__buildTableIndicators()
		self.__buildTableHistoricalData()

if __name__ == "__main__":
	with DbConnector("environ", "ilumone", "ilumone") as db:
		db.construct()