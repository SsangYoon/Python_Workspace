# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 12.
@attention: About Class 
@author: Sangyun
'''

class Person:
    def __init__(self):     # 생성자 
        pass                # 함수 아래에 아무라인이 없으면 Indentation(들여쓰기) 오류남  
    
    def Set_State(self, Name, Height, Weight) : # 첫번째 인자 self는 자기자신을 뜻하며, 따로 대입하지 않는다 
        self.Name = Name                        # self가 항상 첫번째 인자로 되어있어야함!! 
        self.Height = Height
        self.Weight = Weight
        
    def Show_State(self) : 
        print ("Name : " + self.Name)
        print ("Height : " + str(self.Heigh))       # 문자열로 형변환 
        print ("Weight : " + str(self.Weight))
    
    def Say(self, OtherPerson, Speech = "Hello") :           # self는 클래스 메소드를 정의할 때 꼭 있어야만 한다 
        print (Speech, OtherPerson.Name)                     # 없으면, 클래스 메소드인지, 일반함수인지 구분을 못함 -> 에러
    
    def __add__(self, Other_Person):            # 연산자 오버로딩 - 참고 : 함수오버로딩은 안돼요 
        print ("%s와 %s가 결혼을 하였습니다!!" % (self.Name, Other_Person.Name))
    

class Sangyoon(Person):         # Sangyoon이 Person을 상속함 
    def __init__(self):
        pass
    
    def Set_State(self):        # 함수 오버라이드 
        Person.Set_State(self, "Sangyoon", 177, "Unlimited")    # Person클래스에 있는 함수를 사용 
        
    
    
I = Sangyoon()      # 생성자로 클래스 객체 생성 
I.Set_State()       # 클래스 변수 생성,초기화 

You = Person()      # 생성자로 클래스 객체 생성 
You.Set_State("E.T", 290, 1903)     # 참고 : 외계인임 

I.Say(You, "Hi")        # 디폴트값 미사용 
You.Say(I)              # 디폴트값 사용 

I + You


# 클래스의 기본적인 것들이다 
# 가상함수 그딴거 없다 
# 자료형이 없거등 ㅇㅇ 
