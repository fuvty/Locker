import cv2
import face_recognition

from utils import my_face_recognition

def RecInterface() -> bool:
    cap = cv2.VideoCapture(0)
    auth = False
    while cap.isOpened():
        _, frame_origin = cap.read()
        cv2.imshow("Access Control System Based on Face Recognition", frame_origin)

        input_key = cv2.waitKey(1) & 0xFF
        if input_key == ord('r'):  # 按下r键，进入下面的人脸识别操作
            
            frame = frame_origin.copy()

            # 通过 face_locations 得到图像中所有人脸位置
            face_locations = face_recognition.face_locations(frame_origin)
            for face_location in face_locations:
                top, right, bottom, left = face_location  # 得到每张人脸的四个位置信息
                
                start = (left, top)
                end = (right, bottom)

                # 在图片上绘制矩形框
                cv2.rectangle(frame, start, end, (0, 0, 255), thickness=2)
                
            # cv2.imshow("Access Control System Based on Face Recognition", frame)

            

            if len(face_locations) == 0:
                print("摄像头未识别到人脸")
                cv2.putText(frame, "no face detected", (0,0), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
            elif len(face_locations) == 1:
                result = my_face_recognition(frame_origin)
                print(result)
                cv2.putText(frame, str(result), start, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                auth = True
            else:
                print("摄像头视野中人脸不止一个，请稍后再试")
                cv2.putText(frame, "more than one person", (0,0), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

            cv2.imshow("Access Control System Based on Face Recognition", frame)
            cv2.waitKey(5000)

        elif input_key == ord('q'):  # 按下q键，程序退出
            break
        
        if auth:
            break

    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 释放并销毁窗口
    return auth



def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        _, frame_origin = cap.read()
        cv2.imshow("Access Control System Based on Face Recognition", frame_origin)

        input_key = cv2.waitKey(1) & 0xFF
        if input_key == ord('r'):  # 按下r键，进入下面的人脸识别操作
            
            frame = frame_origin.copy()

            # 通过 face_locations 得到图像中所有人脸位置
            face_locations = face_recognition.face_locations(frame_origin)
            for face_location in face_locations:
                top, right, bottom, left = face_location  # 得到每张人脸的四个位置信息
                
                start = (left, top)
                end = (right, bottom)

                # 在图片上绘制矩形框
                cv2.rectangle(frame, start, end, (0, 0, 255), thickness=2)
                
            # cv2.imshow("Access Control System Based on Face Recognition", frame)

            

            if len(face_locations) == 0:
                print("摄像头未识别到人脸")
                cv2.putText(frame, "no face detected", (0,0), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)
            elif len(face_locations) == 1:
                result = my_face_recognition(frame_origin)
                print(result)
                cv2.putText(frame, str(result), start, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                print("摄像头视野中人脸不止一个，请稍后再试")
                cv2.putText(frame, "more than one person", (0,0), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

            cv2.imshow("Access Control System Based on Face Recognition", frame)

            cv2.waitKey(5000)

        elif input_key == ord('q'):  # 按下q键，程序退出
            break

    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 释放并销毁窗口


if __name__ == '__main__':
    main()
