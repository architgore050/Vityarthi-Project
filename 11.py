def is_deficient(n):
    if n == 1:
        return True 
    total = 1 
    i = 2
    while i * i <= n:
        if n % i == 0:
            total += i
            if i != n / i:
                total += n / i
        i += 1
    return total < n

# testing
for i in [1, 2, 3, 5, 10, 11, 12, 15, 17, 50, 200, 2001]:
    print(f"is_deficient({i}) = {is_deficient(i)}")

# runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_deficient(n)", globals=globals(), number = 1000000)
print("runtime = ", runtime/1000000, "s", sep="")

#counting steps
steps=1
if n == 1:
    steps+=1

    output = True
    steps+=1

total = 1
steps+=1

i = 2
steps+=1

steps+=2
while i * i <= n:
    steps+=1

    steps+=2
    if n % i == 0:
        steps+=1

        total += i
        steps+=1

        steps+=2
        if i != n / i:
            steps+=1

            total += n / i
            steps+=2
    
    i += 1
    steps+=2

output =  total < n
steps+=2

print("Step count =", steps)