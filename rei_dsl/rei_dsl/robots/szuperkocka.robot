robot szuperkocka
{
    elements {
        link base_link {
            body visual viz_cube {
                cube(10.0, 10.0, 10.0)
            }
            reuse collision viz_cube
        }
    }
}