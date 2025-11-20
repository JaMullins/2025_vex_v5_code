# ---------------------------------------------------------------------------- #
#                                                                              #
#   Module:       main.py                                                      #
#   Author:       alancalderonaguilar                                          #
#   Created:      10/23/2025, 3:02:46 PM                                       #
#   Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
import time
import math
from vex import *

# Brain should be defined by default
brain=Brain()
controller = Controller()


REV = False
FWD = True

# Put radio in port 11  
halfMotor = Motor(Ports.PORT9,GearSetting.RATIO_18_1,FWD)

motor1 = Motor(Ports.PORT1,GearSetting.RATIO_6_1,FWD)
motor2 = Motor(Ports.PORT10,GearSetting.RATIO_6_1,REV)
motor3 = Motor(Ports.PORT19,GearSetting.RATIO_6_1,FWD)
motor4 = Motor(Ports.PORT20,GearSetting.RATIO_6_1,REV)

intakeMotor1 = Motor(Ports.PORT7,GearSetting.RATIO_18_1,REV)
intakeMotor2 = Motor(Ports.PORT6,GearSetting.RATIO_18_1,FWD)

intakeSwivel = Motor(Ports.PORT5,GearSetting.RATIO_36_1,FWD)

inertial = Inertial(Ports.PORT8)
inertial.calibrate()
wait(200,MSEC)


spinning = False
swivelling = False


def testDiagonol():
    global spinning, swivelling
    # Goal for this is to test how well the half motor can keep up with 1-2 regular motors if it was a supplemental sideways force
    # This would allow for diagonol movement that mimicks true X-drive
    while not time.sleep(0.2):
        sideways_motion = (controller.axis4.position())*2
        forward_motion = controller.axis3.position()
        forward_motion_decimal = float(forward_motion/100)
        rotational_multiplier = .75 + (.25 * (1 - forward_motion_decimal))
        rotational_motion = (controller.axis1.position() * rotational_multiplier)/2

        # Vertical right stock maybe for swivelling in both directions with full control, otherwise would need 2 buttons or a limit switcher.

        halfMotor.set_velocity(sideways_motion,PERCENT)
        halfMotor.spin(FORWARD)
        motor1.set_velocity((forward_motion + rotational_motion), PERCENT)
        motor1.spin(FORWARD)
        motor2.set_velocity((forward_motion - rotational_motion), PERCENT)
        motor2.spin(FORWARD)
        motor3.set_velocity((forward_motion + rotational_motion), PERCENT)
        motor3.spin(FORWARD)
        motor4.set_velocity((forward_motion - rotational_motion), PERCENT)
        motor4.spin(FORWARD)

        intakeMotor2.set_velocity(100,PERCENT)
        intakeMotor1.set_velocity(100,PERCENT)

        intakeSwivel.set_velocity(35,PERCENT)


        if spinning:
            intakeMotor1.spin(FORWARD)
            intakeMotor2.spin(FORWARD)
        elif not spinning:
            intakeMotor2.stop()
            intakeMotor1.stop()

        if swivelling:
            intakeSwivel.spin(REVERSE)
        elif not spinning:
            intakeSwivel.stop()

        


        def test():
            global spinning
            spinning = not spinning


        def swivel():
            global swivelling
            swivelling = not swivelling
            
            
        if controller.buttonR1.pressing():
            test()
        if controller.buttonR2.pressing():
            swivel()





def driverControlled():


    while not time.sleep(0.2):

        forward_motion_decimal = float(controller.axis3.position()/100)
        rotational_motion = float(controller.axis4.position()/100)

        net_left = (forward_motion_decimal)
        net_right = (rotational_motion)
        

        brain.screen.clear_line()
        brain.screen.print(str(net_right),str(net_left))
        brain.screen.new_line()
        

        """if is_rev:
            forward_motion *= -1
           
        left_motors.set_velocity((forward_motion + rotational_motion), PERCENT)
        right_motors.set_velocity((forward_motion - rotational_motion), PERCENT)
        left_motors.spin(FORWARD)
        right_motors.spin(FORWARD)"""




#driverControlled()
testDiagonol()