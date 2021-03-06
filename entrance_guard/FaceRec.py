import cv2
import face_recognition

from entrance_guard.utils import my_face_recognition
from outer_io.keypad import Keypad

def RecInterface(keypad :Keypad) -> bool:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    auth = False
    while cap.isOpened():
        _, frame_origin = cap.read()
        # cv2.imshow("Access Control System Based on Face Recognition", frame_origin)

        # input_key = cv2.waitKey(1) & 0xFF
        # cv2.waitKey(1)
        input_key = keypad.getKey()
        if input_key == '*':  # 按下*键，进入下面的人脸识别操作
            _, frame_origin = cap.read()
            print("save image")
            cv2.imwrite('entrance_guard/capture/tmp.jpg', frame_origin)
            # frame = frame_origin.copy()

            # 通过 face_locations 得到图像中所有人脸位置
            face_locations = face_recognition.face_locations(frame_origin)
            # for face_location in face_locations:
            #     top, right, bottom, left = face_location  # 得到每张人脸的四个位置信息
                
            #     start = (left, top)
            #     end = (right, bottom)

                # 在图片上绘制矩形框
                # cv2.rectangle(frame, start, end, (0, 0, 255), thickness=2)
                
            # cv2.imshow("Access Control System Based on Face Recognition", frame)

            

            if len(face_locations) == 0:
                print("no face detected")
                # cv2.putText(frame, "no face detected", (0,0), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
            elif len(face_locations) == 1:
                result = my_face_recognition(frame_origin)
                print(result)
                # cv2.putText(frame, str(result), start, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                auth = result
            else:
                print("more than one person in the field")
                # cv2.putText(frame, "more than one person", (0,0), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

            # cv2.imshow("Access Control System Based on Face Recognition", frame)
            # cv2.waitKey(5000)

        elif input_key == '#':  # 按下#键，程序退出
            break
        
        if auth:
            break

    cap.release()  # 释放摄像头
    # cv2.destroyAllWindows()  # 释放并销毁窗口
    return auth

    