with open("input.txt", "r", encoding="utf-8") as puzzle_input:
    input = [line.strip() for line in puzzle_input.readlines()]

overall_priority = 0
for line in input:
    half = len(line) // 2
    first = line[:half]
    second = line[half:]
    char = ''.join(set(first).intersection(second))
    if char.islower():
        overall_priority += ord(char) - 96
    else:
        overall_priority += ord(char) - 38

print(overall_priority)

# PART TWO:

overall_priority = 0

for line_id in range(0, len(input), 3):
    first = set(input[line_id])
    second = set(input[line_id+1])
    third = set(input[line_id+2])
    char = ''.join(first.intersection(second).intersection(third))
    if char.islower():
        overall_priority += ord(char) - 96
    else:
        overall_priority += ord(char) - 38

print(overall_priority)
