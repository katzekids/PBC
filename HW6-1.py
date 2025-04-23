temp = input().split(",")
n = int(temp[0])
interval = int(temp[1])
a = {}
biggest = 0
for i in range(n):
    item = input().split(",")
    typpe = int(item[0])
    place = int(item[1]) // interval
    if typpe not in a:
        a[typpe] = [place]
    else:
        a[typpe].append(place)
target = int(input())
first = True
if target in a:
    for i in range(max(a[target])+1):
        counter = a[target].count(i)
        if first:
            print(counter, end="")
            first = False
        else:
            print("," + str(counter), end="")
else:
    print(0)