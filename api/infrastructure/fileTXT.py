class FileTXT:

	def __init__(self, file):
		self.lines = []
		self.filepath = file
		self.__read_file()

	def __format_line(self, line, format_list=True):
		if format_list:
			return line.split(',')
		else:
			return ' '.join(line)

	def __read_file(self):
		'''
			Read file
		'''
		archive = open(self.filepath, 'r')
		lines = []
		for line in archive:
			line = line.strip()
			line = self.__format_line(line)
			lines.append(line)
		archive.close()

		self.lines = lines

	def get_lines(self):
		return self.lines

	def write_file(self, lines):
		with open(self.filepath, "a+") as file_object:
			file_object.seek(0)
			data = file_object.read(100)
			if len(data) > 0 :
				file_object.write("\n")

			for line in lines:
				line_formated = self.__format_line(line, format_list=False)
				file_object.write(line_formated)

		return True

