def interger_mirror(n:int) -> int:
    if n == 0:
        return 0
    
    reversed_number = 0

    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n = n // 10

    return reversed_number

if __name__ == "__main__":
    num = int(input("Enter an integer: "))
    result = interger_mirror(num)
    print(f"The mirror of {num} is: {result}")
