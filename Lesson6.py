# Vòng lặp hữu hạn - vòng lặp for
    # Hàm range(start, stop, step): lặp đến stop-1
            # start: số bắt đầu (không bắt buộc, mặc định = 0)
            # stop: số kết thúc (bắt buộc)
            # step: bước nhảy (không bắt buộc, mặc định = 1)
    # VD: bắt đầu = 0, kết thúc = 6-1 =5, khoảng cách = 2
# for i in range(0, 6, 2):
#     print(i)

# # VD1: range(stop):
# for i in range(10):     # for i in range(0,10,1):
#     print(i)

# # VD2: range(start, stop):
# for i in range(5,10):   # for i in range(5,10,1):
#     print(i)

# for i in range(1,5): in ra 1,2,3,4
# for i in range(4,15,2): in ra 4,6,8,10,12,14
# for i in range(4): in ra 0,1,2,3

# Bài 1: Nhập 2 số nguyên a và b từ bàn phím (a<b).
    # Yêu cầu: in ra màn hình các số nguyên trong khoảng [a, b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))

# for i in range(a, b+1):
#     print(i)

# Bài 2: Nhập 2 số nguyên a và b từ bàn phím (a<b).
    # Yêu cầu: Tính tổng các số nguyên trong khoảng [a, b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# sum = 0
# for i in range(a, b+1):
#     sum = sum + i
# print('Tổng các số:', sum)

# Bài 3: Nhập 2 số nguyên a và b từ bàn phím (a<b).
    # Yêu cầu: Tính tổng các số chẵn trong khoảng [a, b]
# a = int(input('Nhập a: '))
# b = int(input('Nhập b: '))
# sum = 0
# for i in range(a, b+1):
#     if i%2 == 0:
#         sum = sum +i
# print('Tổng các số:', sum)

# Bài 4: In ra bảng cửu chương 5
for i in range(1,11):
    print(f'5 * {i} = {5*i}')