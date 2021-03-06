from machine import Pin, SoftI2C, WDT
import time
import json
from app.radio import Radio
r = Radio()

wdt = WDT(timeout=60000)  # enable it with a timeout of 60s

while True:

    try:
        r.send("Hello")    

        i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
        i2c.scan()

        #from third_party import VL53L0X
        #tof = VL53L0X.VL53L0X(i2c)
        #tof.set_Vcsel_pulse_period(tof.vcsel_period_type[0], 18)
        #tof.set_Vcsel_pulse_period(tof.vcsel_period_type[1], 14)

        from app.goplus2 import GoPlus2
        motor = GoPlus2(i2c)

        from app.TCS34725 import TCS34725

        colorSensor = TCS34725(i2c)

        while True:
            wdt.feed()
            data = r.read()
            print(data)
            y = json.loads(data)
            if "motorA" in y:
                print(y["motorA"])
                motor.writeMotorASpeed(y["motorA"])
            else:
                motor.writeMotorASpeed(0)
            if "motorB" in y:
                motor.writeMotorBSpeed(y["motorB"])
            else:
                motor.writeMotorBSpeed(0)
            
            #tof.start()
            #dist = tof.read()
            #tof.stop()
            #r.send(json.dumps({
            #'distance': dist
            #}))

            data = colorSensor.read(raw=True)
            r.send(json.dumps({
            'color': data
            }))

    except Exception as err:
        
        r.send(json.dumps({
            'type': type(err),
            'args': err.args
        }))
