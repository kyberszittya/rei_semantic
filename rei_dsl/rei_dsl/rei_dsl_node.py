from textx import metamodel_from_str, get_children_of_type

import os
import copy
import lxml
from lxml import etree
import pybullet as pb
import pybullet_data
import time
import math

class KinematicLink(object):
    def __init__(self, name, body):
        self.name = name
        self.body = body


class Translate(object):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z


class Rotation(object):
    def __init__(self, roll=0.0, pitch=0.0, yaw=0.0):
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw


class Transform(object):
    def __init__(self, translate, rotation):
        self.translate = translate
        self.rotation = rotation


class KinematicJoint(object):
    def __init__(self, name, parent, child, axis, joint_type, origin):
        self.name = name
        self.parent = parent
        self.child = child
        self.axis = axis
        self.joint_type = joint_type.lower()
        self.origin = origin


class Robot(object):
    def __init__(self, name, params, templates, elements):
        self.name = name
        self.elements = elements
        self.params = params
        self.templates = templates
        # Link-Joint structure
        self.links = {}
        self.joints = {}

    def add_link(self, name, lk):
        link = KinematicLink(lk.name, lk.body)
        self.links[name] = link

    def add_joint(self, name, jnt):
        orig = Transform(jnt.origin.translate, jnt.origin.rotation)
        j = KinematicJoint(name,
                           self.links[jnt.parent.name],
                           self.links[jnt.child.name],
                           jnt.axis,
                           jnt.joint_type, orig)
        self.joints[name] = j

    def __str__(self):
        return "{},{}".format(self.name)



def deg_rad(deg: float):
    return math.pi*deg/180.0

def geometry_to_urdf(body, body_link_element):
    if body.origin is not None:
        origin_viz_link_element = etree.SubElement(body_link_element, "origin")
        origin_viz_link_element.attrib["xyz"] = f"{body.origin.translate.x} {body.origin.translate.y} {body.origin.translate.z}"
        if body.origin.rotation is not None:
            origin_viz_link_element.attrib["rpy"] = f"{deg_rad(body.origin.rotation.roll)} {deg_rad(body.origin.rotation.pitch)} {deg_rad(body.origin.rotation.yaw)}"
    geom_link_element = etree.SubElement(body_link_element, "geometry")
    # Add geometry
    if body.geometry.__class__.__name__ == "Sphere":
        geom_element = etree.SubElement(geom_link_element, "sphere")
        geom_element.attrib["radius"] = f"{body.geometry.radius}"
    elif body.geometry.__class__.__name__ == "Cube":
        geom_element = etree.SubElement(geom_link_element, "box")
        geom_element.attrib["size"] = f"{body.geometry.x} {body.geometry.y} {body.geometry.z}"
    elif body.geometry.__class__.__name__ == "Cylinder":
        geom_element = etree.SubElement(geom_link_element, "cylinder")
        geom_element.attrib["radius"] = f"{body.geometry.radius}"
        geom_element.attrib["length"] = f"{body.geometry.height}"

def robot_to_urdf(robot):
    urdf_root = etree.Element("robot", name=f"{robot.name}")
    # Add links
    for link in robot.links.values():
        link_element = etree.SubElement(urdf_root, "link")
        link_element.attrib["name"] = link.name
        # Set base geometries
        for body in filter(lambda x: not x.__class__.__name__ == "ReuseBody", link.body):
            body_link_element = None
            if body.body_type=="visual":
                body_link_element = etree.SubElement(link_element, "visual")
            elif body.body_type=="collision":
                body_link_element = etree.SubElement(link_element, "collision")
            geometry_to_urdf(body, body_link_element)
        # Set reuse geometries
        for body in filter(lambda x: x.__class__.__name__ == "ReuseBody", link.body):
            body_link_element = None
            if body.body_type=="visual":
                body_link_element = etree.SubElement(link_element, "visual")
            elif body.body_type=="collision":
                body_link_element = etree.SubElement(link_element, "collision")
            geometry_to_urdf(body.template, body_link_element)
    # Add joints
    for joint in robot.joints.values():
        joint_element = etree.SubElement(urdf_root, "joint")
        joint_element.attrib["name"] = joint.name
        joint_element.attrib["type"] = joint.joint_type
        parent_element = etree.SubElement(joint_element, "parent")
        parent_element.attrib["link"] = joint.parent.name
        parent_element = etree.SubElement(joint_element, "child")
        parent_element.attrib["link"] = joint.child.name
        # Axis definition
        if joint.axis is not None:
            axis_element = etree.SubElement(joint_element, "axis")
            axis_element.attrib["xyz"] = f"{joint.axis.x} {joint.axis.y} {joint.axis.z}"
        if joint.origin is not None:
            origin_element = etree.SubElement(joint_element, "origin")
            origin_element.attrib["xyz"] = \
                f"{joint.origin.translate.x} {joint.origin.translate.y} {joint.origin.translate.z}"
            origin_element.attrib["rpy"] = \
                f"{deg_rad(joint.origin.rotation.roll)} {deg_rad(joint.origin.rotation.pitch)} {deg_rad(joint.origin.rotation.yaw)}"
    # return XML root
    return urdf_root



