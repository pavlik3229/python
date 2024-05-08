

n = int(input())

strings = [ input() for i in range(n)]

nums = []
anton = "anton"
flag = False

for string in strings:
    string1 = string
    for c in string:
        if c not in anton:
            string1 = string1.replace(c, '')
        string2 = string1
    for i in range(len(string1)):
        for j in range(len(anton)):
            if string1[j] != anton[j]:
                string2 = string2[i + 1:]
            continue
    if string2 == anton:
        nums.append(strings.index(string))
print(*nums)


