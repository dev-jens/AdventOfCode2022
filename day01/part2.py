
def calc(caloriesList):
    l = list(caloriesList)
    l.sort()
    print(f"Solution Part2 = {sum(l[:3])}")

def main():
    caloriesList= []
    som = 0
    with open("input.txt", 'r') as input:
        lines = input.readlines()
 
    for line in lines:
        if line.strip() == "":
            caloriesList.append(sum)
            som = 0
            continue
        som += int(line)    
            
    caloriesList.append(som)
    calc(caloriesList)
   

if __name__ == '__main__':
    main()