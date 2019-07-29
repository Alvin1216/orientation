import cv2
import dlib
import numpy as np


PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
#已經訓練好的資料
predictor = dlib.shape_predictor(PREDICTOR_PATH)
#cascade_path='haarcascade_frontalface_default.xml'
#cascade = cv2.CascadeClassifier(cascade_path)
detector = dlib.get_frontal_face_detector()


def get_landmarks(im):
    #透過dlib預先train好的資料拿來抓臉
    #回傳 眼睛 鼻子 臉邊 嘴唇的座標
    rects = detector(im, 1)
    if len(rects) > 1:
        return "error"
    if len(rects) == 0:
        return "error"
    return np.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])


def annotate_landmarks(im, landmarks):
    im = im.copy()
    for idx, point in enumerate(landmarks):
        pos = (point[0, 0], point[0, 1])
        cv2.putText(im, str(idx), pos,
                    fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
                    fontScale=0.4,
                    color=(0, 0, 255))
        cv2.circle(im, pos, 3, color=(0, 255, 255))
    return im

def top_lip(landmarks):
    #和top_lip不同的點在於
    #top_lip回傳的是y軸[1]
    #這一個top_lip_x_axis是回傳x軸[0]
    #現在把它改成[0]_回傳x_axis
    #因為現在是要判定左右
    #上嘴唇不會歪 下嘴唇會歪 所以可以保持平均(這個好像不行)
    #全部改回來 都用max
    top_lip_pts = []
    for i in range(50,53):
        top_lip_pts.append(landmarks[i])
    for i in range(61,64):
        top_lip_pts.append(landmarks[i])
    top_lip_all_pts = np.squeeze(np.asarray(top_lip_pts))
    top_lip_max = np.max(top_lip_pts, axis=0)
    #print("int(top_lip_max[:,0])")
    #print(int(top_lip_max[:,0]))
    return int(top_lip_max[:,0])

def bottom_lip(landmarks):
    #和bottom_lips不同的點在於
    #bottom_lips回傳的是y軸[1]
    #這一個bottom_lip_x_axis是回傳x軸[0]
    #現在把它改成[0]_回傳x_axis
    #因為現在是要判定左右
    #用平均不准 所以改成用max
    bottom_lip_pts = []
    for i in range(65,68):
        bottom_lip_pts.append(landmarks[i])
    for i in range(56,59):
        bottom_lip_pts.append(landmarks[i])
    bottom_lip_all_pts = np.squeeze(np.asarray(bottom_lip_pts))
    bottom_lip_max = np.max(bottom_lip_pts, axis=0)
    #print("bottom_lip_max")
    #print(bottom_lip_max)
    return int(bottom_lip_max[:,0])

def mouth_open(image):
    #top_lip_center原本是抓y的所有點的平均值
    #現在top_lip_center抓的是所有上嘴唇x的平均值
    #bottom_lip_center原本是抓y的下嘴唇的平均值
    #現在top_lip_center抓的是所有下嘴唇x的最大值
    landmarks = get_landmarks(image)
    
    if landmarks == "error":
        return image, 0
    
    image_with_landmarks = annotate_landmarks(image, landmarks)
    top_lip_center = top_lip(landmarks)
    bottom_lip_center = bottom_lip(landmarks)
    lip_distance = abs(top_lip_center - bottom_lip_center)
    return image_with_landmarks, lip_distance

    #cv2.imshow('Result', image_with_landmarks)
    #cv2.imwrite('image_with_landmarks.jpg',image_with_landmarks)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
skews = 0
skews_status = False 

while True:
    ret, frame = cap.read()   
    image_landmarks, lip_distance = mouth_open(frame)
    
    prev_skews_status = skews_status  
    
    if lip_distance > 2.5:
        skews_status = True 
        
        cv2.putText(frame, "Subject is skewing", (50,450), 
                    cv2.FONT_HERSHEY_COMPLEX, 1,(0,0,255),2)
        

        #output_text = " Skews Count: " + str(skews + 1)

        #cv2.putText(frame, output_text, (50,50),
                    #cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,127),2)
        
    else:
        skews_status = False 
         
    if prev_skews_status == True and skews_status == False:
        skews += 1

    cv2.imshow('Live Landmarks', image_landmarks )
    cv2.imshow('Skew Detection', frame )
    
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()