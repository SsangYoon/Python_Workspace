# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 11.
@attention: 변수에 대해 
@author: Sangyun
'''

#변수를 만들어보자 
#변수는 등호를 이용해서 만든다 
Variable_A = "A"
Variable_Gay = "Gay"
Variable_Favorite = "EATING"        

#변수는 레퍼런스이다 
A = 10          # A -> 10        현재 10이라는 객채의 레퍼런스 카운트 : 1
B = 10          # B -> 10        현재 10이라는 객체의 레퍼런스 카운트 : 2

#Python 내부함수 is는 서로 같은 객체를 가리키고 있는지 아닌지를 판단해준다 
print (A is B)  # True

#변수 삭제하는 방법 
del (A)         # A변수 삭제        현재 10이라는 객체의 레퍼런스 카운트 : 1
del (B)         # B변수 삭제        현재 10이라는 객체의 레퍼런스 카운트 : 0

#이렇게 메모리에 할당된 객체의 레퍼런스 카운트가 0이되면,
#자동으로, 객체는 해제된다 - Garbage Collection


#변수를 만드는 여러가지 방법 
#다 똑같다 
#Tuple, List로 감싸서 만든다고 해서,
#변수가 Tuple, List의 속성을 갖는 것은 아니다 
a, b = 10 , 20
(a, b) = (10, 20)
(a, b) = [10 , 20]
[a, b] = [10, 20]
[a, b] = (10 ,20)
print (a, b)            # 10 20

#여러 변수에 같은 값 대입 
Variable_0 = Variable_1 = 10;      
print (Variable_0, Variable_1)     # 10 10

#변수 값을 서로 바꾸기 
A_Swap_Variable = 10
B_Swap_Variable = 20
C_Swap_Variable = 30
print (A_Swap_Variable, B_Swap_Variable, C_Swap_Variable)       # 10 20 30

#Swapping - 혁신이다 이건 
A_Swap_Variable, B_Swap_Variable, C_Swap_Variable = B_Swap_Variable, C_Swap_Variable, A_Swap_Variable
print (A_Swap_Variable , B_Swap_Variable, C_Swap_Variable)      # 20 30 10

#레퍼런스를 이해해보자 
List = [10 , 20]            # List -> List[0],List[1] -> 10, 20
A_Ref = List[0]             # List[0]이 가리키고 있는 10 객체를 참조하고 있음 
B_Ref = List[1]             # List[1]이 가리키고 있는 20 객체를 참조하고 있음 
print (A_Ref, B_Ref)        # 10 20

List[0] = 40                #하지만, A,B_Ref는 각각 List가 가리키는 List[0],List[1] 아닌,
List[1] = 50                #10, 20을 가리키고 있기 때문에 A,B_Ref는 여전히 10, 20을 참조한다.  

print (A_Ref, B_Ref)        # 10 20
                 
A_List = [10, 20, 30]   # A_List -> A_List[0],A_List[1],A_List[2] -> 10, 20, 30
B_List = A_List         # B_List -> A_List[0],A_List[1],A_List[2] -> 10, 20, 30
A_List[0] = 40          # 그렇기 때문에 A_List를 바꾸면, B_List도 자연스레 바뀌게된다 
print (B_List)          # [40, 20, 30]
B_List[0] = 50          # 또한, 같은 객체이므로 B를 바꿔도 A도 같이 바뀐다 
print (A_List)          # [50, 20, 30]

#그래서...
#값은 같지만 서로다른 객체를 참조 하려면!!
# 방법 1
A_Other_List = [10, 20, 30]
B_Other_List = A_Other_List[:]              # [:]는 리스트 전체를 뜻한다 
print (A_Other_List is B_Other_List)        # False // 값은 서로 같지만, 참조하는 객체의 위치가 다르다.

#방법 2
from copy import copy 
C_Other_List = ["I`m ", "Real ", "Gay"]
D_Other_List = copy(C_Other_List)
print (C_Other_List is D_Other_List)        # False // 마찬가지

