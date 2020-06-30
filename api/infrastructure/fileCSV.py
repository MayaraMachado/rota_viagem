import csv

class FileCSV:
	'''
		Class responsible for managing the reading and writing of the query file.
	'''
	def __init__(self, file):
		'''
			Instance and makes the call to read the file.

			Args:
			----
			- file (str) filepath to access
		'''
		self.lines = []
		self.filepath = file
		self.valid = self.__read_file()


	def __format_line(self, line, format_list=False):
		'''
			Transcribes the structure of the line, it can be either as the result 
			of reading a file to make it a list, or writing it to a file, to make 
			the list string.

			Args:
			----
			- line (list or str) object representing the line that was executed.
			- format_list (boolean) indicates whether to transform to list.

			Returns:
			-----
			- (list or str) the result of the formatting

		'''
		if format_list:
			return line.split(',')
		else:
			return ','.join(line)

	def __read_file(self):
		'''
			Read the file.

			Returns:
			---
			- boolean indicating whether the reading was completed.

			Raises:
			----
			- FileNotFoundError:
				- If the file is not found while attempting to read.
		'''
		with open(self.filepath, mode='r') as csv_file:
			reader = csv.reader(csv_file)
			self.lines = list(reader)

		return True

	def get_lines(self):
		'''
			Gets the lines from the read file

			Returns:
			----
			- list of lists
		'''
		return self.lines

	def write_file(self, lines):
		'''
			Write at the end of an existing file.

			Args:
			-----
			- lines (list of list) representing the lines to be written in the file.

			Returns:
			---
			- boolean indicating whether the writing was completed.

			Raises:
			----
			- FileNotFoundError:
				- If the file is not found while attempting to write.
		'''
		with open(self.filepath, 'a', newline='\n') as csv_file:
			for row in lines:
				row = self.__format_line(row)
				csv_file.write('\n')
				csv_file.write(row)
		return True