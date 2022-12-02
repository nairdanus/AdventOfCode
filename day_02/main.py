with open("input.txt", "r", encoding="utf-8") as puzzle_input:
    input = [line.strip() for line in puzzle_input.readlines()]

# YAAY SWITCH CASE !!

score_part_one = 0

for line in input:
    match line.split():
        case ["A", "X"]:
            score_part_one += 4
        case ["A", "Y"]:
            score_part_one += 8
        case ["A", "Z"]:
            score_part_one += 3
        case ["B", "X"]:
            score_part_one += 1
        case ["B", "Y"]:
            score_part_one += 5
        case ["B", "Z"]:
            score_part_one += 9
        case ["C", "X"]:
            score_part_one += 7
        case ["C", "Y"]:
            score_part_one += 2
        case ["C", "Z"]:
            score_part_one += 6

print(score_part_one)


score_part_two = 0

for line in input:
    match line.split():
        case ["A", "X"]:
            score_part_two += 3
        case ["A", "Y"]:
            score_part_two += 4
        case ["A", "Z"]:
            score_part_two += 8
        case ["B", "X"]:
            score_part_two += 1
        case ["B", "Y"]:
            score_part_two += 5
        case ["B", "Z"]:
            score_part_two += 9
        case ["C", "X"]:
            score_part_two += 2
        case ["C", "Y"]:
            score_part_two += 6
        case ["C", "Z"]:
            score_part_two += 7

print(score_part_two)