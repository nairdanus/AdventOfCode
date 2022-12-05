def stack_manipulation_part_one():
    for n in range(n_items):
        stacks[destination].append(
            stacks[origin].pop()
        )

def stack_manipulation_part_two():
    stacks[destination].extend(
        reversed([stacks[origin].pop() for _ in range(n_items)])
    )


with open("input.txt", "r", encoding="utf-8") as puzzle_input:
    input = [line[:-1] for line in puzzle_input.readlines()]


items = []

for line_id, line in enumerate(input):
    if not input[line_id+1]:
        start_of_commands = line_id + 2
        break

    items.append([line[i:i+4] for i in range(0, len(line), 4)])

stacks = {}

for row in reversed(items):
    for id, item in enumerate(row):
        if id+1 not in stacks.keys():
            stacks[id+1] = []
        if item.strip():
            stacks[id+1].append(item.strip())

for line in input[start_of_commands:]:
    split = line.split()
    n_items = int(split[1])
    origin = int(split[3])
    destination = int(split[5])

    # stack_manipulation_part_one()
    stack_manipulation_part_two()

res = [stack[-1] for stack in stacks.values()]
print(res)