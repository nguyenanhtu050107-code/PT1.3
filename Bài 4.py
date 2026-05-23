# Nhập chuỗi a có độ dài từ 0 đến 50
a = input("Nhập chuỗi a: ")

while len(a) > 50:
    a = input("Nhập lại chuỗi a (tối đa 50 ký tự): ")

# Kiểm tra có ký số hay không
if any(i.isdigit() for i in a):
    print("Chuỗi có ký số")
else:
    print("Chuỗi không có ký số")

# Kiểm tra có ký tự in HOA hay không
if any(i.isupper() for i in a):
    print("Chuỗi có ký tự in HOA")
else:
    print("Chuỗi không có ký tự in HOA")

# Nhập ký tự ch và kiểm tra
ch = input("Nhập ký tự ch: ")

if ch in a:
    print("Có chứa ký tự", ch)
else:
    print("Không chứa ký tự", ch)

# Nhập chuỗi b và kiểm tra
b = input("Nhập chuỗi b: ")

if b in a:
    print("b nằm trong a")
else:
    print("b không nằm trong a")

if len(b) > len(a):
    print("b có độ dài lớn hơn a")
else:
    print("b không có độ dài lớn hơn a")

if b > a:
    print("b lớn hơn a")
else:
    print("b không lớn hơn a")

# Kiểm tra đối xứng
if a == a[::-1]:
    print("Chuỗi a đối xứng")
else:
    print("Chuỗi a không đối xứng")

# Đếm số từ
print("Số từ của chuỗi a là:", len(a.split()))

# Cắt dấu cách cuối chuỗi
print("Cắt space cuối:", a.rstrip())

# Cắt dấu cách đầu chuỗi
print("Cắt space đầu:", a.lstrip())

# Đảm bảo giữa 2 từ chỉ có 1 dấu cách
a1 = " ".join(a.split())
print("Chuỗi sau khi chuẩn hóa space:", a1)

# Tính trung bình ASCII
if len(a) > 0:
    tong = sum(ord(i) for i in a)
    print("Trung bình ASCII:", tong / len(a))
else:
    print("Chuỗi rỗng")

# Đếm số lần xuất hiện mỗi ký tự
for i in set(a):
    print(i, "xuất hiện", a.count(i), "lần")

# Chèn '\n' giữa ký tự thứ 4 và 5
if len(a) >= 5:
    a2 = a[:5] + "\n" + a[5:]
    print(a2)
else:
    print("Chuỗi không đủ độ dài để chèn \\n")

# Chèn '\t' giữa 2 ký tự in hoa liên tiếp
a3 = ""

for i in range(len(a) - 1):
    a3 += a[i]

    if a[i].isupper() and a[i + 1].isupper():
        a3 += "\t"

a3 += a[-1] if len(a) > 0 else ""

print(a3)


