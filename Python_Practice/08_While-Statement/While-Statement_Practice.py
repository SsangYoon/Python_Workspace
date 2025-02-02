# -*- coding: utf-8 -*-
'''
Created on 2015. 8. 11.
@attention: While-Statement Practice
@author: Sangyun
'''

# While-Statement의 기본구조 
# while <조건문> : 
#    <수행할 문장1>
#    <수행할 문장2>

# While-Statement를 직접 사용해보자 
Attack_Count = 0
while Attack_Count < 10 : 
    Attack_Count += 1           # 만약 이 라인이 없다면 계속해서 참이 되기 때문에 무한루프에 빠지게 된다 
    print ("%d번 공격!" % Attack_Count)
    
# 1번 공격!
# 2번 공격!
# 3번 공격!
# 4번 공격!
# 5번 공격!
# 6번 공격!
# 7번 공격!
# 8번 공격!
# 9번 공격!
# 10번 공격!

# 무한 루프
# while True :                # 이렇게 되면 조건식이 항상 참이기 때문에
#     print ("I`m GAY~!")     # 계속 돌아가게 된다 // 참고 : 실행시키면 안멈춤 
#                             # Python (IDLE)에서 멈출려면 Ctrl + C를 누르면 된다 
#                             # 하지만 Eclipse - PyDev는 Option + Command + F9를 눌러주자 (Terminate All)
#                             # 물론 Mac기준 ㅋ 

    
# Continue와 break
Odd_Number = 0
View_Count = 0
while Odd_Number < 10 :         # continue가 여기로 이동함 
    Odd_Number += 1
    
    while True :                # 무한루프!! 하지만!! 
        if View_Count > 3 : 
            break               # 현재 if문 바로 상단에 있는 while문을 빠져나온다!!
        
        print ("View Count : %d" % View_Count)
        View_Count += 1
        
    if Odd_Number % 2 == 0 : 
        continue                # continue를 사용하면 해당블럭의 조건문으로 이동한다 
    
    print ("%d" % Odd_Number)
    
        