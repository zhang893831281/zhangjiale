# a= input("请输入你的名字：")
# b = input("请输入你的年龄：")
# try:
#     if int(b)>18:
#         print(a+"你成年了")
#     else:
#         print(a+"你还未成年")
# except Exception as e:
#     print("你输入的年龄不是int",e)

import time
import random
import pymysql
# for i in range(10):
#     time.sleep(1)
#     print(i)

# a = random.randint(0,100)
# print(a)

# db = pymysql.connect("localhost","root","893831281","zhangjiale")
# cursor = db.cursor()
# cursor.execute("select * from actor")
# res = cursor.fetchall()
# print(res)


# db = pymysql.connect("localhost","root","893831281","zhangjiale")
# cursor = db.cursor()
# try:   
#     cursor.execute("select * from actor")
#     res = cursor.fetchall()
#     print(res)
# except:
#     print("mysql语句有误")


"""
Class 声明类的名字
然后类的名字首字母必须大写
面向对象编程
类里面所有的方法，都必须传一个参数，叫self
"""

# class GrilFriend():
#     """
#     女朋友
#     """
#     def __init__(self):
#         self.sex = "女"
#         self.high = "175cm"
#         self.weight = "56kg"
#         self.hair = "大波浪"
#         self.age = "20岁"
#     def caiyi(self,num):
#         """
#         才艺表演
#         """
#         print("你性别"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女友开自己的才艺表演之：")
#         if num == 1:
#             print("唱歌、跳舞")
#         elif numm == 2:
#             print("画画") 
#         else:
#             print("单手开瓶盖")
#     def chuyi(self):
#         """
#         做饭持家
#         """
#         print("你性别"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女友开自己的厨艺：")
#         print("会做简单的菜肴")  
#     def work(self):
#         """
#         工作挣钱
#         """
#         print("公司HR") 

# #类的实例化
# yexiaoqian = GrilFriend()
# yexiaoqian.caiyi(1)
# yexiaoqian.work()
# print(yexiaoqian.high)

              
class GrilFriend():
    """
    女朋友
    """
    def __init__(self,sex,high,weight,hair,age):
        self.sex = sex
        self.high = high
        self.weight = weight
        self.hair = hair
        self.age = age
    def caiyi(self,num):
        """
        才艺表演
        """
        print("你性别"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女友开自己的才艺表演之：")
        if num == 1:
            print("唱歌、跳舞")
        elif numm == 2:
            print("画画") 
        else:
            print("单手开瓶盖")
    def chuyi(self):
        """
        做饭持家
        """
        print("你性别"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女友开自己的厨艺：")
        print("会做简单的菜肴")  
    def work(self):
        """
        工作挣钱
        """
        print("公司HR") 

# yexiaoqian = GrilFriend("女","160cm","45kg","锡纸烫","20岁")
# yexiaoqian.caiyi(1)
# yexiaoqian.work()
# print(yexiaoqian.high)


# class Car():
#     def __init__(self,pinpai,yanse,neishi,jilun):
#         self.pinpai = pinpai
#         self.yanse = yanse
#         self.neishi = neishi
#         self.jilun = jilun
#     def bianxing(self):
#         print("车子变型")
#     def fly(self):
#         print("车子会飞")

# zhang = Car("奥括","黑色","简易","4")
# zhang.bianxing()
# zhang.fly()

class Nvpengy(GrilFriend):    #类的进程GrilFriend父类 。 Nvpengy子类
    def work(self):
        print("打游戏")
yexiaoqian = Nvpengy("女","160cm","45kg","锡纸烫","20岁")    
print(yexiaoqian.sex)
yexiaoqian.caiyi(1)
yexiaoqian.work()