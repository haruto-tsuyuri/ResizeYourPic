import cv2
import glob
import os
import numpy as np
import sys

# 日本語ファイル名も読見とれるようにするためにOverride
def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None


# 日本語ファイル名も読見とれるようにするためにOverride
def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


size_dict = {"640x640": [640, 640], "400x400": [400, 400]}
file_type = 'jpg'
dir_path = 'C:/test222/'
for path in glob.glob(os.path.join(dir_path, f'*.{file_type}')):
    basename = os.path.basename(path)
    folder_name = os.path.splitext(basename)[0]
    os.mkdir(dir_path + folder_name)
    img = imread(path)
    file_num = input(f"{folder_name} の附番を入力してください")
    for size_folder in size_dict.keys():
        os.mkdir(dir_path + folder_name + "/" + size_folder)
        sizing_dir_path = dir_path + folder_name + "/" + size_folder
        print(sizing_dir_path)
        for i in range(0, 11):
            imwrite(sizing_dir_path + "/" + file_num + "0" + str(i) + ".jpg", img)