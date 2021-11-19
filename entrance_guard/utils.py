import os
import cv2
import face_recognition

from numpy import ndarray


def my_face_recognition(image_to_detect: ndarray) -> bool:
    # 输入为一幅图像，保证只有一个人脸，输出结果为是否有门禁权限

    known_face_encodings = face_recognition.face_encodings(image_to_detect)
    # print(list(os.getcwd() + "/entrance_guard/dataset"))

    for root, _, files in os.walk(os.getcwd() + "/entrance_guard/dataset"):
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
            print(file)
            print(matches)
            if matches[0]:
                return True

    return False


def save_image():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, frame = cap.read()
        cv2.imshow("press y to save image", frame)

        input_key = cv2.waitKey(1) & 0xFF
        if input_key == ord('y'):  # 按下y键，进入下面的人脸识别操作
            filename = "dataset/" + str(len(list(os.walk(os.getcwd() + "\\dataset"))[0][2]) + 1) + ".jpg"
            cv2.imwrite(filename=filename, img=frame)

            cv2.waitKey(3000)
            cap.release()  # 释放摄像头
            cv2.destroyAllWindows()  # 释放并销毁窗口
            break
