# break and continue keyword

# 1 to 10 print
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# print 1 to 10 , but not 5
for i in range(1,11):
    if i == 5:
        continue
    print(i)