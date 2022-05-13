from machine import Pin, SoftI2C
import time
import json
from app.radio import Radio
r = Radio()

try:
    r.send("Hello")    

    i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
    i2c.scan()

    #from third_party import VL53L0X
    #tof = VL53L0X.VL53L0X(i2c)

    #tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)

    #tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)


    #while True:
    # Start ranging
    #tof.start()
    #tof.read()
    #print(tof.read())
    #tof.stop()

    from app.goplus2 import GoPlus2
    motor = GoPlus2(i2c)

    while True:
        data = r.read()
        print(data)
        y = json.loads(data)
        if "motorA" in y:
            print(y["motorA"])
            motor.writeMotorASpeed(y["motorA"])
        if "motorB" in y:
            motor.writeMotorBSpeed(y["motorB"])

except Exception as err:
    
    r.send(json.dumps({
        'type': type(err),
        'args': err.args
    }))