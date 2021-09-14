import time
import picamera
import numpy as np
import cv2

# fourcc(Four-Character-Codes)：独立显示视频数据流格式的四字符编码
# 定义视频编码器为XVID
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 设定输出视频的名称和格式，以及帧率和分辨率
# out = cv2.VideoWriter('output1.mp4', fourcc, 24.0, (640, 480))

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 60
    time.sleep(2)
    while True:
        output = np.empty((640 * 480 * 3,), dtype=np.uint8)
        camera.capture(output, 'rgb')

        # gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)  # 灰度视频流的参数设置
        output = output.reshape((480, 640, 3))
        # output = output[:100, :100, :]
        # out.write(output)  # 将视频保存
        cv2.imshow('frame', output)  # 显示原视频流
        # cv2.imshow('gray', gray)  # 显示灰度格式的视频流
        if cv2.waitKey(1) == ord('q'):  # 按下q后退出条件成立
            break

    # out.release()
    cv2.destroyAllWindows()
