#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：李熙
日期：2020/4/16
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
	 """
	 将游戏对象对应到不同的整数
	 """
	 if name=="石头":
		 number=0
	 if name=="史波克":
		 number=1
	 if name=="纸":
		 number=2
	 if name=="蜥蜴":
		 number=3
	 if name=="剪刀":
		 number=4
	 return number   
    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果
def number_to_name(number):
	"""
	将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	"""
	if number==0:
		name="石头"
	if number==1:
		name="史波克"
	if number==2:
		name="纸"
	if number==3:
		name="蜥蜴"
	if number==4:
		name="剪刀"
	return name
    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果



def rpsls(player_choice):
	"""
	用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
	"""
	if player_choice!="石头" and player_choice!="剪刀" and player_choice!="蜥蜴" and player_choice!="史波克" and player_choice!="纸":#输入不正确的游戏对象时，屏幕输出Error: No Correct Name
		print("Error: No Correct Name")
	else:#输入正确的游戏对象
		print("--------") # 输出"-------- "进行分割
		player_choice_number=int(name_to_number(player_choice))# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
		comp_number=random.randint(0,4) # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
		name=number_to_name(comp_number) # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
		print("计算机的选择为：%s"%(name))# 在屏幕上显示计算机选择的随机对象
		dif=comp_number-player_choice_number
		if dif>2 or dif==(-1) or dif==(-2):#利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
			print("您赢了")
		elif dif==0:
			print("您和计算机出的一样")
		else:
			print("计算机赢了")# 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
# 对程序进行测试
print("欢迎使用RPSLS游戏")#提醒游戏已经开始
print("----------------")#用分割线分割
print("请输入您的选择:")
choice_name=input()#输入玩家的选择
rpsls(choice_name)#使用自定义函数rpsls


