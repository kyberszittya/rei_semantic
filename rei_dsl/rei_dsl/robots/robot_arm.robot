robot basic_anthropomorph
{

    elements {

        link base_link {
            inertia 10.0
            body visual viz_base_link {
                origin (0, 0.0, 0.15),
                cylinder (0.2, 0.3)
            }
            reuse collision viz_base_link
        }

        joint jnt_base_shoulder: base_link ->shoulder_link: [0,0,1]  {
            type REVOLUTE
            limit [-180;180]
            origin (0.0, 0.0, 0.1),(0.0,0.0,0.0)
        }

        link shoulder_link {
            body visual viz_shoulder_link {
                origin (0, 0.0, 0.3),
                cylinder (0.15, 0.1)
            }
            reuse collision viz_shoulder_link
        }

        joint jnt_shoulder_arm: shoulder_link->arm_link: [1,0,0]  {
            type REVOLUTE
            limit [-120;120]
            origin (0.0, 0.0, 0.15),(0.0,0.0,0.0)
        }

        link arm_link {
            body visual viz_arm_link {
                origin (0, 0.0, 0.3),
                cylinder (0.1, 0.6)
            }
            reuse collision viz_arm_link
        }

        joint jnt_arm_wrist: arm_link->wrist_link1: [1,0,0]  {
            type REVOLUTE
            limit [-120;120]
            origin (0.0, 0.0, 0.6),(0.0,0.0,0.0)
        }

        link wrist_link1 {
            body visual viz_wrist_link1 {
                origin (0, 0.0, 0.1),
                cylinder (0.1, 0.1)
            }
            reuse collision viz_wrist_link1
        }

        joint jnt_wrist1_wrist2: wrist_link1->wrist_link2: [0,0,1]  {
            type REVOLUTE
            limit [-120;120]
            origin (0.0, 0.0, 0.075),(0.0,0.0,0.0)
        }

        link wrist_link2 {
            body visual viz_wrist_link2 {
                origin (0, 0.0, 0.15),
                cylinder (0.1, 0.1)
            }
            reuse collision viz_wrist_link2
        }

        joint jnt_wrist2_wrist3: wrist_link2->wrist_link3: [1,0,0]  {
            type REVOLUTE
            limit [-120;120]
            origin (0.0, 0.0, 0.075),(0.0,0.0,0.0)
        }

        link wrist_link3 {
            body visual viz_wrist_link3 {
                origin (0, 0.0, 0.15),
                cylinder (0.1, 0.3)
            }
            reuse collision viz_wrist_link2
        }

    }
}