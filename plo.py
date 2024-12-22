import random
import string

# ฟังก์ชันสำหรับสร้างรหัส
def generate_code(length, count):
    characters = string.ascii_letters + string.digits + string.punctuation  # A-Z, 0-9, และตัวอักษรพิเศษ
    codes = []
    for _ in range(count):
        codes.append(''.join(random.choices(characters, k=length)))
    return codes

# ฟังก์ชันสำหรับสร้างรหัสแบบสุ่มความยาว
def generate_code_auto(max_length, count):
    characters = string.ascii_letters + string.digits + string.punctuation
    codes = []
    for _ in range(count):
        random_length = random.randint(1, max_length)  # สุ่มความยาว 1 ถึง max_length
        codes.append(''.join(random.choices(characters, k=random_length)))
    return codes

# รับค่าจากผู้ใช้
def main():
    print("=== โปรแกรมสร้างรหัส ===")
    print("1. โหมดกำหนดเอง (Manual Mode)")
    print("2. โหมดสร้างอัตโนมัติ (Auto Generate Mode)")
    mode = int(input("เลือกโหมด (1 หรือ 2): "))

    if mode == 1:  # โหมดกำหนดเอง
        length = int(input("กรุณาใส่ความยาวของรหัส (เช่น 16): "))
        count = int(input("กรุณาใส่จำนวนรหัสที่ต้องการสร้าง (เช่น 1000): "))
        codes = generate_code(length, count)
    elif mode == 2:  # โหมดสร้างอัตโนมัติ
        max_length = int(input("กรุณาใส่ความยาวสูงสุดของรหัส (เช่น 100): "))
        count = int(input("กรุณาใส่จำนวนรหัสที่ต้องการสร้าง (เช่น 1000): "))
        codes = generate_code_auto(max_length, count)
    else:
        print("เลือกโหมดไม่ถูกต้อง!")
        return

    # บันทึกลงไฟล์แบบต่อท้าย
    save_option = input("ต้องการบันทึกลงไฟล์? (y/n): ").lower()
    if save_option == 'y':
        filename = input("กรุณาใส่ชื่อไฟล์ (เช่น codes.txt): ")
        with open(filename, 'a') as file:  # ใช้โหมด 'a' เพื่อเขียนต่อท้าย
            for code in codes:
                file.write(code + '\n')
        print(f"รหัสทั้งหมดถูกเขียนเพิ่มในไฟล์ {filename}")
    else:
        print("\nรหัสที่สร้าง:")
        for code in codes:
            print(code)

if __name__ == "__main__":
    main()
