f = open(r"e:\dataset_3363_2.txt")
s = f.readline().strip()
s = s + 'a'
print(s)
d = []
a = []
a_ch = []
s1_new = []
res_pr = ''
for i in range(len(s)):
    if s[i].isalpha():
        a.append(i)
        a_ch.append(s[i])
    else:
        d.append(i)
for i in range(len(a)-1):
    s1 = s[a[i]+1:a[i+1]]
    s1_new.append(s1)
print(s1_new)
for i in range(len(s1_new)):
    res = int(s1_new[i]) * a_ch[i]
    res_pr = res_pr +res
print(res_pr)
f_out = open("e:\\test1.txt", "w")
f_out.write(res_pr)
f_out.close()

