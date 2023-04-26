from cv2 import cv2
import check_image

image_path = "odp-id-w2.jpg"

correct_answers = [1, 2, 0, 0, 3, 2, 3, 1, 3, 0, 3, 1]

zdj = check_image.CheckImage(image_path, correct_answers)
zdj.check_image()

print(zdj.percentage)
cv2.imshow("Finalne polaczenie ", zdj.img)
cv2.waitKey(0)
