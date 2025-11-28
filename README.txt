# Euler's Totient Function – φ(n)

A lightweight, pure-Python implementation of Euler’s totient function φ(n), which counts how many integers from 1 to n-1 are coprime to n (i.e., gcd(k, n) = 1).  
The code includes a custom recursive Euclidean GCD helper and a direct counting approach, making it easy to understand ## Features
- Computes φ(n) by explicitly checking coprimality for every k in 1 … n-1  
- Custom recursive gcd() function (no imports needed)  
- Simple, readable logic – perfect for learning the definition of the totient function  
- Includes test cases, runtime measurement, and step-counting step counter

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
```
.
├── euler_totient.py
├── README.txt
└── statement.txt
```

## How to Run
Save the code to a file and run:

```bash
python euler_totient.py

_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Möbius Function – μ(n)

A lightweight, pure-Python implementation of the Möbius function μ(n), a fundamental arithmetic function in number theory that returns:  
- 0 if n has a squared prime factor  
- 1 if n has an even number of distinct prime factors  
- -1 if n has an odd number of distinct prime factors  

This version uses only basic loops and trial division — no imports, no factorization libraries — making it perfect for learning and small-to-moderate inputs.

## Features
- Correctly computes μ(n) for all positive integers  
- Detects square factors by checking if any divisor i has integer square root  
- Counts distinct prime factors using naive primality testing on divisors  
- Includes comprehensive test cases (including square-free and square-containing numbers)  
- Measures runtime and total number of executed steps for performance analysis  

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
```
.
├── mobius.py
├── README.txt
└── statement.txt
```

## How to Run
Save the code to a file and run:

```bash
python mobius.py

_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Sum of Divisors Function – σ(n)

A lightweight, pure-Python implementation of the divisor sum function σ(n), which calculates the sum of all positive divisors of n (including 1 and n itself).  
This is one of the most basic and important arithmetic functions in number theory, used in the study of perfect numbers, abundancy, and multiplicative functions.

## Features
- Computes σ(n) by checking every integer from 1 to n for divisibility  
- Simple, easy-to-follow logic — ideal for learning and small-to-moderate inputs  
- Includes test cases for primes, powers, perfect numbers (like 28), and larger values  
- Measures average runtime and total number of executed steps for performance insight  
- Fully self-contained with no external dependencies

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
.
├── divisor_sum.py
├── README.txt
└── statement.txt

## How to Run
Save the code to a file and run:

