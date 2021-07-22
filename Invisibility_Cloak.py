import cv2
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')
count = 0

# flipping of the background frame
background = np.flip(background, axis=1)

# we are reading from video
while cap.isOpened():
    return_val, frame = cap.read()
    if not return_val:
        break
    count = count + 1

    # flipping of the current frames from the video
    frame = np.flip(frame, axis=1)

    # convert the image - BGR to HSV
    # as we focused on detection of red color

    # converting BGR to HSV for better
    # detection or you can convert it to gray
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kernel to be used for dilation(If Webcam quality is bad, it will fill/correct the bad parts of the frame)
    kernel = np.ones((3, 3), np.uint8)

# You should choose the range of the color you want to use for the mask
# lower and upper range for mask #1
    lower_red = np.array([48, 3, 3])
    upper_red = np.array([48, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    # lower and upper range for mask #2
    lower_red = np.array([90, 3, 3])
    upper_red = np.array([150, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # the above block of code could be replaced with
    # some other code depending upon the color of your cloth
    mask1 = mask1 + mask2

    # Refining the mask corresponding to the detected color
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    # Final output
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisibility Cloak from Harry Potter!", final_output)
    # cv2.resizeWindow(im, (1000, 3000))

    if cv2.waitKey(3) == ord('q'):
        break

    cv2.destroyAllWindows()
