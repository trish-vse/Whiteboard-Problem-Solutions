# Trishitha Dharmavaram
# 10-12-2025
# Reverses a string using both iterative and recursive methods.

def reverseIterative(s):
    return ''.join(reversed(s))

def reverseRecursive(s):
    if len(s) == 0:
        return s
    return reverseRecursive(s[1:]) + s[0]

def main():
    s = input("Enter a string to reverse: ")
    print("reverseIterative:", reverseIterative(s))
    print("reverseRecursive:", reverseRecursive(s))

if __name__ == "__main__":
    main()