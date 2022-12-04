import os.path


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def main():
    priority = 0
    with open(INPUT_PATH, 'r') as input:
        lines = input.readlines()

    for i in range(0, len(lines), 3):
        p1, p2, p3 = lines[i], lines[i+1], lines[i+2]
        for j in range(len(p1)):
            if p2.__contains__(p1[j]) and p3.__contains__(p1[j]):
                if p1[j].islower():
                    priority += ord(p1[j]) - 96
                else:
                    priority += ord(p1[j]) - 38
                break
    print(priority)

if __name__ == '__main__':
    main()