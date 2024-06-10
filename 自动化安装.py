import os
import requests
import zipfile

# 获取名字
response = requests.get('https://blog.yaqwq.top/cz/czm.txt')
response.encoding = 'utf-8'
names = response.text.split('\n')
print("收录同步官网首页，可前往官网首页查看")
print("以下是收录的插件列表，按照提示输入名字即可")

z = 1
# 输出所有名字
for name in names:
    print(f"{z}{":"}{name}")
    z = z + 1

# 获取用户输入
plugin_dir = input('请输入LiteLoaderQQNT的插件位置（例如D:/LiteLoaderQQNT/plugins）: ')
line_number = input("请输入需要安装的插件所在行数: ")
try:
    line_number = int(line_number)
except ValueError:
    input("输入错误")

# 获取文件链接
print("正在获取对应链接")
response = requests.get('https://blog.yaqwq.top/cz/cz.txt')
response.encoding = 'utf-8'
links = response.text.split('\n')
link = links[line_number - 1]

# 创建文件夹
folder_name = names[line_number - 1]
folder_path = os.path.join(plugin_dir, folder_name)
os.makedirs(folder_path, exist_ok=True)


# 下载文件
print("正在下载文件（如果失败需要确保自己可以访问github）")
response = requests.get(link)
filename = os.path.join(plugin_dir, f'{name}.zip')
with open(filename, 'wb') as f:
    f.write(response.content)

# 解压文件
print("解压中")
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(folder_path)

# 删除文件
os.remove(filename)
input("安装已完成，按下回车退出")
