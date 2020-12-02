from parse import *

def main():
    # part 1
     f = open("input2.txt", "r")
     i = 0
     for x in f:
        line = parse("{}-{} {}: {}", x)
        min = int(line[0])
        max = int(line[1])
        c = line[2]
        psw = line[3]
        occurence = psw.count(c)
        if(occurence >= min and occurence <= max): i+=1
     print("part1 : ", i)
     f.close() 

    # part 2
     f = open("input2.txt", "r")
     i = 0
     for x in f:
        line = parse("{}-{} {}: {}", x)
        pos1 = int(line[0]) - 1
        pos2 = int(line[1]) - 1
        c = line[2]
        psw = line[3]
        if((psw[pos1] == c) != (psw[pos2] == c)): i+=1
     print("part2 : ", i)
     f.close() 
     return


if __name__ == "__main__":
    main()