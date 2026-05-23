# Bài 2
# Nhập số nguyên N
N = int(input("Nhập N (0 < N < 50): "))

while N <= 0 or N >= 50:
    N = int(input("Nhập lại N (0 < N < 50): "))

# Nhập list gồm N số thực
a = []

for i in range(N):
    x = float(input(f"Nhập phần tử thứ {i + 1}: "))
    a.append(x)

print("List đã nhập:", a)

# Tìm số lớn nhất và nhỏ nhất
print("Số lớn nhất:", max(a))
print("Số nhỏ nhất:", min(a))

# Tìm số dương chẵn lớn nhất
duong_chan = [i for i in a if i > 0 and i % 2 == 0]

if len(duong_chan) > 0:
    print("Số dương chẵn lớn nhất:", max(duong_chan))
else:
    print("Không có số dương chẵn")

# Tìm số âm lẻ nhỏ nhất
am_le = [i for i in a if i < 0 and i % 2 != 0]

if len(am_le) > 0:
    print("Số âm lẻ nhỏ nhất:", min(am_le))
else:
    print("Không có số âm lẻ")

# Tính tổng list
tong = sum(a)
print("Tổng list:", tong)

# Trung bình cộng
tbc = tong / N
print("Trung bình cộng:", tbc)

# Tìm các số lớn hơn trung bình cộng
print("Các số lớn hơn trung bình cộng:")

for i in a:
    if i > tbc:
        print(i)

# Sắp xếp tăng dần
tang = sorted(a)
print("List tăng dần:", tang)

# Sắp xếp giảm dần
giam = sorted(a, reverse=True)
print("List giảm dần:", giam)