with open("input.txt", "r", encoding="utf-8") as puzzle_input:
    input = [line.strip() for line in puzzle_input.readlines()]

columns = [[input[row][i] for row in range(len(input))] for i in range(len(input))]

visible_count = 0
highest_scenic_score = 0


def check_seen(i, j):
    global visible_count
    tree = input[i][j]
    for check_list in [input[i][:j], input[i][::-1][:len(input[i])-j-1],
                       columns[j][:i], columns[j][::-1][:len(columns[j])-i-1]]:
        if all(tree > corner_tree for corner_tree in check_list):
            visible_count += 1
            break


def get_scenic_score(i, j):
    global highest_scenic_score
    tree = input[i][j]
    scenic_score = 1
    for check_list in [input[i][:j][::-1], input[i][j+1:],
                       columns[j][:i][::-1], columns[j][i+1:]]:
        if not check_list:
            scenic_score = 0
            break
        for corner_tree_id in range(len(check_list)):
            if tree <= check_list[corner_tree_id]:
                scenic_score *= corner_tree_id + 1
                break
        else:
            scenic_score *= len(check_list)
    highest_scenic_score = max(scenic_score, highest_scenic_score)


for i in range(len(input)):
    for j in range(len(input[0])):
        check_seen(i, j)
        get_scenic_score(i, j)

print(visible_count)  # PART ONE
print(highest_scenic_score)  # PART TWO
