import cv2
import numpy as np
import time

def region_of_interest(img,vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def drawLines(img,lines):
    img = np.copy(img)
    blank_img=np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)
    if lines is not None:
        for line in lines:
            for x1,y1,x2,y2 in line:
                cv2.line(blank_img,(x1,y1),(x2,y2),(0,255,0),thickness=10)
    img = cv2.addWeighted(img, 0.8, blank_img, 1, 0.0)
    return img

def process(img):
    height,width = img.shape[0],img.shape[1]
    region_of_interest_vertices = [(0,height) , (width/2 , height/2) , (width,height)] 
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cany_img = cv2.Canny(gray_img,250,120)
    cropped_image = region_of_interest(cany_img,np.array([region_of_interest_vertices],np.int32))
    lines = cv2.HoughLinesP(cropped_image, 
                            rho=2, 
                            theta=np.pi/180, 
                            threshold=220,
                            lines=np.array([]),
                            minLineLength=150,
                            maxLineGap=5)
    imgWithLine = drawLines(img,lines)
    return imgWithLine

# Video kaynağı
cap = cv2.VideoCapture("video2.mp4")

prev_time = time.time()

while True:
    success , img = cap.read()
    if not success:
        break

    img = process(img)

    # FPS hesaplama
    current_time = time.time()
    fps = 1 / (current_time - prev_time + 1e-6)
    prev_time = current_time

    # FPS'i ekrana yaz
    cv2.putText(img, f"FPS: {int(fps)}", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow("img",img)
    if cv2.waitKey(20) & 0xFF == ord('q'):  # 'q' ile çık
        break

cap.relea
