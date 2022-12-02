def main():
    file = open("input.txt", "r")
    max_cals = [0]
    cur_cal = 0
 
    for line in file:
        if line == "\n":
            print("Cur cal: " + str(cur_cal))
            max_cals.append(cur_cal)
            cur_cal = 0
        else:
            cur_cal += int(line.strip())
 
    max_cals.sort()
    print("Max_Cals: " + str(max_cals))
    print(str(max_cals[-1] + max_cals[-2] + max_cals[-3]))
 
 
if __name__ == "__main__":
    main()
 