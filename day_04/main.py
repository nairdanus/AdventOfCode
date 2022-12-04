with open("input.txt", "r", encoding="utf-8") as puzzle_input:
    input = [line.strip() for line in puzzle_input.readlines()]

total_duplicates = 0
partial_duplicates = 0

for line in input:
    first_elf, second_elf = ((int(y), int(z)) for y, z in [r.split("-") for r in line.split(",")])
    first_range = range(first_elf[0], first_elf[1]+1)
    second_range = range(second_elf[0], second_elf[1]+1)

    if all(x in first_range for x in second_range) or all(y in second_range for y in first_range):
        total_duplicates += 1

    if set(first_range).intersection(second_range):
        partial_duplicates += 1


print(f"Answer part one: {total_duplicates}")
print(f"Answer part two: {partial_duplicates}")
