def longestCommonPrefix(strs: list[str]):
    result = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]
    
    return result

print(longestCommonPrefix(["road", "roar", "roam"]))