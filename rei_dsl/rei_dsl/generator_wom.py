from generator_abstract_elements import AbstractRobotFormatGenerator
from generator_utilities import deg_rad, rpy_to_quaternion
from kinematic_elements import Robot, KinematicLink, KinematicJoint

import numpy as np

class WomGenerator(AbstractRobotFormatGenerator):

    def __init__(self):
        super().__init__()

    def model_to_text(self):
        return self.generate_format()

    def generate_geometry(self, body, body_link_element):
        element_type = ""
        mesh_url = ""
        # Add geometry
        if body.geometry.__class__.__name__ == "Sphere":
            pass
        elif body.geometry.__class__.__name__ == "Cube":
            pass
        elif body.geometry.__class__.__name__ == "Cylinder":
            pass
        elif body.geometry.__class__.__name__ == "Mesh":
            element_type = "'mesh'"
            mesh_url = body.geometry.path
            pass
        pos = np.array([0.0, 0.0, 0.0])
        ori = np.array([0.0, 0.0, 0.0, 1.0])
        if self.robot.links[body_link_element.name].parent_link is not None:
            origin = self.robot.links[body_link_element.name].parent_link[0].origin
            pos[0] = origin.translate.x
            pos[1] = origin.translate.y
            pos[2] = origin.translate.z
            # WOM has strange semantics, so we need to get pose from link-joint relations
            if origin.rotation is not None:
                ori = rpy_to_quaternion(deg_rad(origin.rotation.roll), deg_rad(origin.rotation.pitch),
                                        deg_rad(origin.rotation.yaw))
        if body.origin is not None:
            origin = self.robot.parent_link[0].origin
            print(self.robot.parent_link[0].name)
            pos[0] = origin.translate.x
            pos[1] = origin.translate.y
            pos[2] = origin.translate.z
            # WOM has strange semantics, so we need to get pose from link-joint relations
            if body.origin.rotation is not None:
                ori = rpy_to_quaternion(deg_rad(origin.rotation.roll), deg_rad(origin.rotation.pitch), deg_rad(origin.rotation.yaw))

        return element_type, f"{{url:{mesh_url}, position: {{x: {pos[0]}, y: {pos[1]}, z: {pos[2]} }}, orientation: {{w: {ori[3]}, x: {ori[0]}, y: {ori[1]}, z: {ori[2]} }}, scale: 100, autophysics: true  }}"


    def generate_format(self):
        wom_kinematic = ""
        robot_base = f"""{self.robot.name} = wom.create(('mesh'), {{url: 'pendulum_kocsi.mesh', position: conf.cart.position, orientation: conf.cart.orientation, scale: conf.cart.scale, autophysical: false}});
"""
        wom_kinematic = wom_kinematic.join([robot_base, '\n'])
        for link in self.robot.links.values():
            link_desc = f"""\
        let {link.name} = wom.create('mesh', {{
            {self.generate_geometry(link.body[0], link)}
        }});
            """
            wom_kinematic += link_desc + '\n'
        for joint in self.robot.joints.values():
            joint_desc = f"""\
        {joint.parent.name}.appendChild({joint.child.name});"""
            wom_kinematic += joint_desc + '\n'
        wom_kinematic += '\n' + f"""\
        {self.robot.name}.appendChild({self.robot.get_root().name});""" + '\n'
        wom_module = f"""\
module.exports = {{
    resources: `${{__dirname}}/resources`,
    init() {{
    }},
    done() {{
    }},
    render(options) {{
        
        {wom_kinematic}
        wom.render({self.robot.name});
    }}
}}
        """

        return wom_module


