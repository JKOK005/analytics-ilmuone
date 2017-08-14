class Excel(object):
	def __init__(self):
		self.file_name 	= None;
		self.sheet_name = None;
		self.skip_rows 	= 0;

	def setFileName(self, file_name):
		self.file_name 	= file_name
		return self

	def setSheetName(self, sheet_name):
		self.sheet_name = sheet_name
		return self

	def SkipRows(self, rows):
		self.skip_rows 	= rows;
		return self

	def getFileName(self):
		return self.file_name

	def getSheetName(self):
		return self.sheet_name

	def getSkipRows(self):
		return self.skip_rows

	def build():
		return 
