from .rotation import Rotation
import RPi.GPIO as GPIO


class Steering:

    '''
        构造函数
        channelH: 水平舵机的信号通道
        min_angleH: 水平舵机最小转角
        max_angleH: 水平舵机最大转角
        channelV: 垂直舵机的信号通道
        min_angleV: 垂直舵机最小转角
        max_angleV: 垂直舵机最大转角
        init_angleH: 水平舵机初始转角
        init_angleV: 垂直舵机初始转角
    '''
    def __init__(self, channelH, min_angleH, max_angleH,
                 channelV, min_angleV, max_angleV, init_angleH=0, init_angleV=0):
        self.hRotation = Rotation(channelH, min_angleH, max_angleH, init_angleH)
        self.vRotation = Rotation(channelV, min_angleV, max_angleV, init_angleV)

    def setup(self):
        GPIO.setwarnings(False)
        self.hRotation.setup()
        self.vRotation.setup()

    '''
        向上步进转动
    '''
    def up(self):
        self.vRotation.positiveRotation()

    '''
        向下步进转动
    '''
    def down(self):
        self.vRotation.reverseRotation()

    '''
        向左步进转动
    '''
    def left(self):
        self.hRotation.positiveRotation()

    '''
        向右步进转动
    '''
    def right(self):
        self.hRotation.reverseRotation()

    '''
        转动到指定的角度
    '''
    def specify(self, angleH, angleV):
        if (angleH != None):
            self.hRotation.specifyRotation(angleH)

        if (angleV != None):
            self.vRotation.specifyRotation(angleV)

    '''
        停止舵机
    '''
    def cleanup(self):
        self.hRotation.stop()
        self.vRotation.stop()
        GPIO.cleanup()

