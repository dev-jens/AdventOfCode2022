opponentDict = {
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors"
}
playerDict ={
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}

def pointsForPlaying(choice):
    if playerDict[choice] == "Rock": 
        return 1
    elif playerDict[choice] == "Paper": 
        return 2
    elif playerDict[choice] == "Scissors":
        return 3  

def main():
    points = 0
    last = ""
    with open("input.txt", 'r') as input:
        lines = input.readlines()
    for line in lines:
        line = line.split(" ")
        opp_choice, player_choice= line[0], line[1].strip()

        if playerDict[player_choice] == "Rock" and opponentDict[opp_choice] == "Scissors" or playerDict[player_choice] == "Paper" and opponentDict[opp_choice] == "Rock" or playerDict[player_choice] == "Scissors" and opponentDict[opp_choice] == "Paper":
            points += 6
        elif opponentDict[opp_choice] == playerDict[player_choice]:
            points += 3
        points += pointsForPlaying(player_choice)
    print(points)
    
if __name__ == "__main__":
    main()