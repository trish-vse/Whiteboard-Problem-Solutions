# Trishitha Dharmavaram
# 10-12-2025
# Check if a string is a palindrome iteratively and recursively.

def isPalindromeIterative(s):
    return s == s[::-1]

def isPalindromeRecursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindromeRecursive(s[1:-1])

def main():
    s = input("Enter a string: ")
    print("Iterative:", isPalindromeIterative(s))
    print("Recursive:", isPalindromeRecursive(s))

if __name__ == "__main__":
    main()
