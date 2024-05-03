
# 2920 음계 

a= list(map(int, input().split()))

ascending = 0
descending = 0
for i in range(1, 8): 
    if a[i] > a[i-1]: 
        ascending += 1
    elif a[i] < a[i-1]:
        descending += 1

if ascending == 7: 
    print("ascending")
elif descending == 7: 
    print("descending")
else: 
    print("mixed")
