# Tên file: PTB16_TungLam_CP2.py

# Danh sách (list / array):
# CRUD: Create - Read - Update - Delete

# Create - Khởi tạo danh sách
    # Tạo danh sách rỗng
arr = []
    # Tạo danh sách có sẵn
arrHS = ['Tùng Lâm', 'Đức Hiếu', 'Duy Phú', 'Xuân Hùng']
arrNum = [1, 2, 3, 4, 5, 6]

    # len() - trả về kích thước / độ dài của danh sách
# print(len(arrHS))
# print(len(arrNum))
# print(len(arr))

# Read - Duyệt phần tử danh sách
    # Hiện phần tử bằng chỉ số index
# print(arrHS[0])
    # Hiện phần tử cuối cùng: index = -1
# print(arrHS[-1])

    # Duyệt danh sách (quan trọng):
        # Cách 1: lấy cả index và value
# for i in range(len(arrHS)):
#     print(f'[{i}] {arrHS[i]}')

        # Cách 2: chỉ lấy value
# for item in arrHS:
#     print(item)

    # Hiện toàn bộ danh sách
# print(arrHS)

# Update - Chỉnh sửa phần tử danh sách
    # Thêm phần tử vào cuối danh sách - append(value)
arrHS.append('Đức Trung')
    # Thêm phần tử vào vị trí chỉ định - insert(index, value)
arrHS.insert(1, 'Gojo Satoru')
    # Chỉnh sửa phần tử bằng index
arrHS[1] = 'hihi'

# Delete - Xóa phần tử trong danh sách
    # Xóa phần tử bằng index - pop(index)
arrHS.pop(-1)
    # Xóa phần tử bằng value - remove(value)
arrHS.remove('hihi')
    # Xóa toàn bộ phần tử danh sách - clear()
arrHS.clear()

# Sắp xếp phần tử danh sách - sort()
num_list = [0, 9, 5, 1, 8, 4, 6, 7, 3, 2]
    # Theo thứ tự từ nhỏ đến lớn - sort()
num_list.sort()
    # Theo thứ tự từ lớn đến nhỏ - sort(reverse=True)
num_list.sort(reverse=True)
