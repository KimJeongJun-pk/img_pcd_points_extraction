import cv2

points_2d = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        points_2d.append((x,y))
        print(f"Clicked point: [{x}, {y}]")
        
image = cv2.imread('/home/kjj/rosbag/rosbag_250804/img_pcd_250804/camera_images/image_0070.png')
cv2.imshow('Image', image)
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllwindows()

print(f"selected points:[{points_2d[0]}, {points_2d[1]}]", points_2d)