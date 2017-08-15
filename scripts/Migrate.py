import os
from Excel import Excel 
from ParseExcel import ExcelParser
from GenEnvironDb import DbConnector

if __name__ == "__main__":
	parser 	= ExcelParser(os.path.join("..", "data"))
	excel 	= Excel().setFileName("environ.xlsx").setSheetName("Data").SkipRows(3)
	res 	= parser.read(excel)
	import IPython
	IPython.embed()

	with DbConnector("environ", "ilumone", "ilumone") as db:
		db.construct()