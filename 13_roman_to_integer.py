def romanToInt(s):
    roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    # if smaller value goes before the larger one - subtract
    # if smaller value goes after the larger one - add
    num = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_table[s[i]] < roman_table[s[i+1]]:
            num -= roman_table[s[i]]
        else:
            num += roman_table[s[i]]
    return num

print(romanToInt("CMXCVIII"))