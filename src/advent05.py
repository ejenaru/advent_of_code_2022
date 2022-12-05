import sys
import utils


example = sys.argv[1:]

if example:
  file = utils.get_example()
else:
	file = utils.get_input()

input_list = list(file.read().splitlines())

def get_cargo_list():
  cargo_list = []
  for i in range(0, len(input_list[0]), 4):
    cargo_list.append([]) 
  return cargo_list


instructions = []
cargo_list = get_cargo_list()

    
def print_cargo():
  for stack in cargo_list:
    print(cargo_list.index(stack), end = '')
    for item in stack:
      print(item, end = '')
    print()

def turn_cargo():
  for i in range(len(cargo_list)):
    cargo_list[i].reverse()

def get_initial_stack():
  global instructions

  for line_raw in input_list:
    #Fills the stack inside cargo_list
    if line_raw[:3:] == ' 1 ':
      #get instructions out
      instructions = input_list[input_list.index(line_raw) + 2:len(input_list)]
      #for instruction in input_list[input_list.index(line_raw) + 2:len(input_list)]:
      #  instructions.append(instruction)
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
  turn_cargo()
  

  return cargo_list







def do_instrucctions():
  for line in instructions:

    ins = line.split(" ")
    num = int(ins[1])
    cargo_from = int(ins[3]) - 1
    cargo_to = int(ins[5]) - 1
    
    for i in range(num):
      cargo_list[cargo_to].append(cargo_list[cargo_from].pop())
      
 
def part1():
  sum = ''
  get_initial_stack()
  print_cargo()
  print("------------------")
  do_instrucctions()
  print_cargo()
  print("-------------------")
  
  for cargo in cargo_list:
    sum += cargo.pop()
  print('Part 1 ==> {}'.format(sum))



def part2():
  sum = 0

  print('Part 2 ==> {}'.format(sum))




def main():
  
  part1()
  part2()


if __name__ == "__main__":
	main()