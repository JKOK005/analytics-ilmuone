import os
from Excel import Excel 
from ParseExcel import ExcelParser
from GenEnvironDb import DbConnector

if __name__ == "__main__":
	parser 	= ExcelParser(os.path.join("..", "data"))

	with DbConnector("environ", "ilumone", "ilumone") as db:
		# Migrate countries data
		excel 	= Excel().setFileName("environ.xlsx").setSheetName("Metadata - Countries").SkipRows(0)
		res 	= parser.read(excel)
		db.fillCountriesChunk(res['Country Code'], res['Country Name'], res['Region'], res['IncomeGroup'], res['SpecialNotes'], 100)
		
		# Migrate indicators data
		excel 	= Excel().setFileName("environ.xlsx").setSheetName("Metadata - Indicators").SkipRows(0)
		res 	= parser.read(excel)
		db.fillIndicatorsChunk(res['INDICATOR_CODE'], res['INDICATOR_NAME'], res['SOURCE_NOTE'], 100)

		# Migrate historical data
		excel 	= Excel().setFileName("environ.xlsx").setSheetName("Data").SkipRows(3)
		res 	= parser.read(excel)
		db.fillHDChunk(res['Country Code'], res['Indicator Code'], res.ix[:, '1960':'2015'], 100)