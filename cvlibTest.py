import cvlib as cv
import cv2
import sys
import os

img = cv2.imread(sys.argv[1])

faces, confis = cv.detect_face(img)

print(faces)
print(confis)

for face, confi in zip(faces, confis):
	startX, startY = face[0], face[1]
	endX, endY = face[2], face[3]
	textX, textY = endX + 5, startY

	cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 2)
	cv2.putText(img, "face, {:.3f}".format(confi), (textX, textY), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("cvlibTest", img)
cv2.waitKey()
cv2.imwrite("./static/cvlibTestResult3.jpg", img)
cv2.destroyAllWindows()