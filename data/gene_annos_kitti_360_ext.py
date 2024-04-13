if __name__=='__main__':
    import os
    import os.path as osp
    import numpy as np
    import cv2
    import json


    CAM_INTRINSIC = {
        "02": np.array(
            [
                [1.33632e+03, 0.000000e00, 7.16943e+02],
                [0.000000e00, 1.33578e+03, 7.05764e+02],
                [0.000000e00, 0.000000e00, 1.000000e00],
            ]
        ),
        "03": np.array(
            [
                [1.48543e+03, 0.000000e00, 6.98883e+02],
                [0.000000e00, 1.48494e+03, 6.98145e+02],
                [0.000000e00, 0.000000e00, 1.000000e00],
            ]
        )
    }

    code_root = '/home/yuliangguo/Projects/Metric3D'
    data_root = 'datasets/KITTI-360'
    split_file = 'kitti360_val_fisheye_undistort_f175.txt'
    files = []

    with open(os.path.join(code_root, data_root, split_file)) as f:
        for line in f:
            if line.strip().split(" ")[0] == 'None' or line.strip().split(" ")[1] == 'None':
                continue

            rgb_path = osp.join(data_root, line.strip().split(" ")[0])
            depth_path = osp.join(data_root, line.strip().split(" ")[1])

            cam_in = [175, 175, 700, 700]
            
            depth_scale = 256.
            meta_data = {}
            meta_data['cam_in'] = cam_in
            meta_data['rgb'] = rgb_path
            meta_data['depth'] = depth_path
            meta_data['depth_scale'] = depth_scale
            files.append(meta_data)
    files_dict = dict(files=files)
    
    with open(osp.join(code_root, data_root, 'test_annotations_fisheye_undistort_f175_metric3d.json'), 'w') as f:
        json.dump(files_dict, f)


    #####################################################################################################################
    
    code_root = '/home/yuliangguo/Projects/Metric3D'
    data_root = 'datasets/KITTI-360'
    split_file = 'kitti360_val_fisheye_undistort_f350.txt'
    files = []

    with open(os.path.join(code_root, data_root, split_file)) as f:
        for line in f:
            if line.strip().split(" ")[0] == 'None' or line.strip().split(" ")[1] == 'None':
                continue

            rgb_path = osp.join(data_root, line.strip().split(" ")[0])
            depth_path = osp.join(data_root, line.strip().split(" ")[1])

            cam_in = [350, 350, 700, 700]
            
            depth_scale = 256.
            meta_data = {}
            meta_data['cam_in'] = cam_in
            meta_data['rgb'] = rgb_path
            meta_data['depth'] = depth_path
            meta_data['depth_scale'] = depth_scale
            files.append(meta_data)
    files_dict = dict(files=files)
    
    with open(osp.join(code_root, data_root, 'test_annotations_fisheye_undistort_f350_metric3d.json'), 'w') as f:
        json.dump(files_dict, f)
        

    #####################################################################################################################
    
    code_root = '/home/yuliangguo/Projects/Metric3D'
    data_root = 'datasets/KITTI-360'
    split_file = 'kitti360_val_fisheye_undistort_f700.txt'
    files = []

    with open(os.path.join(code_root, data_root, split_file)) as f:
        for line in f:
            if line.strip().split(" ")[0] == 'None' or line.strip().split(" ")[1] == 'None':
                continue

            rgb_path = osp.join(data_root, line.strip().split(" ")[0])
            depth_path = osp.join(data_root, line.strip().split(" ")[1])

            cam_in = [700, 700, 700, 700]
            
            depth_scale = 256.
            meta_data = {}
            meta_data['cam_in'] = cam_in
            meta_data['rgb'] = rgb_path
            meta_data['depth'] = depth_path
            meta_data['depth_scale'] = depth_scale
            files.append(meta_data)
    files_dict = dict(files=files)
    
    with open(osp.join(code_root, data_root, 'test_annotations_fisheye_undistort_f700_metric3d.json'), 'w') as f:
        json.dump(files_dict, f)
        
        
    #####################################################################################################################
    
    code_root = '/home/yuliangguo/Projects/Metric3D'
    data_root = 'datasets/KITTI-360'
    split_file = 'kitti360_val_fisheye_erp.txt'
    files = []

    with open(os.path.join(code_root, data_root, split_file)) as f:
        for line in f:
            if line.strip().split(" ")[0] == 'None' or line.strip().split(" ")[1] == 'None':
                continue

            rgb_path = osp.join(data_root, line.strip().split(" ")[0])
            depth_path = osp.join(data_root, line.strip().split(" ")[1])

            # ERP suppose to have no focal length
            cam_in = [445.63, 445.63, 700, 700]
            
            depth_scale = 256.
            meta_data = {}
            meta_data['cam_in'] = cam_in
            meta_data['rgb'] = rgb_path
            meta_data['depth'] = depth_path
            meta_data['depth_scale'] = depth_scale
            files.append(meta_data)
    files_dict = dict(files=files)
    
    with open(osp.join(code_root, data_root, 'test_annotations_fisheye_erp_metric3d.json'), 'w') as f:
        json.dump(files_dict, f)