import os

print(__file__)

# 获取当前脚本的真实路径
current_path = os.path.realpath(__file__)
print(current_path)

# name = os.path.basename(current_path)
# print(name)
# 获取当前脚本文件夹
file_path = os.path.dirname(current_path)
print(file_path)
# 获取上一级文件夹
# shang_path = os.path.dirname(file_path)
# print(shang_path)

ping_path = os.path.join(file_path,)