def instantiate_template(template_use, robot):
    links = {}
    old_links = {}
    for elem in filter(lambda x: x.__class__.__name__ == "KinematicLink", template_use.basetemplate.elements):
        # robot.add_link(elem.name, elem)
        link_name = f"{template_use.name}_{elem.name}"
        l = KinematicLink(link_name, elem.body)
        links[l.name] = l
        old_links[elem.name] = l
    joints = {}
    for elem in filter(lambda x: x.__class__.__name__ == "KinematicJoint", template_use.basetemplate.elements):
        # robot.add_link(elem.name, elem)
        joint_name = f"{template_use.name}_{elem.name}"
        j = KinematicJoint(joint_name, old_links[elem.parent.name], old_links[elem.child.name], elem.axis, elem.type, elem.origin)
        joints[j.name] = j
    # Select root node
    parent_links = set(links.keys())
    for j in joints.values():
        parent_links.remove(j.child.name)
    # Setup connecting joint
    origin_joint = KinematicJoint(f"jnt_{template_use.name}_connect",
                                  robot.links[template_use.origin_link.name], links[list(parent_links).pop()],
                                  None, "FIXED", template_use.origin)
    joints[origin_joint.name] = origin_joint
    return links, joints


def main():
    f = open('kinematic_grammar.tx', 'r')
    mm = metamodel_from_str(''.join(f.readlines()), classes=[Robot])
    model_str = """
    robot basic_robot 
    {
        templates {
            template wheel { 
                elements {
                    link wheel_axle {
                        body visual viz_wheel_axle { cylinder (0.025, 0.05) }
                        reuse collision viz_wheel_axle
                    }
                    joint jnt_left_wheel : wheel_axle->wheel_link: [0,0,1] { 
                        type CONTINUOUS
                        origin (0.0, 0.0, 0.05), (0.0,0.0,0.0) 
                    }
                    link wheel_link {
                        body visual viz_wheel_link { cylinder (0.2, 0.1) }
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
                        body visual viz_caster_wheel_link { cylinder (0.2, 0.1) }
                        reuse collision viz_caster_wheel_link
                    }
                    joint jnt_caster_tire : caster_wheel_link->tire_link { 
                        type CONTINUOUS
                        origin (0.0, 0.0, 0.05), (0.0,0.0,0.0) 
                    }
                    link tire_link {
                        body visual viz_tire_link { cylinder (0.2, 0.1) }
                        reuse collision viz_tire_link
                    }
                }
            }
        }
        elements {
            
            link base_link {
                body visual viz_base_link {
                    origin (-0.25, 0.0, 0.0),
                    cube (0.5, 0.2, 0.05) 
                }
                reuse collision viz_base_link           
            }
            
            use right_wheel: wheel base_link -> (0,-0.2, -0.05),(90.0,0.0,0.0)
            use left_wheel:  wheel base_link -> (0, 0.2, -0.05),(-90.0,0.0,0.0)
            use caster_wheel: Caster_wheel base_link -> (-0.3, 0.0, 0.0),(0.0, 90.0, 0.0)
        }
    }
    """
    robot: Robot
    robot = mm.model_from_str(model_str)
    # Add template
    # Add links
    for elem in filter(lambda x: x.__class__.__name__ == "KinematicLink", robot.elements):
        robot.add_link(elem.name, elem)
    # Add joints
    for elem in filter(lambda x: x.__class__.__name__ == "KinematicJoint", robot.elements):
        robot.add_joint(elem.name, elem)
    for template in filter(lambda x: x.__class__.__name__ == "TemplateInstantiation", robot.elements):
        links, joints = instantiate_template(template, robot)
        for l in links:
            robot.add_link(l, links[l])
        for j in joints:
            robot.add_joint(j, joints[j])
    urdf = robot_to_urdf(robot)
    print(etree.tostring(urdf, pretty_print=True, encoding="unicode"))
    with open("temp.urdf", "w") as f:
        f.writelines(etree.tostring(urdf, pretty_print=True, encoding="unicode"))
    physicsClient = pb.connect(pb.GUI)
    pb.setAdditionalSearchPath(pybullet_data.getDataPath())
    pb.setGravity(0, 0, -10)
    planeId = pb.loadURDF("plane.urdf")
    startPos = [0, 0, 1]
    startOrientation = pb.getQuaternionFromEuler([0, 0, 0])
    pb.loadURDF("temp.urdf", startPos, startOrientation)
    for i in range(10000):
        pb.stepSimulation()
        time.sleep(1. / 240.)


if __name__ == '__main__':
    main()
