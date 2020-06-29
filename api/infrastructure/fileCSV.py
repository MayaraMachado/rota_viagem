import csv

class FileCSV:
	def __init__(self, file):
		self.filepath = file
		self.lines = []
		self.__read_file()

	def __format_line(self, line, format_list=False):
		if format_list:
			return line.split(',')
		else:
			return ','.join(line)

	def __read_file(self):
		'''
			Read file

			raises:
			FileNotFoundError:
		'''
		with open(self.filepath, mode='r') as csv_file:
			reader = csv.reader(csv_file)
			self.lines = list(reader)

	def get_lines(self):
		return self.lines

	def write_file(self, lines):
		with open(self.filepath, 'a', newline='\n') as csv_file:
			for row in lines:
				row = self.__format_line(row)
				csv_file.write(row)
				csv_file.write('\n')
		return True