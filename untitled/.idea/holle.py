
#_*_coding: UTF-8_*_
# print "你好 小尚";print("贾林");print('好好学习');
# str="abc";
# num=10;
# print num;
# print str;
# stt=100.1;
# print stt;
#
# str1="aaa";
# str2="bbb";
# str3="ccc";
# temp=str1+\
#      str2+\
#      str3;
# print temp;
# num1=10;
# num2=20;
# num3=30;
# temp1=num1+\
#     num2+\
#     num3;
# print temp1;
#
# a=3;
# if(a>3
#    ):
#     print("周衡是好人");
# else:
#     print("贾林是坏蛋");




# Filename : test.py
# author by : www.runoob.com

# 定义函数
# def add(x, y):
#     """相加"""
#
#     return x + y
#
#
# def subtract(x, y):
#     """相减"""
#
#     return x - y
#
#
# def multiply(x, y):
#     """相乘"""
#
#     return x * y
#
#
# def divide(x, y):
#     """相除"""
#
#     return x / y
#
#
# # 用户输入
# print("选择运算：")
# print("1、相加")
# print("2、相减")
# print("3、相乘")
# print("4、相除")
#
# choice = input("输入你的选择(1/2/3/4):")
#
# num1 = int(input("输入第一个数字: "))
# num2 = int(input("输入第二个数字: "))
#
# if choice == 1:
#     print(num1, "+", num2, "=", add(num1, num2))
#
# elif choice == 2:
#     print(num1, "-", num2, "=", subtract(num1, num2))
#
# elif choice == 3:
#     print(num1, "*", num2, "=", multiply(num1, num2))
#
# elif choice == 4:
#     print(num1, "/", num2, "=", divide(num1, num2))
# else:
#     print("非法输入")


for a in range(1,10):
    d = []
    for b in range(1,10):
        if b <= a:
            c = '%d*%d=%d'%(a,b,a*b)
            d.append(c)
    print(d)