import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")

def part1(lines):
    caloriesList= []
    sum = 0
    for line in lines:
        if line.strip() == "":
            caloriesList.append(sum)
            sum = 0
            continue
        sum += int(line)    
            
    caloriesList.append(sum)

    print(f"Solution Part1 = {max(caloriesList)}")
    return caloriesList

def part2(caloriesList):
    caloriesList.sort()
    print(f"Solution Part2 = {sum(caloriesList[-3:])}")

def main():
    with open(INPUT_PATH, 'r') as input:
        lines = input.readlines()
        
    caloriesList = part1(lines)
    part2(caloriesList)

if __name__ == '__main__':
    main()