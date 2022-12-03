import sys


RES_PATH = ".\\input\\"
INPUT = "input"
EXAMPLE = "example"
TXT = ".txt"

def get_input():
	file_path = RES_PATH + INPUT + sys.argv[0][-5:-3] + TXT
	return open(file_path, "r")

def get_example():
	file_path = RES_PATH + EXAMPLE + sys.argv[0][-5:-3] + TXT
	return open(file_path, "r")