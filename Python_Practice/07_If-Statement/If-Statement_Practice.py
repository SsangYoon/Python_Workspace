# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 11.
@attention: If문에 대해서 
@author: Sangyun
'''

# If-Statement를 사용해보자 
Current_State = {"Health" : "Good", "Cash" : 0, "Card" : True}

def HealthView (Health_State) :
    if Health_State == "Good" :             # :(콜론) 꼭 붙여주자 
        print ("Health : " + Health_State)  # Indentation(들여쓰기)에 주의하자 Python은 괄호가아닌 Indentation으로 영역을 구분하기 때문이다 
        
    elif Health_State == "Bad" :            # else if --> elif 
        print ("Health : " + Health_State)
        
    else :
        pass                # 아무것도 하지않는 다는 의미 // 그렇다고해서 아래 라인이 실행되지 않는 것은 아니다 
        #print ("Error")    # else레이블 아래에 아무것도 없으면 구문오류가 발생하므로 pass를 사용한다 
    
    
def CashView (Cash_State) :
    if Cash_State > 0 :
        print ("Cash : " + str(Cash_State))
    
    else : pass      # 이처럼 pass를 옆에 써도 된다 // 그냥 else레이블을 없애는게 더 나은...
    
def CardView (Card_State) :
    if Card_State :
        print ("Card : I have")
        
        
HealthView (Current_State["Health"])
CashView (Current_State["Cash"])
CardView (Current_State["Card"])


# 비교연산자 목록 
# Value == Value         # 두 변수가 같다 
# Value != Value         # 두 변수가 다르다 
# Value >  Value         # 여기서 부터는 일반인도 아니까 넘어가자 
# Value <  Value 
# Value >= Value 
# Value <= Value 

# And, Or, Not 연산자 목록 
# X and Y          # X, Y 둘다 참이여야 참 
# X or Y           # X, Y 둘 중 하나라도 참이면 
# not X            # X가 거짓이면 

# In, Not In 연산자 - 중요!
# Value in List
# Value in Tuple
# Value in String(문자열)

# Value not it List
# Value not it Tuple
# Value not it String(문자열)

# Example
Pocket = ["Cash", "Card", "Smartphone"]     # 주머니에 있는 것들 
Head = ()                                   # 머리가 비었다!!
Info = "I`m Gay"                            # 나는 게이다!!

if "Cash" in Pocket : 
    print ("I Have Cash")
    
if "Card" in Pocket :
    print ("I Have Card")
    
if "Smartphone" in Pocket : 
    print ("I Have Smartphone")
    
if "Brain" not in Head :
    print ("I Have no Brain")
    
if "I`m" in Info and "Gay" in Info : 
    print ("I`m Certainly GAY!!")




