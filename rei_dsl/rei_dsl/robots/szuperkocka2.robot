robot szuperkocka2
{
    elements {
        link base_link {
            body visual viz_cube {
                cube(1.0, 1.0, 1.0)
            }
            reuse collision viz_cube
        }

        link endbox {
            body visual viz_endbox {
                cube(0.5, 0.7, 0.3)
            }
            reuse collision viz_endbox
        }

        link endbox_tree_1 {
            body visual viz_endbox_tree_1 {
                cube(0.2, 0.2, 0.2)
            }
            reuse collision viz_endbox_tree_1
        }

        link endbox_tree_2 {
            body visual viz_endbox_tree_2 {
                cube(0.2, 0.2, 0.2)
            }
            reuse collision viz_endbox_tree_2
        }

        link leg_left {
            body visual viz_leg_left {
                origin (0.0, 0.0, -0.6),(0.0, 0.0, 0.0)
                cube(0.2, 1.2, 0.2)
            }
            reuse collision viz_leg_left
        }

        link leg_right {
            body visual viz_leg_right {
                origin (0.0, 0.0, -0.6),(0.0, 0.0, 0.0)
                cube(0.2, 1.2, 0.2)
            }
            reuse collision viz_leg_right
        }

        joint jnt_endbox: base_link->endbox: [1,0,0]  {
            type REVOLUTE
            origin (0.0, 0.0, 0.5),(0.0,0.0,0.0)
        }

        joint jnt_endbox_tree_1: endbox->endbox_tree_1: [1,0,0]  {
            type REVOLUTE
            origin (0.2, 0.0, 0.55),(0.0,0.0,0.0)
        }

        joint jnt_endbox_tree_2: endbox->endbox_tree_2: [1,0,0]  {
            type REVOLUTE
            origin (-0.2, 0.0, 0.55),(0.0,0.0,0.0)
        }

        joint jnt_leg_left: base_link->leg_left: [1,0,0]  {
            type REVOLUTE
            origin (0.0, 0.2, -0.5),(0.0,0.0,0.0)
        }

        joint jnt_leg_right: base_link->leg_right: [1,0,0]  {
            type REVOLUTE
            origin (0.0, -0.2, -0.5),(0.0,0.0,0.0)
        }
    }
}