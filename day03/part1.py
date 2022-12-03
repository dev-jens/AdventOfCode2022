import os.path


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def main():
    priority = 0
    with open(INPUT_PATH, 'r') as input:
        lines = input.readlines()
    for s in lines:
        p1,p2 = s[:len(s)//2] ,s[len(s)//2:]
        # check if p1 and p2 have a same character
        for i in range(len(p1)):
            if p2.__contains__(p1[i]):
                if p1[i].islower():
                    priority += ord(p1[i]) - 96
                else:
                    priority += ord(p1[i]) - 38
                break
    print(priority)

if __name__ == '__main__':
    main()