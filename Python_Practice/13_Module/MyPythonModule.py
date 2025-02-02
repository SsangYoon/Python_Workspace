# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 13.
@attention: Module_Practice.py에서 임포트시킬 모듈 
@author: Sangyun
'''

class Person:               # 배껴오기 신공!!
    def __init__(self):     # 생성자 
        pass                # 함수 아래에 아무라인이 없으면 Indentation(들여쓰기) 오류남  
    
    def Set_State(self, Name, Height, Weight) : # 첫번째 인자 self는 자기자신을 뜻하며, 따로 대입하지 않는다 
        self.Name = Name                        # self가 항상 첫번째 인자로 되어있어야함!! 
        self.Height = Height
        self.Weight = Weight
        
    def Show_State(self) : 
        print ("Name : " + self.Name)
        print ("Height : " + str(self.Height))       # 문자열로 형변환 
        print ("Weight : " + str(self.Weight))
        
def Sum(*NumberList):   # 여러개의 인자를 받아와서 튜플로 만들어줌 
    SumNumber = 0
    
    for Number in NumberList:
        SumNumber += Number
         
    return SumNumber

def HelloWorld():
    print ("Hello World")


if __name__ == "__main__":          # 만약 요놈이 없으면,
    print ("MyPythonModule.py")     # 다른 모듈에서 임포트 시킬 때
                                    # 아래에 있는 print가 실행되어 버린다 
                                    # __name__어트리 뷰트는 파이썬 인터프리터가
                                    # 이 파일을 직접 실행시켰을 때 __main__을 가진다 



