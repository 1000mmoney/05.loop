import random

def lotto():

    lotto_list = list()

    while True:
        select_num = random.randint(1, 45)

        if select_num not in lotto_list:
            lotto_list.append(select_num)
        if len(lotto_list) == 6:
            lotto_list.sort()
            for i in lotto_list:
                print(str(i), end="")
            print(i)
            break
