#  Hàm không có giá trị trả về
def say_hello():
    print("Hello Tùng Lâm")
# Gọi hàm khi cần sử dụng
# say_hello()

# Hàm có tham số truyền vào
def say_hello2(name):
    print(f"Xin chào {name}")
# say_hello2('Đức Trung')
# say_hello2('Tùng Lâm không làm BTVN')

# Hàm có giá trị trả về
def dtich_HCN(a, b):
    return a * b
# print('Diện tích HCN:', dtich_HCN(5,3))

# Bài 1: Viết một hàm sum_odd(numbers) để tính tổng các số lẻ trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về tổng các số lẻ trong danh sách đó.
def sum_odd(numbers):
    sum = 0
    for item in numbers:
        if item % 2 != 0:
            sum = sum + item
    return sum
num_list = [1, 2, 3, 4, 5]
print('Tổng các số lẻ trong danh sách:', sum_odd(num_list))

# Bài 2: Viết một hàm is_prime(n) để kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về True nếu n là số nguyên tố, ngược lại trả về False.
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 2: return True
    else: return False
num = 6
print(f'{num} là số nguyên tố:', is_prime(num))

# Bài 3: Viết một hàm count_words(s) để đếm số lượng từ trong một chuỗi s.
# 	YC1: Hàm nhận vào một chuỗi ký tự s.
# 	YC2: Hàm trả về số lượng từ trong chuỗi đó.
def count_words(s):
    # strip(): xóa khoảng trắng ở đầu và cuối
    # split(): tách các phần tử khi gặp khoảng trắng
    words = s.strip().split()
    # len() - trả về số lượng phần tử của danh sách
    return len(words)
name = 'Tùng Lâm đẹp trai siêu cấp vippro'
print('Số lượng từ trong chuỗi:', count_words(name))

# Bài 4: Viết một hàm sum_of_digits(n) để tính tổng các chữ số của một số nguyên dương n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	YC2: Hàm trả về tổng các chữ số của n.
def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10
    return sum
num = 1234
print(f'Tổng các chữ số của {num} là:', sum_of_digits(num))

# Bài 5: Viết một hàm find_max(numbers) để tìm vị trí số lớn nhất trong một danh sách numbers.
# 	YC1: Hàm nhận vào một danh sách các số nguyên.
# 	YC2: Hàm trả về vị trí số lớn nhất trong danh sách đó.
numbers = [1, 2, 3, 4, 5, -3, 9, -2, 6]
def find_max(numbers):
    # Tìm giá trị phần tử lớn nhất trong danh sách
    max_value = max(numbers)
    # Duyệt danh sách để tìm vị trí
    for i in range(len(numbers)):
        if numbers[i] == max_value:
            return i
print('Vị trí phần tử lớn nhất trong danh sách:', find_max(numbers))

# Bài 6: Viết một hàm sum_to_n(n) để tính tổng các số từ 1 đến n.
# 	YC1: Hàm nhận vào một số nguyên dương n.
# 	Yc2: Hàm trả về tổng các số từ 1 đến n.
def sum_to_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum
num = 5
print(f'Tổng từ 1 đến {num} là:', sum_to_n(num))
