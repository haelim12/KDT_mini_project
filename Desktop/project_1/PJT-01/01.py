# f = open('01.txt', 'w', encoding = 'UTF-8')
# f.write('Hello, Python!')

# for i in range(2,7):
#     f.write(f'{i}일차 파이썬 공부 중')
# f.close()

# f = open('01.txt', 'w', encoding = 'UTF-8')

# f.writelines('\n'.join(['Hello, Python!', 
# '1일차 파이썬 공부 중', 
# '2일차 파이썬 공부 중',
# '3일차 파이썬 공부 중',
# '4일차 파이썬 공부 중',
# '5일차 파이썬 공부 중']))

# f.close()

# ===================================

# 답
string_list = [
    'Hello, Python!',
    '1일차 파이썬 공부 중',
    '2일차 파이썬 공부 중',
    '3일차 파이썬 공부 중',
    '4일차 파이썬 공부 중',
    '5일차 파이썬 공부 중',
]

with open('./01.txt', 'w', encoding = 'UTF-8') as f:
    for string in string_list:
        f.write(string + '\n')
