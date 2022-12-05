import os.path


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")
LOAD_PATH = os.path.join(os.path.dirname(__file__), "starting_stack.txt")

def printStack(stack):
    for i in range(len(stack)):
       print(stack[i])

def peekTop(stack):
    print("solution part1 = ", end='')
    for i in range(1,len(stack)):
        print(stack[i][-1].replace('[','').replace(']',''), end='')


def main():
    
    stack = []

    with open(LOAD_PATH, 'r') as input:
        lines = input.readlines()

    for line in lines:
        stack.append(line.strip().split(' '))
   
    with open(INPUT_PATH, 'r') as input:
        lines = input.readlines()

    for line in lines:
        line = line.strip().split(' ')
        count = int(line[1])
        stack_from = int(line[3])
        stack_to = int(line[5])
        for i in range(0,int(count)):
            popped = stack[stack_from].pop()
            stack[stack_to].append(popped)
            
    peekTop(stack)

if __name__ == '__main__':
    main()