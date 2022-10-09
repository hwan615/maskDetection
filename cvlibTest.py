import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2

#-- 이미지 경로
obj_img = cv2.imread('.static//tesla.jpeg')

#-- detect 함수 불러오기
bbox, label, conf = cv.detect_common_objects(obj_img)

#-- 검출 객체 박스 처리
if label:
    out = draw_bbox(obj_img, bbox, label, conf, write_conf=True)

cv2.imshow("cvlib_img_test", obj_img)

cv2.waitKey()
cv2.destroyAllWindows()