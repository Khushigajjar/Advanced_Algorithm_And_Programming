def is_balaced_symbols(s:str) -> tuple[bool, int]:
    stack = []
    comparisons = 0
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        comparisons += 1
        if char in "({[":
            stack.append(char)
        else:
            comparisons += 1
            if not stack:
                return False, comparisons
            top = stack.pop()

            comparisons += 1
            if pairs[char] != top:
                return False, comparisons
            
    comparisons += 1
    return len(stack) == 0, comparisons

if __name__ == "__main__":
    comparisons = 0
    input_string = input("Enter a string of symbols: ")
    balanced, total_comparisons = is_balaced_symbols(input_string)
    print(f"Balanced: {balanced}, Comparisons: {total_comparisons}")