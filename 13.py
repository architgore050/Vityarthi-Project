def is_automorphic (n):
    n_2 = n**2
    n = str(n)
    n_2 = str(n_2)
    l_n = 0             # length of n
    for i in n:
        l_n += 1
    if n_2[-l_n:]==n:
        return True
    else:
        return False

# testing
for i in [0, 1, 2, 3, 4, 5, 6, 10, 200, 36000, 7000009]:
    print(f"is_automorphic({i}) =", is_automorphic(i))

# runtime calculation
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_automorphic(n)", globals=globals(), number = 1000000)
print("runtime = ", runtime/1000000, "s", sep="")

# steps coujnting
n_2 = n**2
steps = 2

n = str(n)
steps+=2

n_2 = str(n_2)
steps+=2

l_n = 0
steps+=1

for i in n:
    steps+=1

    l_n += 1
    steps+=2

steps+=2
if n_2[-l_n:]==n:
    steps+=1

    output = True
    steps+=1

else:
    output = False
    steps+=1

print("steps count =", steps)