```bash
python divisor_sum.py
____________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Prime-Counting Function – π(n)

A lightweight, pure-Python implementation of the prime-counting function π(n) — the number of prime numbers less than or equal to n — using a basic Sieve of Eratosthenes variant.  
This function builds a boolean array up to n, marks multiples of each integer starting from 2, and counts the remaining True values (primes).  
Perfect for learning the sieve algorithm and exploring prime distribution up to moderate values.

## Features
- Computes exact π(n) using sieve-style elimination  
- Works correctly for n = 0, 1, and all positive integers  
- Includes extensive test cases up to 1,000,000  
- Measures average runtime and total steps taken (for algorithmic analysis)  
- Simple, readable, educational implementation with no external libraries  

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

**Note:** Memory usage grows linearly with n — suitable up to ~10⁷ on most systems.

## Project Structure
.
├── prime_pi.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python prime_pi.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Legendre Symbol – (a/p)

A lightweight, pure-Python implementation of the Legendre symbol (a/p), which tells whether a is a quadratic residue modulo an odd prime p:  
- Returns **1** if a is a quadratic residue mod p (and a not equivalent to 0 mod p)  
- Returns **-1** if a is a quadratic non-residue mod p  
- (Note: this version assumes p is odd prime and a not equivalent to 0 mod p — returns incorrect value otherwise)

This implementation uses Euler’s criterion: (a/p) equivalent to a^((p-1)/2) mod p — making it extremely simple and fast.

## Features
- Computes (a/p) using direct modular exponentiation (Euler’s criterion)  
- One-liner core logic — perfect for learning and educational  
- Includes classic test cases covering residues and non-residues  
- Measures average runtime over 1 million calls and exact step count  
- No external dependencies — pure Python

## Requirements
- Python 3.x  
- No external dependencies (uses built-in pow-like behavior via **)

**Warning:** This version does **not** handle the case a ≡ 0 (mod p) — it should return 0 in that case. For full correctness, add `if a % p == 0: return 0`.

## Project Structure
.
├── legendre_symbol.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python legendre_symbol.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Factorial – n!

A lightweight, pure-Python implementation of the factorial function n! that computes the product of all positive integers from 1 to n (with 0! = 1).  
This classic function is foundational in combinatorics, probability, and algorithm analysis — and this version is written for clarity and educational use.

## Features
- Computes exact factorial using a simple iterative multiplication loop  
- Includes input validation (non-negative integer only)  
- Handles edge cases correctly: 0! = 1, 1! = 1  
- Tested up to 50! (huge numbers handled effortlessly by Python’s arbitrary-precision integers)  
- Measures average runtime over 1 million calls and total executed steps  
- Clean, readable, and beginner-friendly logic

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
.
├── factorial.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python factorial.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Palindrome Checker – is_palindrome(n)

A lightweight, pure-Python function that checks whether a given integer reads the same forwards and backwards — i.e., it is a numeric palindrome.  
Examples: 121 → True, 12321 → True, 123 → False, 1221 → True.

This implementation converts the number to a string and compares it with its reverse — the fastest and most Pythonic way to solve the problem.

## Features
- Works with positive, negative, and zero inputs  
- Handles very large integers (e.g., 1234567890987654321) effortlessly  
- Extremely simple and readable one-liner core logic  
- Includes comprehensive test cases covering edge cases and large palindromes  
- Measures average runtime (blazing fast — often < 1 microsecond) and exact step count  
- No external dependencies — pure Python

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── palindrome.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python palindrome.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Mean of Digits – mean_of_digits(n)

A lightweight, pure-Python function that calculates the arithmetic mean (average) of all digits in a given integer — positive, negative, or zero.  
It ignores the sign, extracts each digit, and returns the average as a float.

Examples:  
- mean_of_digits(123) → 2.0  
- mean_of_digits(9876) → 7.5  
- mean_of_digits(-123) → 2.0  
- mean_of_digits(1111) → 1.0

Perfect for digit DP problems, checksum ideas, or just curious number exploration!

## Features
- Works correctly with positive, negative, and zero inputs  
- Handles arbitrarily large integers (thanks to Python’s big integers)  
- Clean list-comprehension digit extraction  
- Manually computes sum and length (no `sum()` or `len()` for educational clarity)  
- Includes rich test cases from single digit to 10-digit numbers  
- Measures average runtime and exact step count

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
.
├── mean_of_digits.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python mean_of_digits.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Digital Root – digital_root(n)

A lightweight, pure-Python implementation of the **digital root** function — repeatedly sums the digits of a number until a single digit (1–9) is obtained.  
It works for any integer (positive, negative, or zero) and uses elegant recursion.

Examples:  
- digital_root(9875) → 9 + 8 + 7 + 5 = 29 → 2 + 9 = **11 → 1 + 1 = 2**  
- digital_root(493193) → eventually **2**  
- digital_root(9999) → **9 (famous property: dr(n) = 1 + (n-1) mod 9)

Fun fact: The digital root of any number is equal to `n mod 9`, except when `n mod 9 == 0`, then it's 9 (unless n=0).

## Features
- Handles positive, negative, and zero inputs correctly  
- Uses clean recursive approach — very readable and mathematically natural  
- Works instantly even with extremely large integers  
- Includes comprehensive test cases (including 10-digit and negative numbers)  
- Measures average runtime over 1 million calls — lightning fast!

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
.
├── digital_root.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python digital_root.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Abundant Number Checker – is_abundant(n)

A lightweight, pure-Python function that determines whether a positive integer n is abundant — that is, the sum of its proper divisors (excluding itself) is greater than n.

Examples:  
- 12: divisors 1+2+3+4+6 = 16 > 12 → abundant  
- 18: 1+2+3+6+9 = 21 > 18 → abundant  
- 28: 1+2+4+7+14 = 28 = 28 → perfect (not abundant)  
- 945: first odd abundant number!

Abundant numbers are key in the study of perfect, deficient, and highly composite numbers.

## Features
- Computes sum of all proper divisors by checking divisibility from 1 to n−1  
- Returns True only if sum of proper divisors > n  
- Simple, educational, and easy-to-follow logic  
- Includes test cases with known abundant (12, 18, 945), perfect (28), and prime/deficient numbers  
- Measures average runtime over 1 million calls

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

**Note:** This O(n) approach is fine for learning and small inputs. For large n, a √n version would be much faster.

## Project Structure
.
├── abundant.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python abundant.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Deficient Number Checker – is_deficient(n)

A lightweight, pure-Python function that determines whether a positive integer n is deficient — meaning the sum of its proper divisors (excluding itself) is less than n.  
Almost all numbers are deficient; perfect and abundant numbers are the rare exceptions.

Examples:  
- Primes (2, 3  5  7  11…) → deficient (only divisor is 1)  
- 10 → 1+2+5 = 8 < 10 → deficient  
- 12 → 1+2+3+4+6 = 16 > 12 → abundant (not deficient = False)

This implementation uses an efficient O(√n) divisor search — much faster than checking up to n-1.

## Features
- Fast O(√n) algorithm by checking divisors only up to √n  
- Correctly pairs divisors (adds both i and n/i when different)  
- Special handling for n = 1 (which is considered deficient)  
- Includes diverse test cases: primes, powers of 2, perfect numbers (6, 28 not included), abundant numbers (12), and larger values  
- Measures average runtime over 1 million calls and exact step count  

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
.
├── deficient.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python deficient.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Harshad Number Checker – is_harshad(n)

A lightweight, pure-Python function that checks whether a positive integer n is a **Harshad number** (also known as a Niven number) — that is, n is divisible by the sum of its own digits.

Examples:  
- 18 → 1+8 = 9, 18 ÷ 9 = 2 → True  
- 111 → 1+1+1 = 3, 111 ÷ 3 = 37 → True  
- 2002 → 2+0+0+2 = 4, 2002 ÷ 4 = 500.5 → False  
- 99909 → 9+9+9+0+9 = 36, 99909 ÷ 36 = 2775.25 → False

Harshad numbers are fun, abundant, and appear in many recreational math problems!

## Features
- Converts number to string to easily extract digits  
- Computes sum of digits and checks divisibility  
- Works with arbitrarily large integers (thanks to Python)  
- Extremely fast — string conversion + loop is negligible  
- Includes classic test cases (including large and near-Harshad numbers)  
- Measures average runtime over 1 million calls and exact step count

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
.
├── harshad.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python harshad.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Automorphic Number Checker – is_automorphic(n)

A lightweight, pure-Python function that checks whether a positive integer n is **automorphic** — meaning that n² ends with the digits of n itself.

Famous examples:  
- 5² = 25 → ends with 5  
- 6² = 36 → ends with 6  
- 25² = 625 → ends with 25  
- 76² = 5776 → ends with 76  
- 376² = 141376 → ends with 376  

These numbers are rare and beautiful — only two exist for each number of digits in base 10 (except for 0 and 1).

## Features
- Computes n² and checks if the last digits match n  
- Works by converting both numbers to strings for easy suffix comparison  
- Handles arbitrarily large automorphic numbers (Python handles big integers flawlessly)  
- Includes known automorphic numbers: 0, 1, 5, 6, 25, 76, 376, 625, 9376, etc.  
- Measures average runtime and exact step count — blazing fast even for huge n  

## Requirements
- Python 3.x  
- No external dependencies (pure Python)

## Project Structure
.
├── automorphic.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python automorphic.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Pronic Number Checker – is_pronic(n)

A lightweight, pure-Python function that checks whether a non-negative integer n is **pronic** (also called oblong or heteromecic) — that is, n is the product of two consecutive integers:  
n = k × (k+1) for some integer k ≥ 0.

Examples:  
- 0 = 0×1 → True  
- 2 = 1×2 → True  
- 6 = 2×3 → True  
- 12 = 3×4 → True  
- 20 = 4×5 → True  
- 21 = not consecutive → False  

Pronic numbers form the sequence: 0, 2, 6, 12, 20, 30, 42, 56, 72, 90, …

## Features
- Efficient O(√n) algorithm — only checks divisors up to √n  
- Correctly identifies n by checking if any factor i has i+1 or i-1 as the paired factor  
- Handles edge cases: n=0 (True), n=1 (False)  
- Includes comprehensive test suite with known pronic and non-pronic numbers  
- Measures average runtime over 1 million calls and exact step count  
- Pure Python — no dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── pronic.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python pronic.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Prime Factors – prime_factors(n)

A lightweight, pure-Python function that returns the list of **prime factors** of a given positive integer n.  
This implementation uses trial division and checks primality of each divisor — perfect for learning the fundamentals of factorization.

Examples:  
- prime_factors(100) → [2, 2, 5, 5]  
- prime_factors(17) → [17]  
- prime_factors(20) → [2, 2, 5]  
- prime_factors(1) → [] (no prime factors)

Note: This version returns **all prime factors with multiplicity** (not unique primes).

## Features
- Finds all prime factors by testing divisibility from 2 to n  
- Uses naive primality testing on candidate divisors  
- Returns factors in ascending order with duplicates (e.g., 100 → [2,2,5,5])  
- Includes comprehensive test cases from small numbers to 1000  
- Measures average runtime over 1 million calls and exact step count  
- Pure Python — no dependencies, fully educational

## Requirements
- Python 3.x  
- No external dependencies

**Performance Note:** This O(n²) approach is slow for large n. For real-world use, prefer optimized trial division up to √n with repeated division.

## Project Structure
.
├── prime_factors.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python prime_factors.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Distinct Prime Factors Counter – distinct_prime_factors(n)

A lightweight, pure-Python function that returns the number of **unique (distinct) prime factors** of a positive integer n — also known as ω(n) in number theory.

Examples:  
- distinct_prime_factors(100) → 2 (only 2 and 5)  
- distinct_prime_factors(30) → 3 (2, 3, 5)  
- distinct_prime_factors(17) → 1 (prime)  
- distinct_prime_factors(1) → 0 (no prime factors)

This is the count of **different** primes — not including multiplicity (unlike Ω(n)).

## Features
- Efficient O(√n) trial division with repeated division to remove all instances of each prime  
- Eliminates duplicate factors automatically  
- Works flawlessly with large numbers and primes  
- Includes memory usage tracking via `tracemalloc`  
- Measures runtime over 1 million calls and exact step count  
- Pure Python — no external dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── distinct_prime_factors.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python distinct_prime_factors.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Prime Power Checker – is_prime_power(n)

A lightweight, pure-Python function that checks whether a positive integer n is a **prime power** — that is, can be expressed as p^k where p is a prime and k ≥ 1.

Examples:  
- 4 = 2² → True  
- 8 = 2³ → True  
- 9 = 3² → True  
- 25 = 5² → True  
- 27 = 3³ → True  
- 121 = 11² → True  
- 1331 = 11³ → True  
- 10, 50, 100 → False (multiple prime factors)

Prime powers include all primes (p¹) and perfect powers like squares, cubes, etc., of primes.

## Features
- Generates all primes up to n using trial division  
- For each prime p, checks if p^k = n for some k ≥ 2  
- Handles edge cases: 0, 1, and negative numbers appropriately  
- Includes extensive test cases with known prime powers  
- Measures runtime over 1 million calls, peak memory usage, and step count  
- Pure Python — no external dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── prime_power.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python prime_power.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Mersenne Prime Checker – is_mersenne_prime(p)

A lightweight, pure-Python function that checks whether **2ᵖ − 1** is a prime number, given that `p` is a prime — i.e., whether it is a **Mersenne prime**.

Mersenne primes are of the form **2ᵖ − 1** where p is prime.  
Examples:  
- p = 2 → 2²−1 = 3 → prime  
- p = 3 → 2³−1 = 7 → prime  
- p = 5 → 2⁵−1 = 31 → prime  
- p = 7 → 2⁷−1 = 127 → prime  
- p = 11 → 2¹¹−1 = 2047 = 23×89 → **not prime**

These are among the largest known primes and play a key role in cryptography, GIMPS (Great Internet Mersenne Prime Search), and number theory.

## Features
- Computes M = 2ᵖ − 1 directly (Python handles huge integers effortlessly)  
- Uses simple trial division up to M/2 to test primality  
- Includes classic test cases (p = 2, 3, 5, 7, 13, 17, 19…)  
- Measures runtime over 1 million calls, memory usage, and step count  
- Pure Python — no external dependencies

**Note:** This implementation is **educational**. Real-world Mersenne prime testing uses the **Lucas-Lehmer test** (much faster and deterministic for Mersenne numbers). This version becomes slow for p > 30.

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── mersenne_prime.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python mersenne_prime.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Twin Primes Generator – twin_primes(limit)

A lightweight, pure-Python function that finds all **twin prime pairs** (p, p+2) where both numbers are prime, up to a given limit `n`.

Twin primes are one of the most fascinating open problems in mathematics — it is unknown whether there are infinitely many!

Examples:  
- (3,5), (5,7), (11,13), (17,19), (29,31), (41,43), …

## Features
- Generates all primes up to `n` using trial division  
- Scans the prime list to find consecutive primes differing by exactly 2  
- Returns a clean list of tuples: `[(3,5), (5,7), (11,13), …]`  
- Includes comprehensive testing up to 100  
- Measures runtime over 1 million calls, peak memory usage, and total execution steps  
- Pure Python — no dependencies, great for learning

**Note:** This implementation is educational. For large limits, use the Sieve of Eratosthenes for speed.

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── twin_primes.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python twin_primes.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Number of Divisors – count_divisors(n)

A lightweight, pure-Python function that returns **d(n)** (also written τ(n) or σ₀(n)) — the total number of positive divisors of a given integer n.

Examples:  
- count_divisors(1) → 1  
- count_divisors(6) → 4 (1, 2, 3, 6)  
- count_divisors(28) → 6 (1, 2, 4, 7, 14, 28)  
- count_divisors(100) → 9 (1, 2, 4, 5, 10, 20, 25, 50, 100)

This is a fundamental arithmetic function used in number theory, perfect numbers, and highly composite number studies.

## Features
- Efficient O(√n) algorithm — checks divisors only up to √n  
- Correctly handles perfect squares (adds only one divisor when i × i = n)  
- Works instantly even for very large numbers  
- Includes memory tracking and step counting  
- Measures runtime over 1 million calls  
- Pure Python — no dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── count_divisors.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python count_divisors.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Aliquot Sum – aliquot_sum(n)

A lightweight, pure-Python function that computes the **aliquot sum** of a positive integer n — the sum of all **proper divisors** of n (i.e., all positive divisors excluding n itself).

This is denoted **s(n) = σ(n) − n**, where σ(n) is the sum of all divisors.

Used to classify numbers as:
- **Perfect** → s(n) = n (e.g., 6, 28)  
- **Deficient** → s(n) < n (most numbers)  
- **Abundant** → s(n) > n (e.g., 12, 18, 20)

## Features
- Efficient O(√n) divisor search  
- Correctly handles perfect squares by adding the square root only once  
- Builds list of proper divisors and returns their sum  
- Special handling for n = 1 → s(1) = 0 (no proper divisors)  
- Includes memory tracking, runtime over 1 million calls, and step counting  
- Pure Python — no external dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── aliquot_sum.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python aliquot_sum.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Amicable Numbers Checker – are_amicable(a, b)

A lightweight, pure-Python function that checks whether two positive integers **a** and **b** form an **amicable pair** — one of the most beautiful concepts in number theory.

Two numbers are **amicable** if:  
- The sum of the proper divisors of a equals b  
- The sum of the proper divisors of b equals a  
- And a ≠ b

The most famous pair: **220 and 284**  
- Proper divisors of 220 → 1+2+4+5+10+11+20+22+44+55+110 = **284**  
- Proper divisors of 284 → 1+2+4+71+142 = **220**

## Features
- Efficient O(√n) divisor search for both numbers  
- Handles perfect squares correctly (adds square root only once)  
- Returns `True` only if both conditions are satisfied and a ≠ b  
- Includes runtime over 1 million calls, memory usage, and step counting  
- Pure Python — no external dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── amicable.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python amicable.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Multiplicative Persistence – multiplicative_persistence(n)

A lightweight, pure-Python function that calculates the **multiplicative persistence** of a positive integer — the number of times you must multiply its digits together until you reach a single-digit number.

Examples:  
- 987 → 9×8×7 = 504 → 5×0×4 = 0 → **2 steps**  
- 1234 → 1×2×3×4 = 24 → 2×4 = 8 → **2 steps**  
- 9876 → 9×8×7×6 = 3024 → 3×0×2×4 = 0 → **2 steps**  
- 10 → 1×0 = 0 → **1 step**  
- 5 → already single digit → **0 steps**

The maximum known persistence is **11** — achieved by numbers like 277777788888899!

## Features
- Elegant recursive implementation — clean and intuitive  
- Works instantly even with extremely large integers (Python handles big ints)  
- Handles single-digit numbers correctly (returns 0)  
- Includes memory usage tracking, runtime over 1 million calls, and detailed step counting  
- Pure Python — no external dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── multiplicative_persistence.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python multiplicative_persistence.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Highly Composite Number Checker – is_highly_composite(n)

A lightweight, pure-Python function that checks whether a positive integer `n` is **highly composite** — meaning it has **more positive divisors** than **any smaller positive integer**.

Highly composite numbers (HCNs) were introduced by Ramanujan and form a fascinating sequence:  
1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, …

They are the "most divisible" numbers — crucial in understanding divisor functions and superior highly composite numbers.

## Features
- Computes the number of divisors d(n) using O(√n) method  
- Checks **every** number from 1 to n−1 to ensure none has more divisors than n  
- Correctly handles perfect squares  
- Includes runtime (over 10k calls), memory usage, and detailed step counting  
- Pure Python — no external dependencies


## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── highly_composite.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python highly_composite.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Modular Exponentiation – mod_exp(base, exponent, modulus)

A lightweight, pure-Python function that computes **(baseᵉˣᵖᵒⁿᵉⁿᵗ) mod modulus** — the cornerstone of modern cryptography and efficient large-number arithmetic.

This implementation uses Python’s built-in **fast modular exponentiation** (via the `**` operator with three arguments), which internally uses binary exponentiation — O(log exponent) time.

Examples:  
- `mod_exp(2, 100, 1000)` → 2¹⁰⁰ mod 1000  
- `mod_exp(7, 13, 100)` → 7¹³ mod 100 = 43  
- `mod_exp(5, 0, 10)` → 5⁰ = 1 mod 10 = 1

Used everywhere: RSA, Diffie-Hellman, ElGamal, digital signatures, primality testing, and more.

## Features
- Extremely fast — uses Python’s optimized C implementation of binary exponentiation  
- Handles arbitrarily large numbers (thanks to Python’s big integers)  
- Correctly handles edge cases: exponent = 0 → 1, modulus = 1 → 0  
- Includes runtime over 1 million calls, memory usage, and step counting  
- Pure Python — no external dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── mod_exp.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python mod_exp.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Modular Multiplicative Inverse – mod_inverse(a, m)

A pure-Python function that computes the **modular multiplicative inverse** of `a` modulo `m` — i.e., finds an integer `x` such that:

> **a × x ≡ 1 (mod m)**

This exists **only if** `gcd(a, m) = 1`.

This version uses a **brute-force search** over `k` in the equation `x = (k·m + 1) / a`, checking when `x` is an integer.

## Features
- Attempts to solve `a × x ≡ 1 (mod m)` by testing `x = (k·m + 1)/a`  
- Includes basic GCD check using trial division  
- Handles edge cases: `a=0`, `m=0`, `a=m`  
- Returns `None` when no inverse exists  
- Includes full testing, runtime (over 1M calls), memory usage, and step counting  
- Pure Python — no dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── mod_inverse.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python mod_inverse.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Chinese Remainder Theorem Solver – crt(remainders, moduli)

A pure-Python implementation of the **Chinese Remainder Theorem (CRT)** that solves a system of simultaneous congruences:
x ≡ r₁ (mod m₁)
x ≡ r₂ (mod m₂)
...
x ≡ rₖ (mod mₖ)
Returns the **unique solution modulo M = m₁×m₂×…×mₖ**, provided the moduli are **pairwise coprime** (or at least their overall gcd is 1).

This is one of the most powerful and ancient theorems in number theory — used in cryptography, calendar calculations, hashing, and fast arithmetic.

## Features
- Full manual implementation of the constructive CRT algorithm  
- Computes M = ∏mᵢ, then Mᵢ = M/mᵢ, then finds modular inverse of Mᵢ modulo mᵢ  
- Checks that a solution exists (by testing pairwise coprimality via common divisors)  
- Returns `None` if no solution exists  
- Includes comprehensive test cases, runtime, memory usage, and detailed step counting  
- Pure Python — no dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── crt.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python crt.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Quadratic Residue Check – is_quadratic_residue(a, p)

A lightweight, pure-Python function that determines whether a given integer **a** is a **quadratic residue** modulo **p** — that is, whether there exists an integer **x** such that:

> **x² ≡ a (mod p)**

This implementation uses **Euler’s Criterion**:  
a is a quadratic residue modulo an odd prime p if and only if **a^((p-1)/2) ≡ 1 (mod p)**

It is **extremely fast**, elegant, and widely used in cryptography and number theory.

## Features
- Uses Python’s built-in `pow(a, exp, mod)` for fast modular exponentiation  
- Correctly handles special cases:  
  - `a = 0` → True (x=0 is a solution)  
  - `m = 0` → None (invalid modulus)  
- Works instantly even with very large primes (e.g., p = 5003)  
- Includes comprehensive test cases covering small and large values  
- Measures average runtime (often under 1 microsecond), memory usage, and step count  
- Pure Python — no external dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── quadratic_residue.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python quadratic_residue.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Multiplicative Order – order_mod(a, n)

A pure-Python function that computes the **multiplicative order** of `a` modulo `n` — the smallest positive integer `k` such that:

> **aᵏ ≡ 1 (mod n)**

This is one of the most important concepts in **group theory**, **cryptography**, and **number theory**.

The order exists **only if** `gcd(a, n) = 1` (i.e., a and n are coprime).

### Also known as:
- The **order of a modulo n**
- `ordₙ(a)`
- The period of a in modular arithmetic

---

## Features
- Checks that `gcd(a, n) = 1` using trial division (required condition)  
- Returns `None` if no order exists (not coprime or `n ≤ 1`)  
- Uses `pow(a, k, n)` for fast modular exponentiation  
- Brute-force search for smallest `k` — correct and educational  
- Includes rich test cases with known orders  
- Measures runtime, memory, and exact step count  
- Pure Python — no dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── order_mod.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python order_mod.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Fibonacci Prime Checker – is_fibonacci_prime(n)

A lightweight, pure-Python function that checks whether a positive integer `n` is both a **Fibonacci number** and a **prime number** — i.e., a **Fibonacci prime**.

Fibonacci primes are extremely rare and beautiful numbers that appear in both the Fibonacci sequence and the sequence of primes.

Known Fibonacci primes:  
2, 3, 5, 13, 89, 233, 1597, 28657, 514229, …

It is unknown whether there are infinitely many!

## Features
- Generates Fibonacci numbers on-the-fly until exceeding `n`  
- Checks if `n` is in the Fibonacci sequence  
- Uses simple trial division to test primality (correct for educational use)  
- Returns `True` only if `n` is both Fibonacci and prime  
- Includes comprehensive test cases  
- Measures runtime over 1 million calls, memory usage, and step counting  
- Pure Python — no dependencies

**Note**: The primality test is O(n) — fine for learning, but slow for large n.  
For real use, use probabilistic tests like Miller-Rabin.

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── fibonacci_prime.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python fibonacci_prime.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Lucas Numbers Generator – lucas_sequence(n)

A lightweight, pure-Python function that generates the first **n** terms of the **Lucas sequence** — a close cousin of the Fibonacci sequence, defined by:
L₀ = 2,  L₁ = 1,  Lₙ = Lₙ₋₁ + Lₙ₋₂ for n ≥ 2
First few terms:  
2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, …

Lucas numbers appear in geometry (tiling, golden ratio), number theory, and even in approximations of π!

## Features
- Simple iterative generation — clean and efficient  
- Returns a list of the first `n` Lucas numbers  
- Handles edge cases: `n = 0`, `n = 1`, `n = 2` correctly  
- Includes comprehensive testing up to 20 terms  
- Measures average runtime over 1 million calls, memory usage, and step counting  
- Pure Python — no external dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── lucas_sequence.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python lucas_sequence.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Perfect Power Checker – is_perfect_power(n)

A lightweight, pure-Python function that determines whether a positive integer `n` is a **perfect power** — that is, can be expressed as:

> **n = aᵇ** where **a > 1** and **b > 1** are integers

Examples of perfect powers:  
- 4 = 2²  
- 8 = 2³  
- 9 = 3²  
- 16 = 4² = 2⁴  
- 27 = 3³  
- 81 = 3⁴ = 9²  
- 1 = 1ᵇ (for any b) → usually considered **True**

Non-examples: 2, 3, 5, 6, 7, 10, 11, …

Perfect powers are surprisingly sparse — only about **√n** of them up to n!

## Features
- Brute-force search over base `a` from 2 up  
- For each base, increases exponent `b` until `aᵇ > n`  
- Special handling for `n = 1` → **True**  
- Handles large exponents efficiently using Python’s arbitrary-precision integers  
- Includes comprehensive test cases  
- Measures runtime over 1 million calls, memory usage  
- Pure Python — no dependencies

**Note**: This method is **correct** but slow for very large `n` due to O(√n log n) behavior.  
Faster methods exist using binary search per exponent.

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── perfect_power.py
├── README.txt
└── statement.txt
## How to Run
Save the code to a file and run:

```bash
python perfect_power.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Polygonal Numbers – polygonal_number(s, n)

