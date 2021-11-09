from textx import metamodel_from_str, get_children_of_type

import os
import copy
import lxml
from lxml import etree
import pybullet as pb
import pybullet_data
import time
import math


from kinematic_elements import Robot






def load_robot_from_file(path):



    urdf = robot_to_urdf(robot)
    print(etree.tostring(urdf, pretty_print=True, encoding="unicode"))
    with open("temp.urdf", "w") as f:
        f.writelines(etree.tostring(urdf, pretty_print=True, encoding="unicode"))
    return robot, urdf

