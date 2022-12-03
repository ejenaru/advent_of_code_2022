import sys


RES_PATH = ".\\input\\"
INPUT = "input"
EXAMPLE = "example"
TXT = ".txt"

def get_file():
	file_path = RES_PATH + INPUT + sys.argv[0][-5:-3] + TXT
	return open(file_path, "r")

def get_example(num):
	file_path = RES_PATH + EXAMPLE + num + TXT
	return open(file_path, "r")