A **lightweight, ultra-fast** pure-Python function that computes the **n-th s-gonal (polygonal) number** using the closed-form formula:

> **P(s, n) = ((s−2)·n·(n−1))/2 + n**  
> or equivalently: **P(s, n) = n·((s−2)·n − (s−4))/2**

This generalizes:
- Triangular numbers → s = 3  
- Square numbers → s = 4  
- Pentagonal → s = 5  
- Hexagonal → s = 6  
- … up to any s ≥ 3

implementation uses a beautifully simplified form:
```python
(s-2)*n*(n+1)//2 - (s-3)*n
Features

Direct O(1) computation — no loops, no recursion
Handles edge cases: s < 3 → None, n < 0 → None
Uses integer arithmetic (//) for exact results
Works instantly even for astronomically large n and s
Includes comprehensive test cases (triangular, square, large inputs, invalid cases)
Measures runtime (sub-microsecond!), memory, and exact step count
Pure Python — zero dependencies

Requirements

Python 3.x
No external dependencies

Project Structure
├── polygonal_number.py
├── README.txt
└── statement.txt
How to Run
Save the code and run:
Bashpython polygonal_number.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Polygonal Numbers – polygonal_number(s, n)

A **blazing-fast**, pure-Python function that returns the **n-th s-gonal (polygonal) number** using the elegant closed-form formula:

> **P(s, n) = ((s−2)·n·(n−1))/2 + n**  
> `(s-2)*n*(n+1)//2 - (s-3)*n` — mathematically equivalent and beautiful!

