# John is trying to solve the arithmetic series(AP). He wants to find two things in the series
# 1. He wants to find nth terms in the series
# 2. He wants to find the sum up to the nth term.

a = float(input("Enter first number (a): "))
d  = float(input("Enter the common difference (d): "))
n = int(input("Enter the term number (n): "))

nth_term = a + (n-1) * d

sum_nth_terms = n/2 * (2 * a + (n-1)*d)

print(f"The {n}th term of the AP is: {nth_term}")
print(f"The sum of first {n} terms of the AP is: {sum_nth_terms}")