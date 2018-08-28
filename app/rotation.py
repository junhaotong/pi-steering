import RPi.GPIO as GPIO
import time


class Rotation:
    frequency = 50  # 脉冲频率(Hz)
    interval = 0.2  # 步进转动间隔

    '''
        构造函数：
        channel: 舵机信号线所连接的树莓派引脚编号（BCM编码）
        min_theta: 舵机转动的最小角度
        max_theta: 舵机转动的最大角度
        init_theta: 舵机的初始角度
    '''
    def __init__(self, channel, min_angle = 0, max_angle = 180, init_angle = 0):
        self.channel = channel
        self.init_angle = init_angle
        if (min_angle < 0 or min_angle > 180 or min_angle > max_angle):
            self.min_angle = 0
        else:
            self.min_angle = min_angle

        if (max_angle < 0 or max_angle > 180 or max_angle < min_angle):
            self.max_angle = 180
        else:
            self.max_angle = max_angle

    '''
        初始化
    '''
    def setup(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.channel, GPIO.OUT, initial=False)
        self.pwm = GPIO.PWM(self.channel, self.frequency)
        self.pwm.start(self.getDutyCycle(self.init_angle))

        time.sleep(self.interval)

    '''
        角度转换为脉冲占空比
    '''
    def getDutyCycle(self, angle):
        dutyCycle = 2.5 + angle * 10 / 180
        return dutyCycle

    '''
        正转
    '''
    def positiveRotation(self):
        if (self.init_angle + 45 <= self.init_angle):
            self.init_angle += 45
        else:
            self.init_angle = self.max_angle
        self.pwm.ChangeDutyCycle(self.getDutyCycle(self.init_angle))
        time.sleep(self.interval)

    '''
        反转
    '''
    def reverseRotation(self):
        if (self.init_angle - 45 >= 0):
            self.init_angle -= 45
        else:
            self.init_angle = 0
        self.pwm.ChangeDutyCycle(self.getDutyCycle(self.init_angle))
        time.sleep(self.interval)

    '''
        转动到指定角度
    '''
    def specifyRotation(self, angle):
        if (angle < self.min_angle or angle > self.max_angle):
            self.init_angle = self.min_angle
        else:
            self.init_angle = angle
        self.pwm.ChangeDutyCycle(self.getDutyCycle(self.init_angle))
        time.sleep(self.interval)

    '''
        停止舵机
    '''
    def stop(self):
        self.pwm.stop()
