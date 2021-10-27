from tkinter import messagebox

import cv2
import face_recognition

from utils import my_face_recognition, show_info


def get_images():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, frame_origin = cap.read()
        frame = frame_origin.copy()

        # 通过 face_locations 得到图像中所有人脸位置
        face_locations = face_recognition.face_locations(frame)
        for face_location in face_locations:
            top, right, bottom, left = face_location  # 得到每张人脸的四个位置信息

            start = (left, top)
            end = (right, bottom)

            # 在图片上绘制矩形框
            cv2.rectangle(frame, start, end, (0, 0, 255), thickness=2)

        cv2.imshow("Access Control System Based on Face Recognition", frame)

        input_key = cv2.waitKey(1) & 0xFF
        if input_key == ord('r'):  # 按下r键，进入下面的人脸识别操作




            if len(face_locations) == 0:
                print("摄像头未识别到人脸")
                show_info("摄像头未识别到人脸")
            elif len(face_locations) == 1:
                result = my_face_recognition(frame_origin)
                print(result)
                show_info(str(result))
            else:
                print("摄像头视野中人脸不止一个，请稍后再试")
                show_info("摄像头视野中人脸不止一个，请稍后再试")

        elif input_key == ord('q'):  # 按下q键，程序退出
            break

    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 释放并销毁窗口


if __name__ == '__main__':
    get_images()
