# # 리스트, 딕셔너리 
# list_words = []
# dic_words={}

# # 파일에서 내용 읽어오기
# r = open('data/fruits.txt', 'r')
# w = open('04.txt', 'w')
# words = r.read()

# # 띄워쓰기로 나눈 단어 리스트로 넣기
# list_words = words.split('\n')

# # 단어들을 키-값으로 넣고 새로운 단어가 나오면 0 + 1로 세기
# for word in list_words:
#     dic_words[word] = dic_words.get(word, 0) + 1
#     keys = sorted(dic_words.keys())

# for word in keys:
    
#     w.write(word, str(dic_words[word]))

# ===================================

# # 리스트, 딕셔너리 
# list_words = []
# dic_words = {}

# # 파일에서 내용 읽어오기
# r = open('data/fruits.txt', 'r')
# w = open('04.txt', 'w')
# words = r.read()

# list_words = words.split(" ")

# # 단어들을 키-값으로 넣고 새로운 단어가 나오면 0 + 1로 세기
# for word in list_words:
#    dic_words[word] = dic_words.get(word, 0) + 1
#    keys = sorted(dic_words.keys())

# for word in keys:
#     w.writelines(word, str(dic_words[word]))

# ===================================

# w.close()
# r.close()

# with open('data/fruits.txt','r',encoding='UTF8') as f:
#     cnt = 0
#     berry = {}
#     for i in f:
#         if i in berry.keys():
#             berry[i] += 1
#         elif i not in berry.keys():
#             berry[i] = 1
#     for key, value in berry.items():
#             print(key, value)

# ===================================

# r = open('data/fruits.txt', 'r', encoding='UTF8')
# w = open('04.txt', 'w', encoding='UTF8')

# cnt = 0
# berry = {}
# for i in r:
#     if i in berry.keys():
#             berry[i] += 1
#     elif i not in berry.keys():
#             berry[i] = 1

# for key, value in berry.items():
#     w.writelines(key, value)

# r.close()
# w.close()

# ===================================

# 답
fruit_dict = {}

with open('./data/fruits.txt', 'r') as f:
    fruits = f.readlines
    for fruit in fruits:
        fruit = fruit.strip() # 공백제거

        if fruit not in fruit_dict:
            fruit_dict[fruit] = 1

        elif fruit in fruit_dict:
            fruit_dict[fruit] += 1

with open ('./04.txt', 'w') as f:
    for fruit, count in fruit_dict.items():
        print(fruit, count)
        f.write(f'{fruit} {count} \n')   
