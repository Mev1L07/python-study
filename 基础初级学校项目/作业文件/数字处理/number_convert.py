def binary_to_decimal(binary_str):
    """二进制转十进制"""
    value = binary_str.strip()
    if not value or any(digit not in "01" for digit in value):
        raise ValueError("无效的二进制数，只能包含 0 和 1")
    return int(value, 2)

def binary_to_hex(binary_str):
    """二进制转十六进制"""
    decimal = binary_to_decimal(binary_str)
    return decimal_to_hex(decimal)

def decimal_to_binary(decimal_num):
    """十进制转二进制"""
    if decimal_num < 0:
        raise ValueError("请输入非负整数")
    return bin(decimal_num)[2:]

def decimal_to_hex(decimal_num):
    """十进制转十六进制"""
    if decimal_num < 0:
        raise ValueError("请输入非负整数")
    return hex(decimal_num)[2:].upper()

def hex_to_decimal(hex_str):
    """十六进制转十进制"""
    value = hex_str.strip()
    if value.lower().startswith("0x"):
        value = value[2:]
    if not value or any(digit not in "0123456789abcdefABCDEF" for digit in value):
        raise ValueError("无效的十六进制数，只能包含 0-9 和 A-F")
    return int(value, 16)

def hex_to_binary(hex_str):
    """十六进制转二进制"""
    decimal = hex_to_decimal(hex_str)
    return decimal_to_binary(decimal)

def display_menu():
    """显示菜单"""
    print("\n" + "=" * 40)
    print("        进制转换器")
    print("=" * 40)
    print("1. 二进制 -> 十进制")
    print("2. 二进制 -> 十六进制")
    print("3. 十进制 -> 二进制")
    print("4. 十进制 -> 十六进制")
    print("5. 十六进制 -> 十进制")
    print("6. 十六进制 -> 二进制")
    print("0. 退出")
    print("="*40)

def main():
    while True:
        display_menu()
        choice = input("请输入选项 (0-6): ").strip()

        if choice == "0":
            print("感谢使用，再见！")
            break

        if choice not in {"1", "2", "3", "4", "5", "6"}:
            print("无效选项，请重新输入")
            continue

        try:
            if choice == "1":
                value = input("请输入二进制数: ").strip()
                result = binary_to_decimal(value)
                print(f"二进制 {value} -> 十进制: {result}")

            elif choice == "2":
                value = input("请输入二进制数: ").strip()
                result = binary_to_hex(value)
                print(f"二进制 {value} -> 十六进制: {result}")

            elif choice == "3":
                value = input("请输入十进制数: ").strip()
                decimal = int(value)
                result = decimal_to_binary(decimal)
                print(f"十进制 {value} -> 二进制: {result}")

            elif choice == "4":
                value = input("请输入十进制数: ").strip()
                decimal = int(value)
                result = decimal_to_hex(decimal)
                print(f"十进制 {value} -> 十六进制: {result}")

            elif choice == "5":
                value = input("请输入十六进制数: ").strip()
                result = hex_to_decimal(value)
                print(f"十六进制 {value} -> 十进制: {result}")

            elif choice == "6":
                value = input("请输入十六进制数: ").strip()
                result = hex_to_binary(value)
                print(f"十六进制 {value} -> 二进制: {result}")

        except ValueError as error:
            print(f"错误：{error}")

if __name__ == "__main__":
    main()
