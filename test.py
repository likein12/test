fiz_buz_list = []

while True:
    I = input().split(":")
    if len(I)==2:
        fiz_buz_list.append((int(I[0]),I[1]))
    elif len(I)==1:
        target = int(I[0])
        break

fiz_buz_list.sort(key = lambda x: x[0])

ans = []

for i,s in fiz_buz_list:
    if target%i==0:
        ans.append(s)

if len(ans)==0:
    print(target)
else:
    print("".join(ans))
    