# -*- coding: utf--8 -*-
'''
Created on 2015. 8. 12.
@attention: About Function 
@author: Sangyun
'''

# 포풍저그 콩진호가 간다!!
# 빠르게 가자 

# 함수 정의법  
# Retrun값을 넣어도 되고 안넣어도 된다
# 매개인자도 넣어도 되고 안넣어도 된다
# 매개인자를 *Value로 쓰게되면 여러개의 매개인자를 튜플로 만들어서 받아오게된다 
# 디폴트값을 설정할 수 있다 
def Hello_Function () :
    print ("Hello")
    
def Number_Function (Number) : 
    print ("Number : %d" % Number)

def Return_Function () : 
    return "GAAAAY"

def Multiply_Function (*Numbers) :  # Numbers
    print (Numbers)

def Default_Function (Name, Info = "GAY") : # Default매개인자는 항상 오른쪽 부터 존재해야한다 
    print ("Name : " + Name)                # (Name = "Sangyoon", Info)로 매개인자부분이 써져있으면 
    print ("Info : " + Info)                # Default_Function("asdf")는 전달되는 방법이 모호해지기 때문이다       

# 함수 사용법 
Hello_Function ()
Number_Function (99999)
print (Return_Function ())                  # 반환되는 값을 받아와서 출력 
Multiply_Function (3, 4, 2, 1, 3)           # 여러개의 매개인자를 튜플로 묶어서 Numbers로 전달한다 
Multiply_Function (1)                       # 한개의 매개인자를 받았을 때도 튜플로 만든다 
Default_Function ("You")                    # 디폴트값을 쓰고싶으면 비워 놔도 된다
Default_Function ("Sangyoon", "NOT GAY")    # 디폴트값을 안써도된다 


# 함수내에서 생성된 변수 
def In_Function () :
    Value = 99999       # In_Function함수 블록에서 선언되었으므로 함수안에서만 사용가능하다
                        # 또한 함수에서 벗어나게 되면 함수내에서 선언된 변수는 모두 사라지게 된다
    print (Value)       

# print (Value)           # NameError: name 'Value' is not defined

