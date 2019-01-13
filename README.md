Automation testing for CLI apps using Python
============================================

This repository have an approach for test CLI apps, focusing mainly in two kinds of tests: unit testing for the functions that compose the CLI app and functional testing using the app itself, using like a example a simple python 3 script to find the longest word in a plain text file, the tests were built using pytest.

Installing
----------

Install and update using:

    $ pip install -r requirements.txt


search_word.py
--------------

Run using above command:

    python search_word.py -f text_file_path


Running the tests
-----------------

For setting up the environment to run the tests go to test_search_word.py to place the files paths, for defect are setting this:

    # test_search_word.py

    APP_NAME = 'search_word.py' 
    FILE_NAME = 'test.txt'
    FAKE_FILE = 'fake.exe'

To run all the suite:

    $ pytest -v

To run only unit tests:

    $ pytest -v -m unit

To run only functional tests:

    $ pytest -v -m functional