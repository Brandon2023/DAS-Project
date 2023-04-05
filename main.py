#Hello DAS Committee 
#As for my focus area computer programming I have included this project. This project has exceeded expectations because I self taught more complex programming features.
#I have leared advanced algorthims, complex data structure, learning how computers see the world using OpenCV and how to use Haar Cascade for image processing and classification.
#Thank you for reading this. 


import cv2 as cv

cam = cv.VideoCapture(0)
eye_data = cv.CascadeClassifier('haarcascade_eye.xml')
nose_data = cv.CascadeClassifier('haarcascade_nose.xml')

if not cam.isOpened():
    print("Camera not working")
    exit()

def eye(frame):
    frame_colour = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    box_eye = eye_data.detectMultiScale(frame_colour)
    for (x,y,w,h) in box_eye:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv.putText(frame, 'test', (x, y-10), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,255,0), 2)
        print("eyes detected")

def nose(frame):
    frame_colour = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    box_nose = nose_data.detectMultiScale(frame_colour)
    for (x,y,w,h) in box_nose:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,0,225), 2)
        cv.putText(frame, 'test 2', (x, y-10), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0,255,0), 2)
        print("nose detected")

       
while True:
    ret, frame = cam.read()
    eye(frame)
    nose(frame)

    if ret is None:
        print("no stream") 
        break

    cv.imshow('eye detector', frame)
    if cv.waitKey(1) == ord('w'):
        break

cam.release()
cv.destroyAllWindows()