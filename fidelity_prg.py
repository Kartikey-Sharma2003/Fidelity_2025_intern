data = 100
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact


def reverse_no(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num
print(reverse_no(123))

