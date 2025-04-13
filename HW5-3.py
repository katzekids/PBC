# ===================================================
# 座位分配函数
# 根据乘客偏好尝试分配座位
# 参数:
#   current_sales: 当前座位分配状态
#   c_id: 乘客ID
#   c_pref: 乘客座位偏好 (0:无偏好, 1:靠窗, 2:靠走道)
#   s_start: 起始站
#   s_end: 终点站
# 返回:
#   success: 是否分配成功
#   assigned_seat: 分配的座位号
def try_to_sell(current_sales, c_id, c_pref, s_start, s_end):
    # Initialize the return value: success and assigned_seat
    success = False
    assigned_seat = 0  # Set assigned_seat to 0 as default

    # assign a seat to the customer based on the preference
    if c_pref == 0:  # 無偏好
        for i in range(seat_cnt):
            no_seat = False
            for j in range(s_start, s_end):  # 檢查是否有空座位
                if current_sales[i][j-1] != "--":
                    no_seat = True
            if not no_seat:  # 若有空座位則訂票成功
                success = True
                assigned_seat = i + 1
                break
        if no_seat:  # 若無空座位則返回訂票失敗
            return success, assigned_seat
    elif c_pref == 1:  # 奇數 靠窗
        for i in range(0, seat_cnt, 2):  # 檢查奇數排是否有空座位
            no_seat = False
            for j in range(s_start, s_end):
                if current_sales[i][j-1] != "--":
                    no_seat = True
            if not no_seat:  # 若有空座位則訂票成功
                success = True
                assigned_seat = i + 1
                break
    else:  # 偶數 靠走道
        for i in range(1, seat_cnt, 2):  # 檢查偶數排是否有空座位
            no_seat = False
            for j in range(s_start, s_end):
                if current_sales[i][j-1] != "--":
                    no_seat = True
            if not no_seat:
                success = True
                assigned_seat = i + 1
                break
    if no_seat:  # 若無法照其偏好排座位則檢查是否有任意座位可坐
        re = try_to_sell(current_sales, c_id, 0, s_start, s_end)
        success = re[0]
        assigned_seat = re[1]
    # do something
    # DO NOT modify the values in current_sales
    # return the result
    return success, assigned_seat
# ===================================================


# ===================================================
# 输入模块
# 处理用户输入并解析乘客信息

# 分別記錄座位數、路段、乘客數
first_line = list(map(int, input().split(',')))
seat_cnt = int(first_line[0])  # Number of seats
segment_cnt = int(first_line[1])  # Number of segments
passenger_cnt = int(first_line[2])  # Number of passengers

preference = ["preference", "window", "aisle"]  # 可能的偏好 無偏好記為0 靠窗記為1 靠走道記為2
names = []  # 乘客名稱
passengers = []  # 乘客欲搭乘路段及偏好
for _ in range(passenger_cnt):
    request = input()
    name, rest = request.split("from")  # 以from為分隔，區分名字和其他
    names.append(name)  # 乘客名稱
    start, end_prefer = rest.split("to")  # 以to為分隔，區分起點及其他
    start = start.strip()  # 起點
    end_prefer = end_prefer.split()  # 以空白為分隔，區分起點及偏好
    for i in range(len(start)):
        if not start[i].isnumeric():  # 擷取數字部分
            s_start = int(start[0:i])  # 紀錄起點位置
            break
    for i in range(len(end_prefer[0])):
        if not end_prefer[0][i].isnumeric():  # 擷取數字部分
            s_end = int(end_prefer[0][0:i])  # 紀錄終點位置
            break
    for i in range(len(preference)):
        if preference[i] in end_prefer[2]:  # 確認乘客偏好
            c_pref = i  # 記錄偏好
    passengers.append([s_start, s_end, c_pref])  # 紀錄旅客資訊
# ===================================================


# ===================================================
# 计算模块
# 初始化座位分配状态并处理每个乘客的请求

# Initialize the seat allocation map
# current_sales[i][j] represents whether seat i+1 is occupied at segment j+1
# -- means the seat is available, non-zero means the seat is occupied by a passenger ID
current_sales = []
for _ in range(seat_cnt):
    one_seat = ["--"] * segment_cnt
    current_sales.append(one_seat)

passenger_name = str()
start = []
end = []
seat = []
# Process each passenger's request
for i in range(passenger_cnt):
    s_start, s_end, c_pref = passengers[i]
    # Try to assign a seat to the passenger
    success, assigned_seat = try_to_sell(current_sales, i + 1, c_pref, s_start, s_end)
    if success:
        # Update the seat allocation map
        for station in range(s_start - 1, s_end - 1):
            current_sales[assigned_seat - 1][station] = names[i][0].upper() * 2  # Assign the passenger initials to the seat
        # 將登記成功的旅客紀錄
        passenger_name += names[i][0].upper()
        start.append(s_start)
        end.append(s_end)
        seat.append(assigned_seat)
# ===================================================


# ===================================================
# 重复处理模块
# 为重复的乘客姓名缩写添加编号
for i in range(len(passenger_name)):
    order = 1  # 旅客編號從1開始
    if passenger_name.count(passenger_name[i]) > 1:  # 若縮寫重複出現多次
        indx = passenger_name.find(passenger_name[i])  # 找出是第幾位登記的乘客
        for j in range(passenger_name.count(passenger_name[i])):
            for k in range(start[indx] - 1, end[indx] - 1):
                current_sales[seat[indx] - 1][k] = passenger_name[indx] + str(order)  # 將名字縮寫加上編號
            indx = passenger_name.find(passenger_name[i], indx + 1)  # 找出下一個縮寫重複的乘客
            order += 1  # 編號+1
# ===================================================


# ===================================================
# 输出模块
# 打印最终的座位分配状态

# Print the seat allocation map
for i in current_sales:
    # Iterate through each segment in the seat
    for j in range(len(i)):
        # Print the segment's status
        print(i[j], end='')  # Print the number without newline
        # Print a semicolon if between initials and --
        if j < len(i) - 1 and ((i[j] != "--" and not i[j + 1] != "--") or (not i[j] != "--" and i[j + 1] != "--")):
            print(';', end='')
        # Print a comma if it's not the last segment
        elif j < len(i) - 1:
            print(",", end="")
    print()  # Print a newline after each seat
# ===================================================