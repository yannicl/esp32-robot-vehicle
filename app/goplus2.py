class GoPlus2:

    GOPLUS_ADDR = 0x38
    MOTOR_NUM1 = 0x01
    MOTOR_NUM0 = 0x00
    MOTOR_ADDR_0 = b'\0x30'

    def __init__(self, i2c):
        self.i2c = i2c

    def writeMotorASpeed(self, motorSpeed:int):
        self.i2c.writeto(self.GOPLUS_ADDR, self.MOTOR_ADDR_0 + motorSpeed.to_bytes(2, 'big'))

