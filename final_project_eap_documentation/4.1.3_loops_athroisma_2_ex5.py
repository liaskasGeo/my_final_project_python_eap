numbers = [1,2,3,4,5,6,7,8,9,10]
count = 0
s = 0

while count < 10:             # while count <= len(numbers):
    s+=numbers[count]
    count+=1

print(f"Sum = {s}")