robot szuperhenger
{
    elements {
        link base_link {
            body visual viz_cube {
                sphere(0.5)
            }
            reuse collision viz_cube
        }
    }
}