def first_unique_character(s):
    if not s:
        return -1

    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1


if __name__ == "__main__":
    s = input()
    print(first_unique_character(s))
