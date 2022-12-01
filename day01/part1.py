def main():
    caloriesList= []
    sum = 0

    with open("input.txt", 'r') as input:
        lines = input.readlines()

    for line in lines:
        if line.strip() == "":
            caloriesList.append(sum)
            sum = 0
            continue
        sum += int(line)    
            
    caloriesList.append(sum)

    print(max(caloriesList))

if __name__ == '__main__':
    main()