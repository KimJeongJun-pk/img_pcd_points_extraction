img_feature.py : 이미지에서 선택한 점의 좌표를 출력
- 이미지 파일 경로 수정해야함

pcd_feature.py : 포인트 클라우드에서 선택한 점의 좌표를 출력
- pcd 파일 경로 수정해야함

lidar-camera_calibration.py : img, pcd에서 추출한 좌표(8개 이상)을 기준으로 외부 파라미터 추정 
- 카메라 내부 파라미터 수정
- object_points : pcd에서 추출한 좌표 입력(x,y,z)
- image_points : img에서 추출한 좌표 입력(x,y)
