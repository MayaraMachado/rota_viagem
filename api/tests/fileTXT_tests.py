import unittest.mock 
import pytest
from api.infrastructure.fileTXT import FileTXT

#  teste instanciar um arquivo
def test_read_file_txt():
    file = "files/input-file-test.txt"
    file_txt = FileTXT(file)
    assert file_txt.valid == True

# teste instaciar um arquivo que não existe
def test_read_invalid_file_txt():
    file = "files/input-file-test-invalid.txt"
    with pytest.raises(FileNotFoundError):
        file_txt = FileTXT(file)

# teste obter linhas de um arquivo
def test_get_read_lines_file():
    file = "files/input-file-test.txt"
    file_txt = FileTXT(file)
    assert type(file_txt.get_lines()) == list

# teste escrever uma linha no arquivo
def test_write_new_line_file():
    file = "files/input-file-test.txt"
    line = [['XXX', 'YYY', '10']]
    file_txt = FileTXT(file)
    response = file_txt.write_file(line)
    assert response == True

# teste escrever duas linhas
def test_write_new_lines_file():
    file = "files/input-file-test.txt"
    line = [['XXX', 'YYY', '10'], ['WWW', 'HHH', '9']]
    file_txt = FileTXT(file)
    response = file_txt.write_file(line)
    assert response == True
