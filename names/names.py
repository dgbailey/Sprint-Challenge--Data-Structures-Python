import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:#O(n)
#     for name_2 in names_2:#O(n)
#         if name_1 == name_2:#O(1)
#             duplicates.append(name_1)#O(1) or O(n)

#so immediately this strikes me as O(n^2). The .append() operation may be trivial as it is only added and not multiplied 
#this Binary search tree solution runs first time in O(n) time (runtime: 0.23218512535095215 seconds)(64 duplicates)
bst = BinarySearchTree()
for name_1 in names_1:
    bst.insert(name_1)

for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

