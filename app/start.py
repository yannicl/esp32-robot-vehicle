from machine import Pin, SoftI2C
import time
import json

try:

    i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
    i2c.scan()

    from third_party import VL53L0X
    tof = VL53L0X.VL53L0X(i2c)

    tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)

    tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)


    #while True:
    # Start ranging
    tof.start()
    tof.read()
    print(tof.read())
    tof.stop()

    from app.goplus2 import GoPlus2
    motor = GoPlus2(i2c)
    motor.writeMotorASpeed(10000)
    motor.writeServo1Angle(50)
    time.sleep(4)
    motor.writeServo1Angle(0)
    motor.writeMotorASpeed(0)
    time.sleep(4)
    motor.writeServo1Angle(150)
    motor.writeMotorASpeed(-10000)
    time.sleep(4)
    motor.writeServo1Angle(0)
    motor.writeMotorASpeed(0)

except Exception as err:
    from app.radio import Radio
    r = Radio()
    r.send(json.dumps(err))