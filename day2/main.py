def part_one():
    file = open("input.txt", "r")

    decrypt = {'X':'A', 'Y':'B', 'Z':'C'}
    beats_guide = {'A':'C', 'B':'A', 'C':'B'}
    symbol_scores = {'A':1, 'B':2, 'C':3}

    def calc_round_results(you, opp):
        if beats_guide[you] == opp:
            return 6
        elif beats_guide[opp] == you:
            return 0
        return 3

    score = 0
    for line in file:
        you, opp = decrypt[line[2]], line[0]
        score += symbol_scores[you] + calc_round_results(you, opp)
        
    file.close()
    return score


def part_two():
    file = open("input.txt", "r")

    expected_results_scores = {'X':0, 'Y':3, 'Z':6}
    symbol_scores = {'A':1, 'B':2, 'C':3}
    beats_guide = {'A':'C', 'B':'A', 'C':'B'}
    loses_guide = {'C':'A', 'A':'B', 'B':'C'}

    def get_you(result, opp):
        match result:
            case 'X':
                return beats_guide[opp]
            case 'Y':
                return opp
            case 'Z':
                return loses_guide[opp]

    score = 0
    for line in file:
        opp, result = line[0], line[2]
        you = get_you(result, opp)
        score += expected_results_scores[result] + symbol_scores[you]

    file.close()
    return score


def main():
    print("Part 1 score: " + str(part_one()))
    print("Part 2 score: " + str(part_two()))
 
 
if __name__ == "__main__":
    main()
 
