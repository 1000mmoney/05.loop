# n1 = 0
# while n1 < 100:
#     print(n)
#     n = 2**n1
#     for k in range(0, 100):
# #         print(k)
# #
# n = 0
# while n < 100:
#     print(n)
#     n = 1**n
#
#     result = []
#     for i in range(0, 100):
#         result.append(i)
#     print(result)
#
# n = 0
# n1 = 1
#
# result = []
# for i in  range(n1**(n+1),100):
#
#         print(i)
#
# n=0
# a=0
# b=0
#
# for i in range(1,100+1):
#     n+=i
#     if i%2==1:
#         a+=i
#     if i%2==0:
#         b+=i
#
# print(n)
# print(a)
# print(b)
#
# n = 1
# n1 = n+n
# for i in range(1, 100+1):
#     n = n+1
#     if n % 2 ==1:
#         n = n1

# # naver
# n=0
# a=0
#
# for i in range(1, 100+1):
#     n += i
#     if i % 2 == 1:
#         a += i
# print(a)


#교수님

# 1부터 100까지의 수를 반복 출력
# 변수 i의 역할 : 수열 만들기, 반복문 제어
i = 1
# result하는 역할 : 연산 결과 값을 저장
result = 0
while i < 100:
    i = i + 1

# 반복되는 수가 홀수 인지를 확인
    if i % 2 == 1:


# 홀수라면 그 값을 저장
        result = result + i
# 저장된 값들의 합을 구함

print(result)