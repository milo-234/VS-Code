import cv2
image1 = cv2.imread('Android.png')
image2=cv2.imread('Backgorund.jpg')
AddedImage=cv2.add(image1,image2)
SubImage=cv2.subtract(image1,image2)
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Added Image',AddedImage)
cv2.imshow('Subtracted Image', SubImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
