set_evens = set()
set_odds = set()
set_multiples_3 = set()
set_primes = set()

N = 100

#even numbers 0-100
for number in range(2,N+1,2):
    set_evens.add(number)
print("Even numbers: ", set_evens)

#odd numbers 0-100
for number in range(0,N):
    if number % 2 != 0:
        set_odds.add(number)
print("Odd numbers: ", set_odds)

#pollaplasia tou 3 , 0-100
for number in range(3,N,3):
    set_multiples_3.add(number)
print("Multiples 3: ", set_multiples_3)

#What is a prime number in maths?
#A prime number is any positive number that can only be divided by itself and the number 1
#ta sinola twn prwtwn apo to 0 ews to 100

for number in range(2, N+1):  # ξεκινάμε από το 2
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        set_primes.add(number)

print("Prime numbers: ", set_primes)

set_even_or_multiple = set_evens | set_multiples_3
print("Even or Multiples3: ",set_even_or_multiple)

set_odd_and_prime = set_odds & set_primes
print("Odds and Prime: ",set_odd_and_prime)



