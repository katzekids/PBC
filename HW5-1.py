plpl = []
for _ in range(4):
    plpl.append(int(input()))
if plpl[1] == plpl[2] and plpl[0] in [8, 9] and plpl[3] in [8, 9]:
    print("ignore")
else:
    print("answer")

# 可疑词汇检测功能
trash = ["money", "cash", "urgent", "account", "transfer", "heritage", "price"]
sentence_cnt = int(input())
counter = 0
for i in range(sentence_cnt):
    string = input()
    for word in trash:
        idx = string.find(word)
        if idx != -1:
            # 检查前一个字符
            prev_char_valid = idx == 0 or not string[idx - 1].isalpha()
            # 检查后一个字符
            next_char_valid = idx + len(word) >= len(string) or not string[idx + len(word)].isalpha()
            if prev_char_valid and next_char_valid:
                counter += 1
print(f"发现的可疑词汇数量: {counter}")
