import unittest.mock 
import pytest
from api.infrastructure.fileCSV import FileCSV

#  teste instanciar um arquivo
def test_read_file_csv():
    file = "files/input-file-test.csv"
    file_csv = FileCSV(file)
    assert file_csv.valid == True

# teste instaciar um arquivo que não existe
def test_read_invalid_file_csv():
    file = "files/input-file-test-invalid.csv"
    with pytest.raises(FileNotFoundError):
        file_csv = FileCSV(file)

# teste obter linhas de um arquivo
def test_get_read_lines_file():
    file = "files/input-file-test.csv"
    file_csv = FileCSV(file)
    assert type(file_csv.get_lines()) == list

# teste escrever uma linha no arquivo
def test_write_new_line_file():
    file = "files/input-file-test.csv"
    line = [['XXX', 'YYY', '10']]
    file_csv = FileCSV(file)
    response = file_csv.write_file(line)
    assert response == True

# teste escrever duas linhas
def test_write_new_lines_file():
    file = "files/input-file-test.csv"
    line = [['XXX', 'YYY', '10'], ['WWW', 'HHH', '9']]
    file_csv = FileCSV(file)
    response = file_csv.write_file(line)
    assert response == True
