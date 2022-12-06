with open("input.txt", "r", encoding="utf-8") as puzzle_input:
    input = puzzle_input.read().strip()

packet_found = False
for id in range(len(input)):
    seq_of_four = [input[id+i] for i in range(4)]
    seq_of_fourteen = [input[id+i] for i in range(14)]
    if len(seq_of_four) == len(set(seq_of_four)) and not packet_found:
        packet_marker = id+4
        packet_found = True
    if len(seq_of_fourteen) == len(set(seq_of_fourteen)):
        message_marker = id+14
        break

print(packet_marker)  # PART ONE
print(message_marker)  # PART TWO
