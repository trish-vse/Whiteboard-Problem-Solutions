# Trishitha Dharmavaram
# 10-12-2025
# FizzBuzz problem with Bazz for multiples of 7.

def fizzBuzzModulus(n):
    result = []
    for i in range(1, n+1):
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        if i % 7 == 0:
            s += 'Bazz'
        if s == '':
            s = str(i)
        result.append(s)
    return result

def fizzBuzzDict(n):
    result = []
    rules = {3: 'Fizz', 5: 'Buzz', 7: 'Bazz'}
    for i in range(1, n+1):
        s = ''
        for k, v in rules.items():
            if i % k == 0:
                s += v
        if s == '':
            s = str(i)
        result.append(s)
    return result

def main():
    n = int(input("Enter a number: "))
    print("FizzBuzz Modulus:", fizzBuzzModulus(n))
    print("FizzBuzz Dict:", fizzBuzzDict(n))

if __name__ == "__main__":
    main()