import cv2
# image = cv2.imread("C:\\Users\\ADMIN\\Pictures\\Screenshots\\Screenshot (32).png")
# cv2.imshow("cat",image)
# cv2.waitKey()
vid = cv2.VideoCapture("C:\\Users\\ADMIN\\Desktop\\lol\\VID-20230306-WA0000.mp4")
while True:
    isTrue,frame = vid.read()
    cv2.imshow('frame',frame)
    # cv2.reactangle()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
