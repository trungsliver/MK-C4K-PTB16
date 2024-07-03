# Biến số - Phép gán
    # Biến số: dùng để lưu dữ liệu, có thể thay đổi trong khi lập trình
    # Phép gán: [Tên biến] = [Giá trị]
x = 10
a, b, c = 5, 6, 7

# Data Types - Kiểu dữ liệu
    # String - Chuỗi ký tự / Xâu ký tự
name = 'Bui Duc Trung'
    # Int - số nguyên (không có phần thập phân)
age = 25
    # Float - số thực (có phần thập phân)
score = 1.5
    # Bool / Boolean: True/False - Đúng/Sai
male = True

# Quy tắc đặt tên biến
    # Chỉ bao gồm chữ, số 0-9, ký tự gạch dưới
    # Không được bắt đầu bằng số
    # Phân biệt chữ hoa và chữ thường
    # Không được trùng từ khóa

    # Ví dụ đúng: lam, lam123, lam_cute123, _lam123
    # Ví dụ sai: 123Lam, lam 123, print, lam$$$

# Cách kiểm tra kiểu dữ liệu - type()
# print(type(name), type(age), type(score), type(male))

# Xác định kiểu dữ liệu khi nhập từ bàn phím
# name2 = str(input('Nhập tên của bạn: '))
# age2 = int(input('Nhập tuổi của bạn: '))
# score2 = float(input('Hãy nhập điểm của bạn: '))
# male2 = bool(input('Bạn có phải là nam không: '))
# print(type(name2), type(age2), type(score2), type(male2))

# Ôn tập 4 cách print()
    # Cách 1: Dùng dấu cộng (nối chuỗi, áp dụng khi data type = string)
# print('Họ tên: ' + name2)
    # Cách 2: Dùng dấu phẩy (không phân biệt data type, dữ liệu cách nhau 1 khoảng trắng)
# print('Tuổi:', age2)
    # Cách 3: Dùng f trước dấu nháy (truyền dữ liệu vào string thông qua ngoặc nhọn {})
# print(f'Điểm: {score2}')

# Chuyển đổi các kiểu dữ liệu
x = '123'
y = int(x)

# Các phép toán: 
    # Cộng trừ nhân chia (+ - * /)
    # Chia lấy dư (%)
    # Chia lấy nguyên (//)
    # Lũy thừa (**)

# Bài tập: Nhập chiều dài, chiều rộng từ bàn phím. 
# Tính chu vi, diện tích HCN và hiện ra màn hình.
a = float(input('Nhập chiều dài HCN: '))
b = float(input('Nhập chiều rộng HCN: '))

chuvi = (a + b) * 2
dientich = a * b

print('Chu vi HCN là:', chuvi)
print('Diện tích HCN là:', dientich)

