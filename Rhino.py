from hub import port
import motor_pair
import runloop
import force_sensor

async def main():

    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
    motor_pair.move(motor_pair.PAIR_1, 0)

    await runloop.until(lambda: force_sensor.pressed(port.C))
    
    if force_sensor.pressed(port.C) == True:
        motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
