import cv2
import numpy as np

beeVideo = input(str("Name of the video (without extension):"))

reader = cv2.VideoCapture(beeVideo+".mp4")
i = 0

while True:
	ret, img = reader.read()
	
	if i%40 == 0:
		name = "imagesNew/"+beeVideo+str(int(i/40))+'.jpg'
		print(name)
		cv2.imwrite(name, img)
	cv2.imshow("frame", img)
	i += 1

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

reader.close()
cv2.closeAllWindows()


	

