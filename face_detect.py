import cv2 

face_cascade = cv2.CascadeClassifier("C:\\Users\\ADMIN\\Downloads\\happiness begins here\\open cv\\haarcascade_frontalface_default.xml")

# cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture("C:\\Users\\ADMIN\\Desktop\\lol\\VID-20230306-WA0000.mp4")
''' Not working below link '''
cap = cv2.VideoCapture("C:\\Users\\ADMIN\\Downloads\\happiness begins here\\open cv\VID-20230520-WA0000.mp4")

# img = cv2.imread("C:\\Users\\ADMIN\\Pictures\\Screenshots\\Screenshot (32).png")

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray , scaleFactor=1.1, minNeighbors= 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w ,y+h), (255, 0, 0), 2)
     
    cv2.imshow('frame ',frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
print(f'Number of faces = {len(faces)}') # ?  
cap.release()
cv2.destroyAllWindows()