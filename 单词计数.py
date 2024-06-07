"""
课后练习:
    单词计数
通过Windows的文本编辑器软件，将如下内容，复制并保存到:word.txt，文件可以存储在任意位置
itheima itcast python
itheima python itcast
beijing shanghai itheima
shenzhen guangzhou itheima
wuhan hangzhou itheina
zhengzhou bigdata itheima
通过文件读取操作，读取此文件，统计python单词出现的次数

"""
# 定义要保存的内容
content = "itheima itcast python\
          itheima python itcast\
          beijing shanghai itheima\
          shenzhen guangzhou itheima\
          wuhan hangzhou itheina\
          zhengzhou bigdata itheima"

# 将内容保存到文件word.txt中
with open("word.txt", "w") as f:
    f.write(content)

    # 读取文件word.txtS
    with open("word.txt", "r") as f:
        text = f.read()

    # 统计python单词出现的次数
    count = text.count("python")

    print(f"Python单词出现的次数是: {count}")

print(f"Python单词出现的次数是: {count}")