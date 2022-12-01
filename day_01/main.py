with open("input.txt", "r", encoding="utf-8") as puzzle_input:
    input = puzzle_input.readlines()

elves = []
current_elf = 0
for line in input:
    if line == "\n":
        elves.append(current_elf)
        current_elf = 0
        continue
    current_elf += int(line[:-1])

thirst_three = sorted(elves, reverse=True)[:3]
print(thirst_three)
print(sum(thirst_three))
