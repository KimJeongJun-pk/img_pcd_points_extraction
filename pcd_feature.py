import open3d as o3d
import numpy as np

pcd_path = "/home/kjj/rosbag/rosbag_250804/img_pcd_250804/lidar_points/lidar_0070.pcd"
pcd = o3d.io.read_point_cloud(pcd_path)

vis = o3d.visualization.VisualizerWithEditing()
vis.create_window()
vis.add_geometry(pcd)
render_option = vis.get_render_option()
render_option.point_size = 3
vis.run()
vis.destroy_window()

picked_points_indices = vis.get_picked_points()

points = np.asarray(pcd.points)

selected_points = []
for idx in picked_points_indices:
    selected_points.append(points[idx])
    print(f"Selected point {idx}: [{points[idx]}]")

print("All selected points : ")
for pt in selected_points:
    print(f"[{pt}]")