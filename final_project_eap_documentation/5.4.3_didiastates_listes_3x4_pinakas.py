#3x4
from traceback import format_list

array = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

array.insert(0,[0,0,0,0]) #4x4

for row in array:
    for elem in row:
        print("[",elem,"]",end=" ")
    print("")
print("==============================")
for row in array: #4x5
    row.append(1)

for row in array:
    for elem in row:
        print("[",elem,"]",end=" ")
    print("")
