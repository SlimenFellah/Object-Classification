import cv2
import cvzone


cap = cv2.VideoCapture(1)
myClassifier = cvzone.Classifier('./myModel/keras_model.h5','./myModel/labels.txt')
fpsReader = cvzone.FPS()
while True:
    success, img= cap.read()
    prediction, index = myClassifier.getPrediction(img, scale=1)
    # print(prediction,index)
    fps, img = fpsReader.update(img,pos=(50,50))
    print(fps)
    cv2.imshow("Image",img)
    cv2.waitKey(1)