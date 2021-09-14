# Copyright @ 2019 Alibaba. All rights reserved.
# Created by ruhuan on 2019.09.09
""" python demo usage about MNN API """
from __future__ import print_function
import numpy as np
import MNN
import cv2

INPUT_SIZE = 320
CLASS_NUM = 20


def inference():
    """ inference mobilenet_v1 using a specific picture """
    interpreter = MNN.Interpreter("../model/yolofastest.mnn")
    interpreter.setCacheFile('.tempcache')
    config = {}
    # config['precision'] = 'low'

    # # create session
    # runtimeinfo, exists = MNN.Interpreter.createRuntime((config,))
    # print(runtimeinfo, exists)
    # session = interpreter.createSession(config, runtimeinfo)
    session = interpreter.createSession(config)

    # show session info
    # print('memory_info: %fMB' % interpreter.getSessionInfo(session, 0))
    # print('flops_info: %fM' % interpreter.getSessionInfo(session, 1))
    # print('backend_info: %d' % interpreter.getSessionInfo(session, 2))

    input_tensor = interpreter.getSessionInput(session)
    image = cv2.imread("../1.jpg")
    # cv2 read as bgr format
    # image = image[..., ::-1]
    # change to rgb format
    image = cv2.resize(image, (INPUT_SIZE, INPUT_SIZE))
    # #resize to mobile_net tensor size
    # image = image - (103.94, 116.78, 123.68)
    # image = image * (0.017, 0.017, 0.017)
    # #preprocess it
    # image = image.transpose((2, 0, 1))
    # #change numpy data type as np.float32 to match tensor's format
    # image = image.astype(np.float32)
    # cv2 read shape is NHWC, Tensor's need is NCHW,transpose it
    tmp_input = MNN.Tensor((INPUT_SIZE, INPUT_SIZE, 3), MNN.Halide_Type_Float, \
                           image, MNN.Tensor_DimensionType_Tensorflow)
    input_tensor.copyFrom(tmp_input)
    interpreter.runSession(session)

    scores = "layer125-conv"
    scores2 = "layer115-conv"

    output_tensor0 = interpreter.getSessionOutput(session, scores)
    output_tensor1 = interpreter.getSessionOutput(session, scores2)

    # constuct a tmp tensor and copy/convert in case output_tensor is nc4hw4
    # tmp_output = MNN.Tensor((1, 1001), MNN.Halide_Type_Float, np.ones([1, 1001]).astype(np.float32), MNN.Tensor_DimensionType_Tensorflow)
    tmp_output0 = MNN.Tensor((1, 75, 20, 20), MNN.Halide_Type_Float, \
                             np.ones([1, 75, 20, 20]).astype(np.float32), MNN.Tensor_DimensionType_Tensorflow)
    tmp_output1 = MNN.Tensor((1, 75, 10, 10), MNN.Halide_Type_Float, \
                             np.ones([1, 75, 10, 10]).astype(np.float32), MNN.Tensor_DimensionType_Tensorflow)

    output_tensor0.copyToHostTensor(tmp_output0)
    output_tensor1.copyToHostTensor(tmp_output1)
    print("expect 983")
    print("output belong to class: {}".format(np.argmax(tmp_output0.getData())))
    print("output belong to class: {}".format(np.argmax(tmp_output1.getData())))


if __name__ == "__main__":
    inference()
