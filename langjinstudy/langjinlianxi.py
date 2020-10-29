"""
 现在有10个学生的成绩，需要录入到系统中
 这些人分别是，张一、张二、张三、张四、张五、张六、张七、张八、张九、张十
 并且名字和成绩需要对应上，
 而且分数及格和不及格的要分开存放
"""
# hihtscore={}
# lowscore={}
# studentlist=["张一","张二","张三","张四","张五","张六","张七","张八","张九","张十"]
# for i in range(10):
#     chengji = int(input("请输入"+studentlist[i]+"的成绩："))
#     if chengji >= 60:
#         hihtscore[studentlist[i]] = chengji
#     else:
#         lowscore[studentlist[i]]= chengji
# print("及格的",hihtscore)
# print("不及格的",lowscore)



"""
通过代码获取两端内容，并且计算他们的长度
"""
# a = input("请输入一个值：")
# b = input("请输入一个值：")
# print("长度之和位：",len(a)+len(b))



"""
 获取用户个人信息，并且存储到字典中 
 个人信息包括了，name,age,sex.
"""
# name = input("请输入你的姓名：")
# age = input("请输入你的年龄：")
# sex = input("请输入你的性别：")
# a = {"name":name,"age":age,"sex":sex }
# print(a)
# b = {}
# b["name"] = name
# b["age"] = age
# b["sex"] = sex
# print(b)



"""
现在有10个学生的成绩，需要录入到系统中
这些人分别是，张一、张二、张三、张四、张五、张六、张七、张八、张九、张十
并且名字和成绩需要对应上，
而且分数及格和不及格的要分开存放
"""
# studentlist=["张一","张二","张三","张四","张五","张六","张七","张八","张九","张十"]
# highchengji={}
# lowchengji={}
# a = 0
# while a < 10:
#     chengji = int(input("请输入"+studentlist[a]+"的值"))
#     if chengji <60:
#         lowchengji[studentlist[a]] = chengji
#     else:
#         highchengji[studentlist[a]] = chengji
#     a = a + 1 
# print("成绩合格的人有：",highchengji)
# print("成绩不合格的人有：",lowchengji)


"""
九九乘法表
"""
# for i in range(1,10):
#     for j  in range(1,i+1):
#         print(i,"x",j,"=",i*j,end=" ")
#     print()




"""
练习一
通过打印，模拟一个红绿灯功能，红灯30次，绿灯35次，黄灯3次
练习二
使用代码实现一个注册的功能，简单的来说就是用户输入账号和密码
要求账号长度是5-8位
密码6-12位，并且账号必须小写字母开头。
储存到字典中。{username，password}
"""
# A = (1,2,3,"a","b","哈哈哈")
# B = [4,5,6,"a","b","七七七"]
# deng = {"红灯":30,"绿灯":35,"黄灯":3}
# for i in A:
#     print(i)
# print("------------------------\n")
# for i in B:
#     print(i)
# print("------------------------\n")
# for i in deng:
#     print(i)
# print("------------------------\n")
# while True:
#     for i in deng:
#         for j in range(deng[i]):
#             print("倒计时还剩下：",(deng[i]-j),"秒")

# while True:
#     for i in range(30):
#         print("距离红灯结束还剩",30-i,"秒")
#     for i in range(35):
#         print("距离绿灯结束还剩",35-i,"秒")
#     for i in range(3):
#         print("距离黄灯结束还剩",3-i,"秒")

# username = input("请输入你的账号：")
# password = input("请输入你的密码：")
# if len(username)>=5 and len(username)<=8:
#     if username[0] in "zxcvbnmasdfghjklqwertyuiop":
#         if len(password)>=6 and len(password)<=12:
#             print("账号密码正确",{username:password})
#         else:
#             print("请输入6-12位的正确密码")
#     else:
#         print("请输入开头为小写字母的账号")
# else:
#     print("请输入5-8位的正确账号")



"""
定义一个方法，用来判断用户输入的账号密码是否符合规范
"""
# def checkzhuce(username,password):
#     """
#     定义一个方法，用来判断用户输入的账号密码是否符合规范
#     """
#     if len(username)>=5 and len(username)<=8:
#         if username[0] in "zxcvbnmasdfghjklqwertyuiop":
#             if len(password)>=6 and len(password)<=12:
#                 return "账号密码正确",{username:password}
#             else:
#                 return "请输入6-12位的正确密码"
#         else:
#             return "请输入开头为小写字母的账号"
#     else:
#         return "请输入5-8位的正确账号"

# username = input("请输入你的账号：")
# password = input("请输入你的密码：")
# checkzhuce(username,password)
# print(checkzhuce(username,password))
