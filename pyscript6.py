from robot_control_class import RobotControl

rc = RobotControl()

rc.stop_robot()
while True:
    d = rc.get_laser(360)
    print(d)

    if (d > 1):
        rc.move_straight()
    else:
        rc.stop_robot()
        l = rc.get_laser(719)
        r = rc.get_laser(1)
        if (l > r):
            rc.turn("counter-clockwise",4,.399)
        else:
            rc.turn("clockwise",4,.399)
        