This single line generates:
- **Triangular numbers** (s=3): 1, 3, 6, 10, 15, …  
- **Square numbers** (s=4): 1, 4, 9, 16, 25, …  
- **Pentagonal** (s=5), **Hexagonal** (s=6), **Heptagonal**, … up to any polygon!

## Features
- **O(1) time** — direct arithmetic, no loops  
- Exact integer results using `//` (floor division)  
- Input validation: returns `None` if `s < 3` or `n < 0`  
- Works with **arbitrarily large** `s` and `n` (thanks to Python’s big integers)  
- Includes full testing suite with edge cases and huge inputs  
- Measures runtime (~0.3 microseconds), memory, and step count  
- **Pure Python** — zero dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── polygonal_number.py
├── README.txt
└── statement.txt
## How to Run
Save the code and run:

```bash
python polygonal_number.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Carmichael Number Checker – is_carmichael(n)

A pure-Python function that checks whether a positive integer `n` is a **Carmichael number** — the most deceptive composite numbers in all of mathematics.

### Definition
A **Carmichael number** is a **composite** number `n` that passes the **Fermat primality test** for **every** base `a` coprime to `n`:

> **aⁿ⁻¹ ≡ 1 (mod n)** for all `a` with `gcd(a,n)=1`

They are **"fake primes"** — pseudoprimes to **all** coprime bases!

The smallest (and most famous) is **561 = 3×11×17**

## Features
- Checks Fermat’s Little Theorem condition for **all** `a` coprime to `n`  
- Uses `pow(a, n-1, n)` for fast modular exponentiation  
- Manual GCD check via trial division  
- Returns `False` for primes, 1, and non-Carmichael composites  
- Includes all known small Carmichael numbers in testing  
- Measures runtime, memory, and exact step count  
- **Pure Python** — no dependencies

**Note**: This implementation is **correct** but **slow** for large `n` due to testing every `a`.  
Real detection uses Korselt’s criterion (much faster).

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── carmichael.py
├── README.txt
└── statement.txt
## How to Run
Save and run:

```bash
python carmichael.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Miller-Rabin Primality Test – is_prime_miller_rabin(n, k)

