import os.path


INPUT_PATH = os.path.join(os.path.dirname(__file__), "input.txt")


def main():
    marker = ""

    with open(INPUT_PATH, 'r') as input:
        lines = input.read()

    for char in lines:
        if len(marker) < 4:
            marker += char
        else:
            marker = marker[1:] + char
    
        if len(set(marker)) >= 4:
            break
        
    print("solution part1 = ", lines.index(marker) + 4)
       

   

if __name__ == '__main__':
    main()