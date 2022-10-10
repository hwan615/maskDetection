import cv2
import cvlib as cv

capture = cv2.VideoCapture(0)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    faces, confis = cv.detect_face(frame)
    for face, confi in zip(faces, confis):
        startX, startY = face[0], face[1]
        endX, endY = face[2], face[3]
        textX, textY = endX + 5, startY

        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.putText(frame, "face, {:.3f}".format(confi), (textX, textY), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
