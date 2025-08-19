import numpy as np
import cv2

camera_matrix = np.array([
   [   644.81611,    0.     , 642.02089],
   [     0.     ,  646.24805, 361.00486],
   [     0.     ,    0.     ,    1.    ]
])
dist_coeffs = np.array([-0.036693, 0.031981, 0.000975, -0.000173, 0.000000])

object_points = np.array([
[-0.32480672,  1.28309679,  0.42783689],
[-0.04475839,  1.30194736,  0.37997246],
[-0.0778995 ,  1.35054767,  0.19657543],
[-0.36064959,  1.32586169,  0.24093179],
[0.12152027 ,  1.1739397 ,  0.39951798],
[0.34654385 ,  0.95893258,  0.3005408 ],
[0.34586641 ,  1.07278407,  0.1148899 ],
[0.10329854 ,  1.17772698,  0.19363073]
], dtype = np.float32)

image_points = np.array([
[490, 213],
[636, 243],
[615, 344],
[472, 314],
[710, 201],
[879, 216],
[859, 355],
[699, 320]
], dtype = np.float32)

success, rvec, tvec = cv2.solvePnP(
    objectPoints = object_points,
    imagePoints = image_points, 
    cameraMatrix = camera_matrix,
    distCoeffs = dist_coeffs,
    flags = cv2.SOLVEPNP_ITERATIVE
)

if success:
    print("rvec (회전벡터):\n", rvec)
    print("tvec (평행 이동 벡터):\n", tvec)
    
    R, _ = cv2.Rodrigues(rvec)
    print("R (회전 행렬):\n", R)
    
    extrinsic = np.hstack((R, tvec))
    print("Extrinsic Matrix (R| t):\n", extrinsic)
    
else:
    print("PnP 실패")