# Câu lệnh hiện dữ liệu ra màn hình - print()
# print('Bui Duc Trung')
# print('Tuổi: 2')

# Khai báo biến - Declare variables
    # Biến số là nơi để lưu trữ dữ liệu, có thể thay đổi trong khi lập trình
name = 'Bui Duc Trung'
age = 25
weight = 62.5

# Các cách hiển thị dữ liệu
    # Cách 1: phép cộng
print('Họ tên: ' + name)
print('Tuổi: ' + str(age))
print('Cân nặng: ' + str(weight))

    # Cách 2: dùng dấu phẩy
print('Họ tên:', name)
print('Tuổi:', age)
print('Cân nặng:', weight)

    # Cách 3: Áp dụng khi muốn hiện nhiều biến số trên 1 dòng
print(f'Họ tên: {name}. Tuổi: {age}. Cân nặng: {weight}')

    # Cách 4: In trên nhiều dòng
print("""
*
**
***
****
*****
******
""")

# Nhập dữ liệu - Input()
food = input('Bạn muốn ăn gì: ')

# Phép toán
print(5*6)
