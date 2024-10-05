# # Cấu trúc của xâu / chuỗi ký tự
# name = 'Tung Lam'

# # len() - độ dài / số ký tự của string
# print(len(name))

# # Ký tự thứ 6 của string
# print(name[6])      

# # Duyệt ký tự của string
#     # Cách 1:
# for i in range(len(name)):
#     print(name[i], end=' ')
#     # Cách 2:
# print('\n Cách 2')
# for item in name:
#     print(item, end=' ')

# # Xâu con:
# str1 = 'tunglamdeptrai'
# str2 = 'tunglam'
# str3 = 'xautrai'
#     # Kiểm tra xâu con: hàm in() => True/False
# print(str2 in str1)
# print(str3 in str1)
#     # Tìm vị trí xuất hiện của xâu con: hàm find()
# print(str1.find(str2))          # vị trí = 0
# print(str1.find('deptrai'))     # vị trí = 7
# print(str1.find(str3))          # vị trí = -1

# # Slicing - cắt chuỗi
# print(str1[4:10])   # cắt từ vị trí 4-10
# print(str1[:7])     # cắt từ đầu chuỗi đến 7
# print(str1[7:])     # cắt từ vị trí 4 đến cuối chuỗi

# # strip() - xóa khoảng trắng ở đầu và cuối chuỗi
# str4 = '   lam cute   '
# str4 = str4.strip()
# print(str4 * 3)

# # replace() - thay thế
# str1 = 'tunglamdeptrai'
# str2 = str1.replace('deptrai', 'manhme')
# print(str2)
#     # Thay thế nhiều giá trị
# song = 'baby shark doo doo doo doo doo'
# song2 = song.replace('doo', 'tunglam')
# song3 = song.replace('doo', 'tunglam', 2)
# print(song2)
# print(song3)

# # join() - kết hợp
# arr = ['r','o','n','a','l','d','o']
# print(' '.join(arr))

# # split() - tách chuỗi
# a = '1 2 3 4 5 6 7 8 9'
# b = 'a,s,d,f,g,h,j,k,l'
# arr1 = a.split()
# print(arr1)
# arr2 = b.split(',')
# print(arr2)

# Chuyển đổi kiểu dữ liệu trong sách
a = '1 2 3 4 5 6 7 8 9'
arr1 = a.split()
print(arr1)
    # Cách 1:
arr2 = []
for item in arr1:
    arr2.append(int(item))
print(arr2)
    # Cách 2:
arr3 = [int(item) for item in arr1]
print(arr3)

# Tính tổng phần tử danh sách
    # Cách cũ
tong = 0
for item in arr2:
    tong = tong + item
print(tong)
        # Cách mới
tong = sum(item for item in arr2)
print(tong)

# Tính tổng phần tử chẵn trong danh sách
        # Cách cũ:
tong = 0
for item in arr2:
    if item%2 == 0:
        tong = tong + item

        # Cách mới
tong = sum(item for item in arr2 if item%2==0)

print('Tổng phần tử chẵn:', tong)

#     # Đếm phần tử chẵn trong danh sách
count = sum(1 for item in arr2 if item%2==0)
print('số lượng phần tử chẵn:', count)

# -------------------------Luyện tập-----------------------
# Bài 1: Nhập 2 thông tin: họ, tên. In ra màn hình tên đầy đủ

# Bài 2: Nhập vào 1 xâu ký tự định dạng dd/mm/yyyy (01/08/2024)
    # Tách ngày, tháng, năm và hiển thị ra màn hình

# Bài 3: Nhập vào thông tin dạng username:password
    # kiểm tra xem thông tin vừa nhập có trùng với thông tin có sẵn
    # YC2: bắt người dùng nhập đến khi nào trùng username và password thì kết thúc
    