import sys
import utils


example = sys.argv[1:]

if example:
  file = utils.get_example()
else:
	file = utils.get_input()


input_list = list(file.read().splitlines())
 
def part1():
  sum = 0
  for pair in input_list:
    range1 = range(int(pair.split(',')[0].split('-')[0]),int(pair.split(',')[0].split('-')[1]))
    range2 = range(int(pair.split(',')[1].split('-')[0]),int(pair.split(',')[1].split('-')[1]))
    sum += 1 if check_range(range1, range2) else 0
  
  print('Part 1 ==> {}'.format(sum))
  
def check_range(range1, range2):
  #Checks both ways
  check1 = range1.start <= range2.start and range1.stop >= range2.stop
  check2 = range2.start <= range1.start and range2.stop >= range1.stop
  return check1 or check2



def part2():
  sum = 0
  print('Part 2 ==> {}'.format(sum))



def main():
  
  part1()
  part2()


if __name__ == "__main__":
	main()