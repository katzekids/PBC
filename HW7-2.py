import datetime
n = int(input())
temp_start = []
temp_end = []
dt_start = []
dt_end = []
for i in range(n):
    start, end = input().split(',')
    temp_start.append(datetime.datetime.strptime(start, "%Y/%m/%d %H:%M"))
    temp_end.append(datetime.datetime.strptime(end, "%Y/%m/%d %H:%M"))
    if not (temp_start[i] >= temp_end[i] or temp_start[i].date() != temp_end[i].date()):
        dt_start.append(temp_start[i])
        dt_end.append(temp_end[i])
if not dt_start:
    print(0)
else:
    overlap = 0
    earliest = min(dt_start)
    same_day_start = [x for x in dt_start if x.date() == earliest.date()]
    same_day_end = [x for x in dt_end if x.date() == earliest.date()]
    for i in range(len(same_day_start) - 1):
        for j in range(i + 1, len(same_day_start)):
            if not (same_day_end[i] <= same_day_start[j] or same_day_end[j] <= same_day_start[i]):
                overlap = 1
    print(f"{len(same_day_start)},{overlap}")