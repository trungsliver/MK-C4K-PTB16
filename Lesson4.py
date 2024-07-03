# Chữa BTVN
# Bài 4: Quy đổi thời gian
# 1p = 60s, 1h = 3600s
# 3661s = 1h 1p 1s
# time = int(input('Nhập thời gian (giây): '))
# h = time // 3600
# m = (time % 3600) // 60
# s = time % 60
# print(f'{time}s = {h}h {m}m {s}s')

# Câu điều kiện
    # Dạng thiếu
# age = int(input('Hãy nhập tuổi của bạn: '))
# if age >= 18:
#     print('Bạn đã đủ 18 tuổi')

    # Dạng đủ
# number = int(input('Hãy nhập 1 số nguyên: '))
# if number % 2 == 0:
#     print('Đây là số chẵn')
# else:
#     print('Đây là số lẻ')

    # Dạng đa nhánh
        # 8-10: Giỏi, 6.5-8: Khá, 5-6.5: Trung Bình, 0-5: Yếu
point = float(input('Hãy nhập điểm của bạn: '))

if 0 <= point <= 10:
    if 8 <= point <= 10:
        print('Xếp loại: Giỏi')
    elif 6.5 <= point < 8:
        print('Xếp loại: Khá')
    elif 5 <= point < 6.5:
        print('Xếp loại: Trung Bình')
    else:
        print('Xếp loại: Yếu')
else:
    print('Bạn đã nhập sai')