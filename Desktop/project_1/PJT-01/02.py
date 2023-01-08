# r = open('data/fruits.txt', 'r')

# # print(f.read().count('\n'+1))
# # print(len(f.readlines()))
# w = open('02.txt', 'w')

# lines = r.readlines()

# result = str(len(lines))
# w.writelines(result)

# w.close()
# r.close()

# ===================================

# 답
count = 0

with open('data/fruits.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        count += 1

with open('./02.txt', 'w') as f:
    f.write(str(count))