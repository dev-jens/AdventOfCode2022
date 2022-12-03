opponentDict = {
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors"
}

def pointsForPlaying(choice):
    if choice == "A": 
        return 1
    elif choice == "B": 
        return 2
    elif choice == "C":
        return 3  

def main():
    options = list(opponentDict.keys())
    points = 0
    with open("input.txt", 'r') as input:
        lines = input.readlines()
    for line in lines:
        line = line.split(" ")
        opp_choice, outcome = line[0], line[1].strip()

        opp_choice_index = options.index(opp_choice)
        my_choice = opp_choice
        points += 3
        if outcome == 'X':
            my_choice = options[(opp_choice_index + 2) % 3]
            points -=3
        elif outcome == 'Z':
            my_choice = options[(opp_choice_index + 1) % 3]
            points += 3
    
        points += pointsForPlaying(my_choice)
       
    print(points)
    
if __name__ == "__main__":
    main()