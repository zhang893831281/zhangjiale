"""
print("你好，我叫张家乐") #字符串
print(2333) #整数
print(2.333)  # 小数
print(True)   #布尔值
print(False)  #布尔值
print(())    #元祖
print([])      #数组
print({})    #字典


将进酒杯莫停
一曲白歌一剑仙


print("我爱你",520,52.1)
print("woaini"+"我爱你")  #字符串的拼接
print("woaini"*100)       
print(((1+3)*20-90)/2)
print((2+0.5)*4/5)        #int 和double 都是数字，可以运算
print(3<5)               #判断对错



name = "叶晓倩"
print(name)

"""

# a =input("请输入：")    #input（）输入的都是字符串类型
# b =input("请输入：")
# print("input输入的值:",int(a)+int(b))

# c = type(2.33)      #type() 判断数据类型
# print(c)

# print(type("叶晓倩"))
# print(type(520))            ctry+/  注释的快捷键
# print(type(52.1))
# print(type(False))
# print(type(()))
# print(type([]))
# print(type({}))


# a = 'asdasdqwdsaascasasacs'
# print(len(a))                 #len()计算字符串长度

# """
# 通过代码获取两端内容，并且计算他们的长度
# """
# a = input("请输入：")
# b = input("请输入：")
# print("两段字符串的长度之和：",len(a)+len(b))


# #元祖,下标，从0开始标号
# a=(1,2,3,4,"hh","张家乐","张家乐","张家乐1","张家乐2","张家乐3","张家乐4",True,False)
# # print(a[0])
# # print(a[4]+a[5])
# print(a.index("张家乐"))         #a.index() 查询输入值在集合a中出现的位置  
# b = a.count("张家乐")             # a.count()计算集合a中某字符出现的次数
# print("张家乐的次数为：",b)
##切片
# print(a[-2],a[-1])   #可以整数也可以倒数

# print(a[:4])    #左闭右开 [ :4 )
# print(a[4:8])
# print(a[8:])
# print(a[7:11])


# #二维元祖
# a=(1,2,3,4,"hh","张家乐","张家乐","张家乐1","张家乐2")
# b=(a,"叶晓倩","呵呵")       #3个值，集合a在集合b中是一个值
# print(b[0])                  #显示的是集合a
# print(b[0][3])              #查找集合a中的4 ,b[0][3]=a[3]
##index()、count（）、只用于一维



# #数组
# a=[1,2,3,4,"hh","张家乐",True,False]
# a.append("append1")
# a.append("append2")    #往数组最后面追加数据，但是元祖不可以
# print(a)
# #元祖一旦写好后就不可以修改，但是数组可以修改
# a.insert(0,"叶晓倩")
# a.insert(6,"叶晓倩")
# b = a.pop(6)
# c = a.pop(6)
# print(a)
# print(b,c)
# print(a.index(False))
# b = ["nihao","buhao"]
# a.extend(b)
# print(a)

"""
所有的方法都是小括号结尾。比如：print(),input(),len()
元祖数组字典的取值，都是中括号，比如a[0]
元祖，数组，字典分别是（）、[]、{}
"""


#字典
#字典的特点 ：1.字典的值没有顺序
# 2.字典的结构必须是键值对的结构：key : value
# 取值通过key

# a= {"name":"张三","id":3,"years":24}
# # 取值、
# print(a["id"])
# # 新增、
# a["high"] = "183cm"
# a["weight"] = "59kg"
# print(a)
# # 修改
# a["name"] = "李四"
# a["id"] = "1"
# print(a)

# b = a.get("name")
# print(b)
# b = a.pop("years")
# print(a)
# print(b)

# a.update(name="yexiaoqian")
# print(a)

# print("-------")
# print(a.get("name"))
# print(a["name"])

# print("-------")
# print(a.get("name11"))           #如果输入不存在的KEY，get会返回空值，而a[]会报错
# print(a["name11"])

# # 数组和字典的删除
# del a["name"]
# print(a)

# del a[0]
# print(a)

"""
获取用户个人信息，并且存储到字典中
个人信息包括了，name,age,sex.
"""
# name = input("请输入你的姓名：")
# age =input("请输入你的年龄：")
# sex =input("请输入你的性别：")
a = {"name":input("请输入你的姓名："),
"age":input("请输入你的年龄："),
"sex":input("请输入你的性别：")}
print(a)