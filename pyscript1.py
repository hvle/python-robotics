from robot_control_class import RobotControl

rc = RobotControl()
rc.stop_robot()
while True:
    a = rc.get_laser(360)
    print("The laser value received was: ", a)
    if a < 1:
        rc.stop_robot()
        break
    else:
        rc.move_straight()