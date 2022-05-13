class GoPlus2:

    GOPLUS_ADDR = 0x38
    MOTOR_NUM1 = 0x01
    MOTOR_NUM0 = 0x00
    MOTOR_ADDR_0 = b'\x30'
    MOTOR_ADDR_1 = b'\x31'
    SERVO_ADDR_0 = b'\x00'

    def __init__(self, i2c):
        self.i2c = i2c

    def writeMotorASpeed(self, motorSpeed:int):
        self.i2c.writeto(self.GOPLUS_ADDR, self.MOTOR_ADDR_0 + self.to_bytes(motorSpeed))

    def writeMotorBSpeed(self, motorSpeed:int):
        self.i2c.writeto(self.GOPLUS_ADDR, self.MOTOR_ADDR_1 + self.to_bytes(motorSpeed))

    def writeServo1Angle(self, angle: int):
        self.i2c.writeto(self.GOPLUS_ADDR, self.SERVO_ADDR_0 + angle.to_bytes(1, 'big'))

    # to byte little endian signed
    def to_bytes(self, x):
        return bytes(((x >> 8) & 0xff, x & 0xff))

