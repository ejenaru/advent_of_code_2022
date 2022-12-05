import sys
import utils


example = sys.argv[1:]

if example:
  file = utils.get_example()
else:
	file = utils.get_input()


input_list = list(file.read().split("\n\n"))

def part1():
  max = 0
  for elf in input_list:
    count = 0
    for amount in elf.split("\n"):
      count += int(amount)
    max = count if max < count else max
  print('Part 1 ==> Max elf: {}'.format(max))

def part2():
  list_elfs = []
  for elf in input_list:
    count = 0
    for amount in elf.split("\n"):
      count += int(amount)
    list_elfs.append(count)
  max = 0
  list_elfs.sort()
  for i in range(3):
    max +=list_elfs.pop()
  print('Part 2 ==> Increased: {}'.format(max))





def main():
	part1()
	part2()
	
	






if __name__ == "__main__":
	main()