A **fast, probabilistic** primality test in pure Python — one of the most powerful tools in modern number theory and cryptography.

The **Miller-Rabin test** is the **gold standard** for quickly checking whether a large number is prime, used in:
- RSA key generation
- Cryptographic libraries (OpenSSL, Java, etc.)
- Finding large primes in seconds

The implementation follows the classic algorithm with **k witness bases** (starting from `a = 2`) and correctly detects strong pseudoprimes.

## Features
- Deterministic for small `n`, probabilistic for large  
- Uses `pow(base, exp, mod)` — Python’s ultra-fast modular exponentiation  
- Correctly writes `n−1 = d·2ˢ`  
- Checks both `x ≡ 1` and `x ≡ −1 (mod n)` conditions  
- Returns `False` immediately on composite witness  
- Includes strong test cases:  
  - `341` = 11×31 (famous pseudoprime to base 2)  
  - `561` = first Carmichael number  
  - `2047` = 23×89 (Mersenne composite)  
- Full performance profiling: runtime, memory, step counting  
- **Pure Python** — zero dependencies

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── miller_rabin.py
├── README.txt
└── statement.txt
# How to Run
Save and run:

```bash
python miller_rabin.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Pollard's Rho Algorithm – pollard_rho(n)

A **beautiful, fast, and legendary** integer factorization method in pure Python — **Pollard's Rho algorithm** — one of the most elegant and effective tools in computational number theory.

The implementation finds a **non-trivial factor** of a composite number `n` using the famous "rho" (ρ) cycle detection method — inspired by birthday paradoxes and Floyd's tortoise and hare!

This algorithm **crushed** the idea that factoring large numbers must be slow.

Used in:
- Factoring RSA keys (when poorly chosen)
- Cryptanalysis
- Number theory libraries (GMP, PARI/GP)
- Breaking challenges in CTFs and Project Euler

## Features
- Pure Python implementation of the classic **Pollard Rho**  
- Uses polynomial `f(x) = x² + c mod n`  
- Floyd’s cycle detection (`x` = tortoise, `y` = hare)  
- Smart GCD computation on differences  
- Recurses with `c += 1` if cycle found (handles bad polynomials)  
- Handles powers of 2 and small primes  
- Includes comprehensive test cases  
- Full performance profiling: runtime, memory, step counting  
- **No external dependencies**

## Requirements
- Python 3.x  
- No dependencies

## Project Structure
.
├── pollard_rho.py
├── README.txt
└── statement.txt
## How to Run
Save and run:

```bash
python pollard_rho.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Riemann Zeta Function Approximation – zeta_approx(s, terms)

