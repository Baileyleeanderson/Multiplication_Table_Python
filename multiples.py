#create a for loop for nums from 1 to 1000, do not use a list
for x in range(1, 1001):
    print x
#create a for loop printing multiples of 5 from 5 to 1,000,000

for i in range(5,1000000):
    if i % 5 == 0:
        print(i)
#create a program that adds the sum of all nums in list
def listsum(numList):
    newSum = 0
    for i in numList:
        newSum = newSum + i
    return newSum
print(listsum([1, 2, 5, 10, 255, 3]))
#create a program that prints the avg of all nums in list
def listsum(numList):
    listSum = sum(numList)
    listLength = len(numList)
    listAvg = listSum / listLength
    return listAvg
print(listsum([1, 2, 5, 10, 255, 3]))