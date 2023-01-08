# f = open('data/fruits.txt', 'r')

# for word in f:
#     if 'berry' in word:
#         print(word)

# f.close()


# list_words = []

# f = open('data/fruits.txt', 'r')
# list_words = f.read()

# data = list(set(list_words))
# cnt = 0

# for word in data:
#     if 'berry' in word:
#         cnt += 1
# print(cnt)

# for word in data:
#     if 'berry' in word:
#         print(word)

# ===================================

# r = open('data/fruits.txt', 'r')
# w = open('03.txt', 'w')

# # 파일에서 읽은 라인들을 리스트로 읽어들임
# lines = r.readlines()

# # set에 넣어서 중복 제거 후 다시 리스트 변환
# lines = list(set(lines))
# # 리스트 정렬
# lines.sort()

# cnt = 0
# for i in lines:
#     if i.find('berry') > 0:
#         cnt += 1
# result = str(cnt) + '\n'
# w.writelines(result)

# for j in lines:
#     if j.find('berry') > 0:
#         w.writelines(j)

# w.close()
# r.close()

# ===================================

# 답
fruit_list = []
fruit_count = 0

with open ('./data/fruits.txt', 'r') as f:
    fruits = f.readlines()
    for fruit in fruits:
        fruit = fruit.strip()
        if fruit[-5:] == 'berry':
            fruit_list.append(fruit)
            fruit_count += 1

with open('./03.txt', 'w') as f:
    print(fruit_count)
    f.write(str(fruit_count) + '\n')

    for fruit in fruit_list:
        print(fruit)
        f.write(fruit + '\n')