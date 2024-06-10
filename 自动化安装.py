import os
import requests
import zipfile

# 检查版本
version_url = 'https://blog.yaqwq.top/cz/b.txt'
response_version = requests.get(version_url)
response_version.encoding = 'utf-8'
current_version = response_version.text.strip()

if current_version != '1.00':
    print("当前脚本版本不是1.00，请前往 https://github.com/WSXYT/LiteLoaderQQNT-Automatic-plugin-installation/releases 更新。")
    input("按回车键退出...")
    exit(0)

# 继续原有逻辑
# 获取名字
response = requests.get('https://blog.yaqwq.top/cz/czm.txt')
response.encoding = 'utf-8'
names = response.text.split('\n')
print("收录同步官网首页，可前往官网首页查看")
print("以下是收录的插件列表，按照提示输入名字即可")

z = 1
# 输出所有名字
for name in names:
    print(f"{z}:{name}")
    z += 1

# 获取用户输入
plugin_dir = input('请输入LiteLoaderQQNT的插件位置（例如D:/LiteLoaderQQNT/plugins）: ')
line_number = input("请输入需要安装的插件所在行数: ")
try:
    line_number = int(line_number)
except ValueError:
    input("输入错误，请重新运行脚本。")
    exit(1)

# 获取文件链接
print("正在获取对应链接")
response = requests.get('https://blog.yaqwq.top/cz/cz.txt')
response.encoding = 'utf-8'
links = response.text.split('\n')
link = links[line_number - 1]

folder_name_raw = names[line_number - 1]
folder_name = folder_name_raw.split('-')[0].strip()  # 更简单的方式获取'-'前的名字
folder_path = os.path.join(plugin_dir, folder_name)
os.makedirs(folder_path, exist_ok=True)

# 下载文件
print("正在下载文件（如果失败需要确保自己可以访问github）")
response = requests.get(link)
filename = os.path.join(plugin_dir, f'{folder_name}.zip')
with open(filename, 'wb') as f:
    f.write(response.content)

# 解压文件
print("解压中")
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall(folder_path)

# 删除文件
os.remove(filename)
input("安装已完成，按下回车退出")
