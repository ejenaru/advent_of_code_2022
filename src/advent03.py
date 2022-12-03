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
  
  for string in input_list:
    rucksack = get_rucksack_data(string)
    sum = sum + get_priority(rucksack["object"])
  print('Part 1 ==> {}'.format(sum))
def get_priority(letter):
  return ord(letter) - 96 if letter.islower() else ord(letter) - 38
def get_rucksack_data(rucksack):
  
  compart_len = int(len(rucksack)/2)
  compartment1 = rucksack[:compart_len:]
  compartment2 = rucksack[compart_len::]

  rucksack_data = {
    "compartment1": compartment1,
    "compartment2": compartment2,
    "compart_len": compart_len,
    "object": ''.join(set(compartment1)&set(compartment2))
  }
  return rucksack_data 


def part2():
  sum = 0
  for i in range(0, len(input_list), 3):
    group = [input_list[i], input_list[i + 1], input_list[i + 2]]
    sum += get_priority(get_badge(group))
  print('Part 2 ==> {}'.format(sum))

def get_badge(group):
  return ''.join(set(group[0])&set(group[1])&set(group[2]))


def main():
  
  part1()
  part2()


if __name__ == "__main__":
	main()