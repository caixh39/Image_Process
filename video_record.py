# encoding: utf-8

import cv2
import os


def videoStreamRecorder(camera_id, save_path):
    fps = 20
    resolution = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    camera = cv2.VideoCapture(camera_id)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    recorder = cv2.VideoWriter()
    recorder_cnt = 1

    record_flag = False
    while True:
        ret, frame = camera.read()
        frame_copy = frame.copy()
        if record_flag:
            recorder.write(frame)
            cv2.putText(frame, "Recoding", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.imshow("Video Recorder", frame)

        key = cv2.waitKey(1000 / fps) & 0xff
        # 开始录制视频
        if key == ord("r"):
            save_name = os.path.join(save_path, "{}_{}.avi".format("record_video", recorder_cnt))
            recorder.open(save_name, fourcc, fps, resolution)
            recorder_cnt += 1
            record_flag = True
            print "Start recording..."
        # 停止录制视频
        elif key == ord("s"):
            record_flag = False
            print "Stop recording..."

            # 识别最后一帧的情绪
            # image_bytes = cv2.imencode(".jpg", frame_copy)[1].tostring()
            # _, fpp_reg_image = imageRecognized(frame_copy, image_bytes, "Face++ API")
            # _, ms_reg_image = imageRecognized(fpp_reg_image, image_bytes, "Microsoft API")
            # recorder.write(ms_reg_image)
            # cv2.imshow("Video Recorder", ms_reg_image)
            recorder.release()

            # 暂停更新帧
            while True:
                go_key = cv2.waitKeyEx(1) & 0xff
                if go_key == ord("g"):
                    break
        elif key == ord("q"):
            print "Exit"
            break

    camera.release()
    recorder.release()
    cv2.destroyAllWindows()
