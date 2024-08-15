# Bài tập: Nhập 1 số nguyên n từ bàn phím.
    # Yêu cầu: Kiểm tra xem n có phải là số nguyên tố hay không?
    # Biết rằng: số nguyên tố là số chỉ chia hết cho 1 và chính nó
# n = int(input('Nhập 1 số nguyên n: '))
# count = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print(n, 'là số nguyên tố')
# else:
#     print(n, 'không phải số nguyên tố')

# Bài 2: Hãy in ra các số nguyên tố trong khoảng [10,30]
# for n in range(10,31):
#     count = 0
#     for i in range(1, n+1):
#         if n%i == 0:
#             count = count + 1
#     if count == 2:
#         print(n, end = ' ')

# Bài 3: Hãy in ra các số nguyên tố trong khoảng [50,100]
# for n in range(50,101):
#     count = 0
#     for i in range(1, n+1):
#         if n%i == 0:
#             count = count + 1
#     if count == 2:
#         print(n, end = ' ')

# ========== Luyện tập ==========
# Câu 1: Nhập một số từ bàn phím và in ra số đó.
# n = int(input('Hãy nhập 1 số: '))
# print('Đó là số:', n)

# Câu 2: Viết chương trình kiểm tra nhập vào 1 số và kiểm tra số đó là chẵn hay lẻ.
# n = int(input('Hãy nhập 1 số nguyên: '))
# if n%2==0:
#     print('Đây là số chẵn')
# else:
#     print('Đây là số lẻ')

# Câu 3: Viết chương trình tính tổng, hiệu, tích, thương của hai số nhập từ bàn phím.
# a = float(input('Nhập a: '))
# b = float(input('Nhập b: '))
# print('Tổng =', a+b)
# print('Hiệu =', a-b)
# print('tích =', a*b)
# print('Thương =', a/b)

# Câu 4: Viết chương trình nhập vào 1 số và kiểm tra số đó có phải số nguyên tố hay không.
# n = int(input('Nhập 1 số nguyên: '))
# count = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print(n, 'là số nguyên tố')
# else:
#     print(n, 'không phải số nguyên tố')

# Câu 5: Viết chương trình chuyển đổi từ USD sang VND (số tiền được nhập từ bàn phím).
usd = float(input('Nhập số tiền cần đổi: '))
vnd = usd * 25000
print('Số tiền sau chuyển đổi:', int(vnd))