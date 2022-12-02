def main():
    file = open("input.txt", "r")
    max_cals = [0]
    cur_cal = 0
 
    for line in file:
        if line == "\n":
            max_cals.append(cur_cal)
            cur_cal = 0
        else:
            cur_cal += int(line.strip())
 
    max_cals.sort()
    print("Max cals: " + str(max_cals[-1]))
    print("Sum top 3 max cals: " + str(max_cals[-1] + max_cals[-2] + max_cals[-3]))
 
 
if __name__ == "__main__":
    main()
 
