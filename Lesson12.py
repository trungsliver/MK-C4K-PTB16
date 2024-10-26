# HÀM - CHƯƠNG TRÌNH CON

# Hàm không không có giá trị trả về
    # Tự định nghĩa 1 hàm/chương trình con
def hello():
    print('Xin chào Tùng Lâm đẹp trai')
    print('Xin chào Đức Trung')

    # Gọi tên chương trình khi cần sử dụng
# hello()

# Bài 1: Viết hàm nhập 1 số nguyên dương n
# Yêu cầu: Tính tổng các số chẵn trong khoảng từ 1 đến n
def sum_even():
    n = int(input('Nhập số nguyên n: '))
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum = sum + i
    print('Tổng ccas số chẵn là:', sum)

# sum_even()

# Truyền dữ liệu cho hàm
def hello2(name):
    print('Xin chào', name)

# hello2('Huy Hiếu')
# hello2('Hoàng Lâm')

# Bài tập: Đăng ký - Đăng nhập
users = ['admin:admin']
# 1. Đăng ký
    # Yêu cầu: không để trống thông tin, tên tài khoản chưa có trong danh sách users
def register():
    # Nhập thông tin 
    username = input('Nhập tên tài khoản: ')
    password = input('Nhập mật khẩu: ')

    check = True    # Để kiểm tra đăng ký 

    # Dùng strip() để xóa khoảng trắng ở đầu và cuối
    username = username.strip()
    password = password.strip()

    # Kiểm tra thông tin
    # Không được để trông username hoặc password
    if username == '' or password == '':
        check = False       # Tạo tài khoản không thành công
        print('Không được để trống thông tin')
    else:
        # Duyệt danh sách users
        for user in users:
            # Chia 1 user thành 2 phần: username, password
            stored_username, stored_password = user.split(':', 1)
            # Kiểm tra trùng username
            if username == stored_username:
                check = False       # Tạo tài khoản không thành công
                print('Tài khoản đã tồn tại!')

    # Kiểm tra xem có đăng ký thành công không
    if check == True:
        print('Đăng ký thành công!')
        # Thêm tài khoản vào danh sách users
        new_acc = username + ':' + password
        users.append(new_acc)
    else:
        print('Đăng ký không thành công!')

# Đăng nhập
def login():
     # Nhập thông tin 
    username = input('Nhập tên tài khoản: ')
    password = input('Nhập mật khẩu: ')

    check = False    # Để kiểm tra đăng ký 

    # Dùng strip() để xóa khoảng trắng ở đầu và cuối
    username = username.strip()
    password = password.strip()

    # Kiểm tra đăng nhập
    for user in users:
        stored_username, stored_password = user.split(':', 1)
        # Bắt buộc phải trùng cả username và password của 1 user trong danh sách
        if username == stored_username and password == stored_password:
            check = True

    # Kiểm tra đăng nhập thành công
    if check == True:
        print('Đăng nhập thành công')
    else:
        print('Đăng nhập không thành công')

register()
login()