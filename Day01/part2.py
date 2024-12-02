list1 = []
list2 = []
file = open("C:/Users/reyfp/code/advent_of_code_2024/Day01/input.txt", "r")

# read file data and separate it into two lists
for line in file:
    items = line.split()
    list1.append(int(items[0]))
    list2.append(int(items[1]))
file.close()

# calculate similarity score between the lists
similarity_score = 0
for i in range(len(list1)):
    count = list2.count(list1[i])
    similarity_score += (list1[i] * count)

print(similarity_score)