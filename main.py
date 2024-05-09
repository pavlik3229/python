
n = int(input())

strings = [ input() for i in range(n)]

nums = []
anton = "anton"

string2 = ''
for string in strings:
    flag = True
    string1 = string
    for c in string:
        if c not in anton:
            string1 = string1.replace(c, '')
        string2 = string1
    if len(string2) < len(anton):
        continue
    for i in range(len(anton)):
        for j in range(len(string1)):
            for g in range(len(anton)):
                if string2[g] != anton[g]:
                    string2 = string2[0:g] + string2[g + 1:]
                    break
                if string2[:5] == anton:
                    flag = False
                    string2 = string2[:5]
                    break
            if not flag:
                break
        if not flag:
            break

    if string2 == anton:
        nums.append(strings.index(string) + 1)
print(*nums)
