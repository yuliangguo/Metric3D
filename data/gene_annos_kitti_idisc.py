if __name__=='__main__':
    import os
    import os.path as osp
    import numpy as np
    import cv2
    import json

    code_root = '/home/yuliangguo/Projects/Metric3D'
    data_root = 'datasets/kitti_idisc'
    split_file = 'kitti_eigen_test.txt'
    files = []

    with open(os.path.join(code_root, data_root, split_file)) as f:
        for line in f:
            if line.strip().split(" ")[0] == 'None' or line.strip().split(" ")[1] == 'None':
                continue

            rgb_path = osp.join(data_root, line.strip().split(" ")[0])
            depth_path = osp.join(data_root, line.strip().split(" ")[1])

            cam_in = [707.0493, 707.0493, 604.0814, 180.5066]
            depth_scale = 256.
            meta_data = {}
            meta_data['cam_in'] = cam_in
            meta_data['rgb'] = rgb_path
            meta_data['depth'] = depth_path
            meta_data['depth_scale'] = depth_scale
            files.append(meta_data)
    files_dict = dict(files=files)
    
    with open(osp.join(code_root, data_root, 'test_annotations_metric3d.json'), 'w') as f:
        json.dump(files_dict, f)

        