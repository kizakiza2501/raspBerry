# -*- coding: utf-8 --
import picamera
import picamera.array
import cv2

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        # カメラの解像度を320*240にセット
        camera.resolution = (320, 240)
        # カメラのフレームを15fpsにセット
        camera.framerate = 15

        # ホワイトバランスをflourescent（蛍光灯）モードにセット
        camera.awb_mode = 'fluorescent'

        while True:
            # stream.arrayにBGRの順で映像データを格納
            camera.capture(stream, 'bgr', use_video_port=True)

            # system.arrayをウィンドウに表示
            cv2.imshow('frame', stream.array)

            # 'q'でアプリケーション終了
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            # streamをリセット
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()