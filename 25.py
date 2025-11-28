def mod_exp (base, exponent, modulus):
    return base**exponent % modulus

#testing
l = [0, 1, 2]
for base in l:
    for exponent in l:
        for modulus in l[1:]:
            print(f"mod_exp({base}, {exponent}, {modulus}) =", mod_exp(base, exponent, modulus))

#runtime
base = int(input("Enter number (base): "))
exponent = int(input("Enter number (exponent): "))
modulus = int(input("Enter number (modulus): "))
import timeit
runtime = timeit.timeit("mod_exp(base, exponent, modulus)", globals=globals(), number = 1000000)
print("Average runtime =", runtime/1000000, "seconds")

#memory usage
import tracemalloc
tracemalloc.start()
mod_exp(base, exponent, modulus)
peak_memory = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print("Peak memory usage =", peak_memory, "Bytes")

#steps counting
print("Number of steps =", 3)