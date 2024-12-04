data = open('2024/1/data.txt').read().splitlines()

list1 = []
list2 = []

for line in data:
    n1, n2 = line.split('   ')
    list1.append(int(n1))
    list2.append(int(n2))

list1.sort()
list2.sort()

total_distance = 0

for i in range(len(list1)):
    distance = abs(list1[i] - list2[i])
    total_distance += distance
    
print(f"Total distance: {total_distance}")

total_similarity = 0

for id1 in list1:
    counter = 0
    for id2 in list2:
        if id1 == id2:
            counter += 1
    
    similarity = id1 * counter
    total_similarity += similarity
    
print(f"Total similarity: {total_similarity}")