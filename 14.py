def is_pronic (n):
    if n == 0:
        return True
    if n == 1:
        return False
    i = 2
    while i <= n**(1/2):
        if n % i == 0:
            a = n/i
            if a+1 == i or i+1 == a:
                return True
        i+=1
    return False

#testing
for i in [0, 1, 2, 3, 4, 5, 6, 7, 12, 20, 21, 17, 20, 50, 100, 200, 2000]:
    print(f"is_pronic({i}) =", is_pronic(i))

#runtimwe
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_pronic(n)", globals=globals(), number = 1000000)
print("runtime = ", runtime/1000000, "s", sep="")

# countign steps
def is_pronic (n):
    steps=1
    if n == 0:
        steps+=1

        steps+=1
        return True, steps

    steps+=1
    if n == 1:
        steps+=1

        steps+=1
        return False, steps
    
    i = 2
    steps+=1

    steps+=2
    while i <= n**(1/2):
        steps+=1

        steps+=2
        if n % i == 0:
            steps+=1

            a = n/i
            steps==2

            steps+=5
            if a+1 == i or i+1 == a:
                steps+=1

                steps+=1
                return True, steps
        i+=1
        steps+=2
    
    steps+=1
    return False, steps

print("step count =", is_pronic(n)[1])