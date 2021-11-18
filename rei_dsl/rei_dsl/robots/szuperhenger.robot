robot szuperhenger
{
    elements {
        link base_link {
            body visual viz_cube {
                cylinder(1.0, 5.7)
            }
            reuse collision viz_cube
        }
    }
}