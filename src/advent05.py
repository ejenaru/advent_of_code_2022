import sys
import utils

example = sys.argv[1:]

if example:
  file = utils.get_example()
else:
	file = utils.get_input()

input_list = list(file.read().splitlines())

def get_empty_cargo_list():
  cargo_list = []
  for i in range(0, len(input_list[0]), 4):
    cargo_list.append([]) 
  return cargo_list

instructions = []

    
def print_cargo(cargo_list):
  for stack in cargo_list:
    print(cargo_list.index(stack), end = '')
    for item in stack:
      print(item, end = '')
    print()

def turn_cargo(cargo_list):
  for i in range(len(cargo_list)):
    cargo_list[i].reverse()

def get_initial_stack(cargo_list):
  global instructions

  for line_raw in input_list:
    #Fills the stack inside cargo_list
    if line_raw[:3:] == ' 1 ':
      #get instructions out
      instructions = input_list[input_list.index(line_raw) + 2:len(input_list)]
      break
    #Iterate through lines to fill stack (upsidedown)
    line = [line_raw[x:x + 3] for x in range(0, len(line_raw), 4)]
    
    #for item in line:
    for i in range(len(line)):
      item = line[i]
      if item == '   ':
        continue
      cargo_list[i].append(item)
    #print('DEBUG: ', line)
    #print('ITERATE:  ',  input_list.index(line_raw))
  turn_cargo(cargo_list)
  

  return cargo_list

def do_instrucctions(cargo_list):
  for line in instructions:

    ins = line.split(" ")
    num = int(ins[1])
    cargo_from = int(ins[3]) - 1
    cargo_to = int(ins[5]) - 1
    
    for i in range(num):
      cargo_list[cargo_to].append(cargo_list[cargo_from].pop())
      
def do_instructions_2(cargo_list):
  temp_list = []
  for line in instructions:

    ins = line.split(" ")
    num = int(ins[1])
    cargo_from = int(ins[3]) - 1
    cargo_to = int(ins[5]) - 1
    
    for i in range(num):
      temp_list.append(cargo_list[cargo_from].pop())
    temp_list.reverse()
    cargo_list[cargo_to].extend(temp_list)
    temp_list.clear()


def part1():
  print("PART_1 ___________________________")
  sum = ''
  cargo_list = get_empty_cargo_list()
  get_initial_stack(cargo_list)
  print_cargo(cargo_list)
  print("------------------")
  do_instrucctions(cargo_list)
  print_cargo(cargo_list)
  print("-------------------")
  
  for cargo in cargo_list:
    sum += cargo.pop()
  print('Solution ==> {}'.format(sum))



def part2():
  print("PART_2_______________________________")
  
  cargo_list = get_empty_cargo_list()
  get_initial_stack(cargo_list)
  sum=''
  print_cargo(cargo_list)
  print("-----------")
  do_instructions_2(cargo_list)
  print_cargo(cargo_list)
  for cargo in cargo_list:
    sum += cargo.pop()

  print('Solution ==> {}'.format(sum))




def main():
  
  part1()
  part2()


if __name__ == "__main__":
	main()