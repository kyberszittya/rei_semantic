robot basic_robot
{
    templates {
        template wheel {
            elements {
                link wheel_axle {
                    body visual viz_wheel_axle { cylinder (0.025, 0.05) }
                    reuse collision viz_wheel_axle
                }
                joint jnt_wheel : wheel_axle->wheel_link: [0,0,1] {
                    type CONTINUOUS
                    control VELOCITY
                    origin (0.0, 0.0, 0.05), (0.0,0.0,0.0)
                }
                link wheel_link {
                    body visual viz_wheel_link { cylinder (0.23, 0.05) }
                    reuse collision viz_wheel_link
                }
            }
        }
        template Caster_wheel {
            elements {
                link caster_root {
                    body visual viz_leftwheel_axle { cylinder (0.025, 0.05) }
                    reuse collision viz_leftwheel_axle
                }
                joint jnt_caster_root : caster_root->caster_wheel_link {
                    type CONTINUOUS
                    origin (0.0, 0.0, 0.05), (0.0,0.0,0.0)
                }
                link caster_wheel_link {
                    body visual viz_caster_wheel_link { cylinder (0.05, 0.1) }
                    reuse collision viz_caster_wheel_link
                }
                joint jnt_caster_tire : caster_wheel_link->caster_tire_link {
                    type CONTINUOUS
                    origin (0.1, 0.0, 0.05), (90.0,0.0,0.0)
                }
                link caster_tire_link {
                    body visual caster_viz_tire_link { cylinder (0.08, 0.04) }
                    reuse collision caster_viz_tire_link
                }
            }
        }
    }
    elements {

        link base_link {
            body visual viz_base_link {
                origin (-0.15, 0.0, 0.1),
                cube (0.5, 0.6, 0.25)
            }
            reuse collision viz_base_link
        }

        use right_wheel: wheel base_link -> (0,-0.3, -0.05),(90.0,0.0,0.0)
        use left_wheel:  wheel base_link -> (0, 0.3, -0.05),(-90.0,0.0,0.0)
        use caster_wheel: Caster_wheel base_link -> (-0.3, 0.0, -0.1),(0.0, 180.0, 0.0)
    }
}