
import base64

encoded_string = "bGwtZ29vZGx1Y2t5"
encoded_string2 = "aHR0cHM6Ly9naXRodWIuY29tL2xsLWdvb2RsdWNreS8="
decoded_string = base64.b64decode(encoded_string).decode("utf-8")
decoded_string2 = base64.b64decode(encoded_string2).decode("utf-8")
print("程序作者：", decoded_string)
print("GIThub主页：", decoded_string2)
print()

file_path = "hex.txt"  # 文件路径

byte_objects = []  # 用于存储转换后的字节对象
original_texts = []  # 用于存储原始文本内容

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()  # 去除行尾的换行符
        original_texts.append(line)  # 保存原始文本内容
        line = line.replace("%", "").replace("0x", "").replace(",", "")  # 去除 "%"、"0x" 和 "," 字符
        hex_string = line  # 处理后的十六进制字符串
        byte_object = bytes.fromhex(hex_string)  # 将十六进制字符串转换为字节对象
        byte_objects.append(byte_object)

for byte_object, original_text in zip(byte_objects, original_texts):
    print("原始文本:", original_text)
    print("字节对象:", byte_object)

    # 将字节对象转换为二进制字符串
    binary_string = bin(int.from_bytes(byte_object, 'big')).lstrip('0b')

    print("二进制字符串:", binary_string)

    # 将二进制字符串每8个字符分组
    grouped_binary = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    # 按照Unicode编码方式，进行重新排列
    processed_binary = []
    for i, group in enumerate(grouped_binary):
        if (i + 1) % 3 == 1:
            processed_binary.append(group[4:])
        elif (i + 1) % 3 == 2:
            processed_binary.append(group[2:])
        else:
            processed_binary.append(group[2:])

    remaining_binary = ''.join(processed_binary)
    remaining_grouped_binary = [remaining_binary[i:i+8] for i in range(0, len(remaining_binary), 8)]

    print("重组后的二进制:", remaining_grouped_binary)

    # 将每组二进制转换为十六进制字符串，并去掉前缀 "0x"
    hex_strings = [hex(int(binary, 2))[2:] for binary in remaining_grouped_binary]

    # 去掉十六进制字符串中的前缀 "0x"，并组合在一起
    combined_hex_string = ''.join(hex_string.lstrip("0x") for hex_string in hex_strings)

    print("重组后的十六进制字符串:", combined_hex_string)

    # 将十六进制字符串转换为 Unicode 编码的中文字符
    unicode_chars = [chr(int(combined_hex_string[i:i+4], 16)) for i in range(0, len(combined_hex_string), 4)]

    chinese_text = ''.join(unicode_chars)

    print("中文字符:", chinese_text)
    print()

# 输出制作人信息
print("本脚本制作人: liushenggoodluck")