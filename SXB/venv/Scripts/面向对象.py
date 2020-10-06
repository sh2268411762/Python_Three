# class Person:
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def print_person(self):
#         print("姓名：", self.name)
#         print("年龄：", self.age)
#         print("身高：", self.height)
#         print("体重：", self.weight)
#
#
# # person = Person("小王", 20, 180, 60)
# # person.print_person()
#
#
# class Student:
#     def __init__(self, name, age, height, weight, grade):
#         self.__grade = grade
#         self.name = name
#         if age < 0 or age > 130:
#             while True:
#                 age = int(input("年龄输入非法，重新输入："))
#                 if age < 0 or age > 130:
#                     pass
#                 else:
#                     self.age = age
#                     break
#         self.age = age
#         self.height = height
#         self.weight = weight
#
#     def print_Stu(self):
#         print("姓名：", self.name)
#         print("年龄：", self.age)
#         print("身高：", self.height)
#         print("体重：", self.weight)
#         print("成绩：", self.__grade)
#
#     def set_Name(self):
#         name = input("请输入要修改的姓名：")
#         self.name = name
#
#     def set_Height(self):
#         height = int(input("请输入要修改的身高："))
#         self.height = height
#
#     def set_Weight(self):
#         weight = int(input("请输入要修改的体重："))
#         self.weight = weight
#
#     def set_Grade(self):
#         grade = int(input("请输入要修改的成绩："))
#         self.__grade = grade
#
#     def set_Age(self):
#         age = int(input("请输入要修改的年龄："))
#         if age < 0 or age > 130:
#             while True:
#                 age = int(input("年龄输入非法，重新输入："))
#                 if age < 0 or age > 130:
#                     pass
#                 else:
#                     self.age = age
#                     break
#         else:
#             self.age = age
#
#     @staticmethod
#     def __say(name):
#         print(name)
#
#     def play(self):
#         self.__say("？？？")
#
#
# class Family(Student):
#     def __init__(self):
#         self.father = ""
#         self.mother = ""
#         super(Family, self).__init__("小明", 22, 180, 67, 88)
#
#     def setFather(self):
#         dad = input("请输入父亲姓名：")
#         self.father = dad
#
#     def setMother(self):
#         mom = input("请输入母亲姓名：")
#         self.mother = mom
#
#     def play1(self):
#         print("我的名字：", self.name, end='，')
#         print("我的父亲：", self.father, "，我的母亲：", self.mother)
#
#
# # stu1 = Student("小李", 9, 180, 70, 90)
# # print(type(stu1))
# # stu1.print_Stu()
# # stu1.set_Grade()
# # stu1.print_Stu()
# f1 = Family()
#
# f1.setFather()
# f1.setMother()
# f1.play1()


# # 多态
# class Animal:
#     def say(self):
#         print("Animal")
#
#
# class Dog(Animal):
#     def say(self):
#         print("Dog")
#
#
# class Cat(Animal):
#     def say(self):
#         print("Cat")
#
#
# def animal_say(animal: Animal):
#     animal.say()
#
#
# dog = Dog()
# cat = Cat()
# dog.say()
# cat.say()
# animal_say(dog)
# animal_say(cat)
# # 判断一个实例是不是某个对象
# print(isinstance(dog, Dog))
# print(isinstance(dog, Animal))
# print(isinstance(dog, Cat))
# print(isinstance(cat, Cat))
# print(isinstance(cat, Animal))
# print(isinstance(cat, Dog))


