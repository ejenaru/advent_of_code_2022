import utils


file = utils.get_file()
input_list = list(map(int, file.readlines()))
 
def part1():
	increased = 0
	for i in range(0, len(input_list)):
		if input_list[i] > input_list[i-1]:
			increased+=1
	print('Part 1 ==> Increased: {}'.format(increased))

def part2():
	previous = input_list[0] + input_list[1] + input_list[2]
	increased = 0
	for i in range(3,len(input_list)):
		data = input_list[i] + input_list[i-1] + input_list[i-2]
		if data > previous:
			increased +=1
		previous = data
	print('Part 2 ==> Increased: {}'.format(increased))





def main():
	part1()
	part2()
	
	






if __name__ == "__main__":
	main()