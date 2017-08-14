import os
import pandas as pd
import numpy as np
from Excel import Excel

class ExcelParser(object):
	def __init__(self, data_path):
		cwd 			= os.getcwd()
		self.data_path 	= os.path.join(cwd, data_path)

	def read(self, excel_obj):
		file 	= os.path.join(self.data_path, excel.getFileName())
		res 	= pd.read_excel(file, sheetname=excel.getSheetName(), skiprows=excel.getSkipRows())
		res.fillna(0, inplace=True)
		return res

if __name__ == "__main__":
	parser 	= ExcelParser(os.path.join("..", "data"))
	excel 	= Excel().setFileName("environ.xlsx").setSheetName("Data").SkipRows(3)
	res 	= parser.read(excel)
	import IPython
	IPython.embed()