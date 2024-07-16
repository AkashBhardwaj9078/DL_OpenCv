import cv2
import mediapipe as mp
import time

detect_face=mp.solutions.face_detection
detect_face_mod=detect_face.FaceDetection()
face_draw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)
cap.set(3,1200)
cap.set(4,1200)
while True:
  ret,frame=cap.read()
  frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
  faces=detect_face_mod.process(frame)
  if faces.detections:
    for id,detection in enumerate(faces.detections):
      face_draw.draw_detection(frame,detection)
      print(detection.score)
     
      print(detection.location_data.relative_bounding_box)
      print(detection.location_data.relative_keypoints)
      bbox=detection.location_data.relative_bounding_box
      fh,fw,fc=frame.shape
      x,y,w,h=int(bbox.xmin*fw),int(bbox.ymin*fh),int(bbox.width*fw),int(bbox.height*fh)
      cv2.putText(frame,str(int(detection.score[0]*100))+"%",(x,y-20),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
      cv2.line(frame,(x,y),(x+20,y),(255,255,0),20)
      cv2.line(frame,(x,y),(x,y+20),(255,255,0),20)
      cv2.line(frame,(x+w-20,y+h),(x+w,y+h),(255,255,0),20)
      cv2.line(frame,(x+w,y+h-20),(x+w,y+h),(255,255,0),20)
      cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),10)
  
  cv2.imshow("frame",frame)
  if cv2.waitKey(1) and 0xFF==ord('q'):
    break

cap.release()
cv2.destroyAllWindows()