# my_list = [100, 200, 400, 800, 1000, 1300]
# for b in my_list:
#     a = sum(int(b))
#     print(int(a))

my_list = [100, 200, 400, 800, 1000, 1300]
result = 0
for i in my_list:
    result = result + i
avg = result / len(my_list)
print(avg)