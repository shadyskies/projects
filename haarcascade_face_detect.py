import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to add image")
ap.add_argument("-c", "--cascade", type=str, default="haarcascade_frontalface_default.xml",
                help="path to haar cascade face detector")
args = vars(ap.parse_args())

# loading haar cascade
print(f"[INFO] Loading face detector")
detector = cv2.CascadeClassifier(args["cascade"])

# loading the image
print(f"[INFO] Loading image..")
image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detecting faces
print(f'[INFO] Detecting faces in image')
rects = detector.detectMultiScale(gray_img, scaleFactor=1.05,
                                  minNeighbors=10, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
print(f"{len(rects)} faces detected!")

# draw rectangles
for (x, y, u, v) in rects:
    cv2.rectangle(image, (x, y), (x + u, y + v), (0, 255, 0), 2)

cv2.imshow("Image", image)
cv2.waitKey(0)
