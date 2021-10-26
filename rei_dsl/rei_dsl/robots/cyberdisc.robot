robot cyberdisc
{
    templates {
        template motor_module {
            elements {
                link motor_root {
                    body visual viz_motor_root { cube (0.08, 0.04, 0.03) }
                    reuse collision viz_motor_root
                }
                joint jnt_motor : motor_root->motor_axle {
                    type FIXED
                    origin (0.04, 0.0, 0.0), (0.0, 90.0, 0.0)
                }
                link motor_axle {
                    body visual viz_axle { cylinder (0.005, 0.07)}
                    reuse collision viz_axle
                }
                joint jnt_motor_wheel : motor_axle->wheel_link: [0,0,1] {
                    type CONTINUOUS
                    control VELOCITY
                    origin (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)
                }
                link wheel_link {
                    body visual viz_wheel_link { cylinder (0.04, 0.02)}
                    reuse collision viz_wheel_link
                }
            }
        }
    }
    elements {
        link base_link {
            body visual viz_disc_body {
                cylinder(0.25, 0.05)
            }
            reuse collision viz_disc_body
        }

        use motor_0: motor_module base_link -> (0.1, 0.1, 0.0),(0.0,0.0,90.0)
        use motor_1: motor_module base_link -> (-0.1, 0.1, 0.0),(0.0,0.0,90.0)
        use motor_2: motor_module base_link -> (-0.1, -0.1, 0.0),(0.0,0.0,-90.0)
        use motor_3: motor_module base_link -> (0.1, -0.1, 0.0),(0.0,0.0,-90.0)
    }
}