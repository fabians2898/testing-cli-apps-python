# test_search_word.py
import pytest
import os
import search_word

from data import listdata, wordsdata


APP_NAME = 'search_word.py'
FILE_NAME = 'test.txt'
FAKE_FILE = 'fake.exe'

@pytest.mark.functional
def test_run():
    res = os.system('python {} -f {}'.format(APP_NAME, FILE_NAME))
    assert res == 0

@pytest.mark.functional
def test_run_inexistent_file():
    res = os.system('python {} -f {}'.format(APP_NAME, FAKE_FILE))
    assert res != 0

@pytest.mark.functional
def test_file_extension():
    valid_ext =  ['.txt', '.csv'] # here you can add new file formats to be validated
    filename, fileext = os.path.splitext(FILE_NAME)
    assert fileext in valid_ext

@pytest.mark.functional
def test_invalid_argument():
    res = os.system('python {} -z {}'.format(APP_NAME, FAKE_FILE))
    assert res != 0

@pytest.mark.functional
def test_help_argument():
    res = os.system('python {} -h'.format(APP_NAME))
    assert res == 0

@pytest.mark.unit
def test_file_encoding():
    valid_encoding =  ['UTF-8'] # here you can add new encoding formats to be validated
    r_file = open(FILE_NAME, 'r')
    assert r_file.encoding in valid_encoding

@pytest.mark.unit
@pytest.mark.parametrize("init, expected", listdata)
def test_sort_by_len(init, expected):
    res = search_word.sort_by_len(init)
    assert res == expected


@pytest.mark.unit
@pytest.mark.parametrize("init, expected", wordsdata)
def test_get_words_from_file(init, expected):
    res = search_word.get_words_from_string(init)
    assert res == expected