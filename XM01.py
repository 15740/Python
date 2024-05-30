# 课件一内容

# print(ord('北'))
# print(ord('京'))
# print(chr(21271),chr(20140))

# fp=open('note.txt','w')     #打开文件  w-->write
# print('北京欢迎你',file=fp)  #将“北京欢迎你”输出（写入）到note.txt文件中
# fp.close()                  #关闭文件

# print('北京欢迎你'+'2023')
# print('北京欢迎你'+'2023') #TypeError: can only concatenate str (not "int") to str

# if __name__ == '__main__':
#     print_hi('PyCharm')
#    print('我的第一个Python程序')  #单行注释
#   print('我的第二个Python程序')


"""
多行注释
fp=open('note.txt','w')     #打开文件  w-->write
print('北京欢迎你',file=fp)  #将“北京欢迎你”输出（写入）到note.txt文件中
fp.close()
"""

# name =input('请输入您的姓名：')
# print('我的姓名是：'+name)
"""
num=input('请输入您的幸福数字：')
print('您的幸福数字是：'+num)
num=int(num)
print('您的幸福数字是：'+num)
"""

print(1,2,3)
fp = open('test.txt','w')
print(1,2,3,sep='---',end='<+++>',file=fp)
fp.close()



