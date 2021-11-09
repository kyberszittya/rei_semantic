from lxml import etree

from generator_abstract_elements import AbstractRobotFormatGenerator
from generator_utilities import deg_rad
from kinematic_elements import Robot, KinematicLink, KinematicJoint


class UrdfGenerator(AbstractRobotFormatGenerator):

    def __init__(self):
        super().__init__()

    def generate_geometry(self, body, body_link_element):
        if body.origin is not None:
            origin_viz_link_element = etree.SubElement(body_link_element, "origin")
            origin_viz_link_element.attrib[
                "xyz"] = f"{body.origin.translate.x} {body.origin.translate.y} {body.origin.translate.z}"
            if body.origin.rotation is not None:
                origin_viz_link_element.attrib[
                    "rpy"] = f"{deg_rad(body.origin.rotation.roll)} {deg_rad(body.origin.rotation.pitch)} {deg_rad(body.origin.rotation.yaw)}"
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

    def model_to_text(self):
        urdf = self.generate_format()
        return etree.tostring(urdf, pretty_print=True, encoding="unicode")

    def generate_format(self):
        robot = self.robot
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
                self.generate_geometry(body, body_link_element)
            # Set reuse geometries
            for body in filter(lambda x: x.__class__.__name__ == "ReuseBody", link.body):
                body_link_element = None
                if body.body_type == "visual":
                    body_link_element = etree.SubElement(link_element, "visual")
                elif body.body_type == "collision":
                    body_link_element = etree.SubElement(link_element, "collision")
                self.generate_geometry(body.template, body_link_element)
            # Add inertia
            for inertia in filter(lambda x: x.__class__.__name__ == "Inertial", link.inertia):
                inertial_element = etree.SubElement(link_element, "inertial")
                mass_element = etree.SubElement(inertial_element, "mass")
                mass_element.attrib["value"] = str(inertia.mass)
                inertia_matrix_element = etree.SubElement(inertial_element, "inertia")
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


