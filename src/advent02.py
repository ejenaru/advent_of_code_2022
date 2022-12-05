import sys
import utils

example = sys.argv[1:]

if example:
  file = utils.get_example()
else:
	file = utils.get_input()


input_list = list(file.read().splitlines())

points_dict = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

self_c = {
  "X": "Rock",
  "Y": "Paper",
  "Z": "Scissors"
}

oponent_c = {
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors"
}



def match_result(oponent_key,self_key):
  if self_c[self_key] == oponent_c[oponent_key]:
    return 3
  elif self_c[self_key] == "Rock" and oponent_c[oponent_key] == "Scissors":
    return 6
  elif self_c[self_key] == "Scissors" and oponent_c[oponent_key] == "Paper":
    return 6
  elif self_c[self_key] == "Paper" and oponent_c[oponent_key] == "Rock":
    return 6
  else:
    return 0
  
def part1():
  sum = 0
  for line in input_list:
    opo = line[0]
    slf = line[2]
    sum += match_result(opo,slf) + points_dict[slf]
  print('Part 1 ==> {}'.format(sum))



def part2():
  sum = 0

  print('Part 2 ==> {}'.format(sum))



def main():
  
  part1()
  part2()


if __name__ == "__main__":
	main()