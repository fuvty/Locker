import os
import face_recognition

from numpy import ndarray


def my_face_recognition(image_to_detect: ndarray) -> bool:
    # 输入为一幅图像，保证只有一个人脸，输出结果为是否有门禁权限

    known_face_encodings = face_recognition.face_encodings(image_to_detect)

    for root, _, files in os.walk(os.getcwd() + "\\dataset"):
        # root 表示当前正在访问的文件夹路径, _ 表示该文件夹下的子目录名list, files 表示该文件夹下的文件list

        # 遍历文件
        for file in files:
            file_path = os.path.join(root, file)
            # 加载一张单人照
            dataset_image = face_recognition.load_image_file(file_path)

            # face_encodings返回的是列表类型，我们只需要拿到第一个人脸编码即可
            compare_face_encodings = face_recognition.face_encodings(dataset_image)[0]

            # 注意第二个参数，只能是答案个面部特征编码，不能传列表
            matches = face_recognition.compare_faces(known_face_encodings, compare_face_encodings)
            if matches[0]:
                return True

    return False