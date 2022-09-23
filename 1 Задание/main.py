
def f8(x):
    if x%8==0:
        return 1
    return 0

def square(x):
    return x * x

list1 = list(filter(f8, range(10,10000,10)))

list2 = list(map(square, list1))

listOfTuples = list(zip(*[list1, list2]))

print(listOfTuples)
