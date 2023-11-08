import base64

# 从文件中逐行读取中文字符
with open("chinese.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

encoded_string = "bGwtZ29vZGx1Y2t5"
encoded_string2 = "aHR0cHM6Ly9naXRodWIuY29tL2xsLWdvb2RsdWNreS8="
decoded_string = base64.b64decode(encoded_string).decode("utf-8")
decoded_string2 = base64.b64decode(encoded_string2).decode("utf-8")
print("程序作者：", decoded_string)
print("GIThub主页：", decoded_string2)
print()

# 处理每行中的中文字符，并输出结果
for line in lines:
    # 移除行末的换行符
    line = line.rstrip("\n")

    # 输出原始的中文字符
    print("原始中文字符：", line)

    # 将每个中文字符转换为十六进制字符串
    hex_strings = [f"\\u{hex(ord(char))[2:].zfill(4)}" for char in line]
    
    # 将十六进制字符串组合在一起并输出
    print("unicode16位编码：", ' '.join(hex_strings))

    # 将每个中文字符转换为二进制字符串
    binary_strings = [bin(ord(char))[2:].zfill(16) for char in line]

    # 输出未处理的二进制字符串
    print("未处理的二进制字符串：", ' '.join(binary_strings))

    # 处理二进制字符串
    processed_binary_strings = []
    for binary_string in binary_strings:
        processed_binary_string = "1110" + binary_string[:4] + "10" + binary_string[4:10] + "10" + binary_string[10:]
        processed_binary_strings.append(processed_binary_string)

    # 输出处理后的二进制字符串
    print("处理后的二进制字符串：", ' '.join(processed_binary_strings))

    # 将处理后的二进制字符串转换为十六进制字符
    hex_strings = [hex(int(binary, 2))[2:].upper() for binary in processed_binary_strings]

    # 输出十六进制字符
    print("十六进制字符：", ' '.join(hex_strings))


    # 输出空行进行分隔
    print()