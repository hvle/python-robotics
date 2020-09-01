from robot_control_class import RobotControl

rc = RobotControl()
rc.stop_robot()

rc.move_straight_time("forward", 4, 0.15)
rc.turn("counter-clockwise", 4, .5)
rc.move_straight_time("forward", 4, .5)
rc.turn("counter-clockwise", 4, .5)
rc.move_straight_time("forward", 10, .2)