A **clean, elegant, and mathematically pure** implementation of the **Riemann zeta function** approximation using the defining Dirichlet series:

> **ζ(s) ≈ Σ (from n=1 to terms) 1/nˢ**

This is the **most famous function in analytic number theory** — the heart of the **Riemann Hypothesis**, one of the seven **Millennium Prize Problems** worth **$1,000,000**.

the function computes the partial sum of the series — the simplest and most direct way to approximate ζ(s) for **Re(s) > 1**.

## Features
- Pure Python, direct summation  
- Works for any real `s > 1` (convergence region)  
- Returns `None` for `s ≤ 1` (where the series diverges)  
- Uses `i**(-s)` — clean and expressive  
- Includes comprehensive test cases:  
  - `ζ(2)` → π²/6 ≈ 1.64493…  
  - `ζ(4)` → π⁴/90 ≈ 1.08232…  
  - `ζ(3)` → Apéry’s constant (irrational!)  
- Full performance profiling: runtime, memory, step counting  
- **Zero dependencies**

## Requirements
- Python 3.x  
- No external dependencies

## Project Structure
.
├── zeta_approx.py
├── README.txt
└── statement.txt
## How to Run
Save and run:

```bash
python zeta_approx.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Partition Function – partition_function(n)

A **beautiful, elegant, and mathematically perfect** implementation of the **integer partition function** p(n) — one of the crown jewels of **combinatorics** and **number theory**.

The recursive function counts the number of ways to write **n** as a sum of positive integers (order doesn't matter):

> **p(n) = number of partitions of n**

Examples:  
- p(4) = 5 → 4, 3+1, 2+2, 2+1+1, 1+1+1+1  
- p(5) = 7  
- p(10) = 42  
- p(50) = 204226

This function grows **faster than exponential** — and is connected to modular forms, q-series, and Ramanujan's famous congruences!

## Features
- **Pure dynamic-programming-style recursion** with two constraints:  
  - `slots`: remaining parts allowed  
  - `maximum`: largest part allowed (enforces non-increasing order)  
- Avoids duplicate partitions by enforcing **non-increasing** order  
- Base cases:  
  - `n == 0` → 1 way (empty partition)  
  - `slots == 0` → 0 ways (can't fill)  
- **Mathematically flawless** — this is the standard recursive definition  
- Includes full OEIS sequence test up to n=50  
- Performance profiling: runtime, memory, step counting  
- **Zero dependencies**

## Requirements
- Python 3.x  
- No dependencies

## Project Structure
.
├── partition_function.py
├── README.txt
└── statement.txt
## How to Run
```bash
python partition_function.py
_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________



