class FileTXT:
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

	def __format_line(self, line, format_list=True):
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
		archive = open(self.filepath, 'r')
		lines = []
		for line in archive:
			line = line.strip()
			line = self.__format_line(line)
			lines.append(line)
		archive.close()

		self.lines = lines

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
		with open(self.filepath, "a+") as file_object:
			file_object.seek(0)
			data = file_object.read(100)
			if len(data) > 0 :
				file_object.write("\n")

			for line in lines:
				line_formated = self.__format_line(line, format_list=False)
				file_object.write(line_formated)

		return True

