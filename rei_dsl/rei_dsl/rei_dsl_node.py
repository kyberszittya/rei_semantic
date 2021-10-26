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
    def __init__(self, name, body, inertia):
        self.name = name
        self.body = body
        self.inertia = inertia


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
    def __init__(self, name, parent, child, axis, joint_type, origin, control_type, limit):
        self.name = name
        self.parent = parent
        self.child = child
        self.axis = axis
        self.joint_type = joint_type.lower()
        self.origin = origin
        self.control_type = control_type
        self.limit = limit

    def set_joint_idx(self, i):
        self.idx = i


class Robot(object):
    def __init__(self, name, params, templates, elements):
        self.name = name
        self.elements = elements
        self.params = params
        self.templates = templates
        # Link-Joint structure
        self.links = {}
        self.joints = {}
        self.controlled_joints = {}

    def add_link(self, name, lk):
        link = KinematicLink(lk.name, lk.body, lk.inertia)
        self.links[name] = link

    def add_joint(self, name, jnt):
        orig = Transform(jnt.origin.translate, jnt.origin.rotation)
        print(jnt)
        j = KinematicJoint(name,
                           self.links[jnt.parent.name],
                           self.links[jnt.child.name],
                           jnt.axis,
                           jnt.joint_type, orig, jnt.control_type, jnt.limit)
        if jnt.control_type is not None:
            print(jnt.control_type)
            self.controlled_joints[name] = j
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
            if body.body_type == "visual":
                body_link_element = etree.SubElement(link_element, "visual")
            elif body.body_type == "collision":
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
        # Add inertia
        for inertia in filter(lambda x: x.__class__.__name__ == "Inertial", link.inertia):
            inertial_element = etree.SubElement(link_element, "inertial")
            mass_element = etree.SubElement(inertial_element, "mass")
            mass_element.attrib["value"] = str(inertia.mass)
            inertia_matrix_element = etree.SubElement(inertial_element, "inertia")
            print(inertia.inertia_matrix)
            if inertia.inertia_matrix is None:
                inertia_matrix_element.attrib["ixx"] = str(1.0)
                inertia_matrix_element.attrib["ixy"] = str(0.0)
                inertia_matrix_element.attrib["iyy"] = str(1.0)
                inertia_matrix_element.attrib["izz"] = str(1.0)
                inertia_matrix_element.attrib["ixz"] = str(0.0)
                inertia_matrix_element.attrib["iyz"] = str(0.0)
            else:
                inertia_matrix_element.attrib["ixx"] = str(inertia.inertia_matrix.ixx)
                inertia_matrix_element.attrib["ixy"] = str(inertia.inertia_matrix.ixy)
                inertia_matrix_element.attrib["iyy"] = str(inertia.inertia_matrix.iyy)
                inertia_matrix_element.attrib["izz"] = str(inertia.inertia_matrix.izz)
                inertia_matrix_element.attrib["ixz"] = str(inertia.inertia_matrix.ixz)
                inertia_matrix_element.attrib["iyz"] = str(inertia.inertia_matrix.iyz)

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
        if joint.limit is not None:
            joint_element = etree.SubElement(joint_element, "limit")
            joint_element.attrib["lower"] = str(deg_rad(joint.limit.lower))
            joint_element.attrib["upper"] = str(deg_rad(joint.limit.upper))
    # return XML root
    return urdf_root


def instantiate_template(template_use, robot):
    links = {}
    old_links = {}
    for elem in filter(lambda x: x.__class__.__name__ == "KinematicLink", template_use.basetemplate.elements):
        # robot.add_link(elem.name, elem)
        link_name = f"{template_use.name}_{elem.name}"
        l = KinematicLink(link_name, elem.body, elem.inertia)
        links[l.name] = l
        old_links[elem.name] = l
    joints = {}
    for elem in filter(lambda x: x.__class__.__name__ == "KinematicJoint", template_use.basetemplate.elements):
        # robot.add_link(elem.name, elem)
        joint_name = f"{template_use.name}_{elem.name}"
        j = KinematicJoint(joint_name, old_links[elem.parent.name], old_links[elem.child.name], elem.axis, elem.joint_type,
                           elem.origin, elem.control_type, elem.limit)
        joints[j.name] = j
    # Select root node
    parent_links = set(links.keys())
    for j in joints.values():
        parent_links.remove(j.child.name)
    # Setup connecting joint
    origin_joint = KinematicJoint(f"jnt_{template_use.name}_connect",
                                  robot.links[template_use.origin_link.name], links[list(parent_links).pop()],
                                  None, "FIXED", template_use.origin, None, None)
    joints[origin_joint.name] = origin_joint
    return links, joints


def load_robot_from_file(path):
    f = open('grammar/kinematic_grammar.tx', 'r')
    mm = metamodel_from_str(''.join(f.readlines()), classes=[Robot])
    model_str = open(path, "r").read()
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
    return robot, urdf

