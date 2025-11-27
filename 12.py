def is_harshad(n):
    n_str = str(n)
    total = 0
    for digit in n_str:
        total+=int(digit)
    return n % total == 0

# testing
for i in [1, 2, 3, 5, 111, 101, 2002, 99909, 99900]:
    print(f"is_harshad({i}) = {is_harshad(i)}")

# runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_harshad(n)", globals=globals(), number = 1000000)
print("runtime = ", runtime/1000000, "s", sep="")

# counting steps
n_str = str(n)
steps = 1

total = 0
steps+=1

for digit in n_str:
    steps+=1

    total+=int(digit)
    steps+=3

output = n % total == 0
steps+=3

print("step count =", steps)