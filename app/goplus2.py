class GoPlus2:

    MOTOR_NUM1 = 0x01
    MOTOR_NUM0 = 0x00
    MOTOR_ADDR = 0x30

    def __init__(self, i2c):
        self.i2c = i2c

    def writeMotorASpeed(self, motorSpeed:int):
        self.i2c.writeto(self.MOTOR_ADDR, motorSpeed.to_bytes(2, 'big'))

