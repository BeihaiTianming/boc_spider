# 输入
input_str, k = input("Input string and k:").split()
k = int(k)
char_list = list(input_str)

# 遍历与替换
for i in range(len(char_list)):
    if char_list[i] in input_str[max(0, i-k):i]:
        char_list[i] = '-'

# 转换回字符串
output_str = ''.join(char_list)
print(output_str)