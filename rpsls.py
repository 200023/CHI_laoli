#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2020/4/16
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	 """
	 ����Ϸ�����Ӧ����ͬ������
	 """
	 if name=="ʯͷ":
		 number=0
	 if name=="ʷ����":
		 number=1
	 if name=="ֽ":
		 number=2
	 if name=="����":
		 number=3
	 if name=="����":
		 number=4
	 return number   
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""
	if number==0:
		name="ʯͷ"
	if number==1:
		name="ʷ����"
	if number==2:
		name="ֽ"
	if number==3:
		name="����"
	if number==4:
		name="����"
	return name
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��



def rpsls(player_choice):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	"""
	if player_choice!="ʯͷ" and player_choice!="����" and player_choice!="����" and player_choice!="ʷ����" and player_choice!="ֽ":#���벻��ȷ����Ϸ����ʱ����Ļ���Error: No Correct Name
		print("Error: No Correct Name")
	else:#������ȷ����Ϸ����
		print("--------") # ���"-------- "���зָ�
		player_choice_number=int(name_to_number(player_choice))# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
		comp_number=random.randint(0,4) # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
		name=number_to_name(comp_number) # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
		print("�������ѡ��Ϊ��%s"%(name))# ����Ļ����ʾ�����ѡ����������
		dif=comp_number-player_choice_number
		if dif>2 or dif==(-1) or dif==(-2):#����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
			print("��Ӯ��")
		elif dif==0:
			print("���ͼ��������һ��")
		else:
			print("�����Ӯ��")# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")#������Ϸ�Ѿ���ʼ
print("----------------")#�÷ָ��߷ָ�
print("����������ѡ��:")
choice_name=input()#������ҵ�ѡ��
rpsls(choice_name)#ʹ���Զ��庯��rpsls


