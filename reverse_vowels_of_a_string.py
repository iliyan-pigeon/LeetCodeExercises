def reverseVowels(s: str) -> str:
    vowels_list = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    current_vowels = []
    for i in range(len(s)):
        if s[i] in vowels_list:
            current_vowels.append(s[i])

    for i in range(len(s)):
        if s[i] in vowels_list:
            s = s[:i] + current_vowels.pop() + s[i+1:]
    return s


print(reverseVowels("IceCreAm"))
