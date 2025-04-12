trash = ["money", "cash", "urgent", "account", "transfer", "heritage", "prize"]
sentence_cnt = int(input())
new = []
for i in range(sentence_cnt):
    string = input()
    counter = 0
    for word in trash:
        idx = string.find(word)
        while idx != -1:
            prev_char_valid = idx == 0 or not string[idx - 1].isalpha()
            next_char_valid = idx + len(word) >= len(string) or not string[idx + len(word)].isalpha()
            if prev_char_valid and next_char_valid:
                counter += 1
            idx = string.find(word, idx + len(word))
    new.append(counter)
    
first = True
for i in range(len(new)):
    if first:
          print(new[i], end="")
          first = False
    else:
         print("," + str(new[i]), end="")