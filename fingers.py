
import mediapipe as mp
import cv2
import numpy as np
import time
mphands=mp.solutions.hands
hands=mphands.Hands()
draw=mp.solutions.drawing_utils

import cv2
import time



ptime=0
cap=cv2.VideoCapture(0)

cap.set(3,1240)
cap.set(4,1600)
while True:
  ret,frame=cap.read()
  frame=cv2.flip(frame,1)
  frRgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
  result=hands.process(frRgb)
  print(result.multi_hand_landmarks) 
  if result.multi_hand_landmarks:
    for handLms in result.multi_hand_landmarks:
      
      
      
      
      draw.draw_landmarks(frame,handLms,mphands.HAND_CONNECTIONS)
      fh,fw,fc=frame.shape
      lmlist=dict([(id,[int(lm.x*fw),int(lm.y*fh)]) for id,lm in enumerate(handLms.landmark)])
      
      
      tips = [4, 8, 12, 16, 20]
      fingers=[]
      for id in tips:
          
        #   thumb
          if id==4:
              if lmlist[id][0]>lmlist[id-1][0]:
                  fingers.append(1)
              else:
                  fingers.append(0)
          else:
              if lmlist[id][1]<lmlist[id-2][1]:
                  fingers.append(1)
              else:
                  fingers.append(0)
      
      print(fingers)
      cv2.rectangle(frame, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
      cv2.putText(frame, str(fingers.count(1)), (45, 375), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)
      
      
                  
                  
      
        
    
              
             
            
      
      
    
  ctime=time.time()
  fps=1/(ctime-ptime)
  ptime=ctime
  cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
  
  
      
   
  if not ret:
    break
  cv2.imshow("frame",frame)
  
  if cv2.waitKey(1) and 0xFF==ord('q'):
    break
  


cap.release()
cv2.destroyAllWindows()
                          

