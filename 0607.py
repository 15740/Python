#6月7日
f = open('python.txt')
content = f.readlines()
# ['hello world\n', ' abcdefg\n', ’aaa\n'， 'bbb\n'. 'ccc']
print(content)
# 关闭文件
f.close()

f =open('python.txt')
content = f.readline ()
print(f'第一行：(content)')
content = f.readline()
print(f'第二行：(content)')
#关闭文件
f.close()