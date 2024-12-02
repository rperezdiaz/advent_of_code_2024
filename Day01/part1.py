list1 = []
list2 = []
file = open("C:/Users/reyfp/code/advent_of_code_2024/Day01/input.txt", "r")

# read file data and separate it into two lists
for line in file: 
    items = line.split()
    list1.append(int(items[0]))
    list2.append(int(items[1]))
file.close()

# sort lists
list1.sort()
list2.sort()

# calculate distance between lists
distance = 0
for i in range(len(list1)):
    distance += (abs(list1[i] - list2[i]))

print(distance)
    
