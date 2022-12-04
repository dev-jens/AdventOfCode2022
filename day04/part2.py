import os.path


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def main():
    pairsP1 = 0
    pairsP2 = 0
    with open(INPUT_PATH, 'r') as input:
        lines = input.readlines()
 
    for line in lines:
        e1, e2 = line.split(',')
        s1Min, s1Max = e1.split('-')
        s2Min, s2Max = e2.split('-')
        elv1 = []
        elv2 = []
        for i in range(int(s1Min), int(s1Max) + 1):
            elv1.append(i)
        for i in range(int(s2Min), int(s2Max) + 1):
            elv2.append(i)
   
        if (elv1[0] >= elv2[0] and elv1[-1] <= elv2[-1]) or (elv2[0] >= elv1[0] and elv2[-1] <= elv1[-1]):
            pairsP1 += 1
        if (elv1[0] >= elv2[0] and elv1[0] <= elv2[-1]) or (elv2[0] >= elv1[0] and elv2[0] <= elv1[-1]):
            pairsP2 += 1
    print("Part 1: " + str(pairsP1))
    print("Part 2: " + str(pairsP2))
   
 
    
      
      

if __name__ == '__main__':
    main()