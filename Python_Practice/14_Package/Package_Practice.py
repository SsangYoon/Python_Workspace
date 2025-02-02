'''
Created on 2015. 8. 13.
@attention: Package_Practice
@author: Sangyun
'''

# Package를 임포트 해보자 
# Relative Package 접근자
# . - 현재 디렉토리
# .. - 부모 디렉토리 

from Game.Initialize.Initialize import *            # Initialize.py에 있는 Initialize클래스의 모든 것을 임포
from Game.Release.Release import *                  # 밑에 것도 마찬가지 
from Game.Update.Update import *    
from Game.Render.Render import *

Initialize_Value = Initialize()
Release_Value = Release()
Update_Value = Update()
Render_Value = Render()

if __name__ == '__main__':
    Initialize_Value.Load_Data()
    Initialize_Value.LoadData.Data_View()
    Initialize_Value.Initialize_View()
    Release_Value.Release_View()
    Update_Value.Update_View()
    Render_Value.Render_View()
    
    