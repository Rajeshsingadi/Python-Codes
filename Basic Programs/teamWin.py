N = int(input())
l1 = input()
l2 = input()
l3 = input()
res = ""
i = 0
while i < N:
    if l1[i] == '#':
        i += 1
    else:
        s = ""
        s = s.join(l1[i:i+3])
        if s == '.':
            res += 'U*'
        elif s == '.*.':
            res += 'A*'
        elif s == '*':
            t = ""
            t = t.join(l2[i:i+3])
            if t == '.':
                res += 'O*'
            elif t == '**.':
                res += 'E*'
            elif t == '.*.':
                res += 'I*'
        i += 3
ans = list(res)
ans.pop()
res = ""
res = res.join(ans)
print(res)