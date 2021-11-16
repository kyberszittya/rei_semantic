from generator_abstract_elements import AbstractRobotFormatGenerator
from generator_utilities import deg_rad, rpy_to_quaternion
from kinematic_elements import Robot, KinematicLink, KinematicJoint

import numpy as np

def pos_to_json(vec3):
    return f"{{ x: {vec3[0]}, y: {vec3[1]}, z: {vec3[2]} }}"

class WomGenerator(AbstractRobotFormatGenerator):

    def __init__(self):
        super().__init__()

    def geometry_utility_functions(self):
        return f"""
function getCubeGeometry(p1, p2, p3, p4, p5, p6, p7, p8){{
    
    const frontFrameSection = {{
        material_name: 'Physics/DebugDraw/VertexDriven',
        renderop: 'trianglestrap',
        geometry: [
          // REAR FACE
          // 1-2-3
          {{ type: 'position', arg: p1}},
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 0, a: 1 }} }},
          {{ type: 'position', arg: p2}},
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 0, a: 1 }} }},
          {{ type: 'position', arg: p3}},
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 0, a: 1 }} }},
          // 1-3-4
          {{ type: 'position', arg: p1}},
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 0, a: 1 }} }},
          {{ type: 'position', arg: p3}},
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 0, a: 1 }} }},
          {{ type: 'position', arg: p4}},
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 0, a: 1 }} }},
          // FRONT FACE
          // 5-6-7
          {{ type: 'position', arg: p7}},
          {{ type: 'color', arg: {{ r: 0, g: 0, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p6}},
          {{ type: 'color', arg: {{ r: 0, g: 0, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p5}},
          {{ type: 'color', arg: {{ r: 0, g: 0, b: 1, a: 1 }} }},
          // 5-7-8
          {{ type: 'position', arg: p8}},
          {{ type: 'color', arg: {{ r: 0, g: 0, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p7}},
          {{ type: 'color', arg: {{ r: 0, g: 0, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p5}},
          {{ type: 'color', arg: {{ r: 0, g: 0, b: 1, a: 1 }} }},
          // BOTTOM FACE
          // 1-2-8
          {{ type: 'position', arg: p8}},
          {{ type: 'color', arg: {{ r: 1, g: 1, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p2}},
          {{ type: 'color', arg: {{ r: 1, g: 1, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p1}},
          {{ type: 'color', arg: {{ r: 1, g: 1, b: 1, a: 1 }} }},
          // 1-7-8
          {{ type: 'position', arg: p7}},
          {{ type: 'color', arg: {{ r: 1, g: 1, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p8}},
          {{ type: 'color', arg: {{ r: 1, g: 1, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p1}},
          {{ type: 'color', arg: {{ r: 1, g: 1, b: 1, a: 1 }} }},
          // LEFT FACE
          // 1-4-6
          {{ type: 'position', arg: p1}},
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 0, a: 1 }} }},
          {{ type: 'position', arg: p4}},
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 0, a: 1 }} }},
          {{ type: 'position', arg: p6}},
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 0, a: 1 }} }},
          // 1-6-7
          {{ type: 'position', arg: p1}},
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 0, a: 1 }} }},
          {{ type: 'position', arg: p6}},
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 0, a: 1 }} }},
          {{ type: 'position', arg: p7}},
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 0, a: 1 }} }},
          // RIGHT FACE
          // 2-3-5
          {{ type: 'position', arg: p5}}, 
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p3}}, 
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p2}},
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 1, a: 1 }} }},
          // 2-5-8
          {{ type: 'position', arg: p8}}, 
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p5}}, 
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p2}},
          {{ type: 'color', arg: {{ r: 1, g: 0, b: 1, a: 1 }} }},
          // TOP FACE
          // 3-4-5
          {{ type: 'position', arg: p5}}, 
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 1, a: 1 }} }},          
          {{ type: 'position', arg: p4}}, 
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p3}},
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 1, a: 1 }} }},
          // 4-5-6
          {{ type: 'position', arg: p4}}, 
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p5}}, 
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 1, a: 1 }} }},
          {{ type: 'position', arg: p6}},
          {{ type: 'color', arg: {{ r: 0, g: 1, b: 1, a: 1 }} }},
        ]
      }}
    return [frontFrameSection]

}}
"""

    def model_to_text(self):
        return self.generate_format()

    def generate_geometry(self, body, body_link_element):
        element_type = ""
        mesh_url = ""
        # Add geometry
        pos = np.array([0.0, 0.0, 0.0])
        ori = np.array([0.0, 0.0, 0.0, 1.0])
        """
        if self.robot.links[body_link_element.name].parent_link is not None:
            origin = self.robot.links[body_link_element.name].parent_link[0].origin
            pos[0] = origin.translate.x
            pos[1] = origin.translate.y
            pos[2] = origin.translate.z
            # WOM has strange semantics, so we need to get pose from link-joint relations
            if origin.rotation is not None:
                ori = rpy_to_quaternion(deg_rad(origin.rotation.roll), deg_rad(origin.rotation.pitch),
                                        deg_rad(origin.rotation.yaw))
        """
        base_scale = 100

        if body.origin is not None:
            #
            translate = np.array([body.origin.translate.x, body.origin.translate.y, body.origin.translate.z])
            translate = translate.dot(np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]]))
            #
            origin = body.origin
            pos[0] = translate[0]
            pos[1] = translate[1]
            pos[2] = translate[2]
            # WOM has strange semantics, so we need to get pose from link-joint relations
            if body.origin.rotation is not None:
                ori = rpy_to_quaternion(deg_rad(origin.rotation.roll), deg_rad(origin.rotation.pitch), deg_rad(origin.rotation.yaw))
        if body.geometry.__class__.__name__ == "Sphere":
            pass
        elif body.geometry.__class__.__name__ == "Cube":
            w = body.geometry.x
            h = body.geometry.y
            d = body.geometry.z
            fx = pos[0]
            fy = pos[1]
            fz = pos[2]
            cube_points = np.array([
                [-w / 2.0 + fx, -h / 2.0 + fy, d / 2.0 + fz],
                [w / 2.0 + fx, -h / 2.0 + fy, d / 2.0 + fz],
                [w / 2.0 + fx,  h / 2.0 + fy, d / 2.0 + fz],
                [-w / 2.0 + fx,  h / 2.0 + fy, d / 2.0 + fz],
                [w / 2.0 + fx, h / 2.0 + fy, -d / 2.0 + fz],
                [-w / 2.0 + fx, h / 2.0 + fy, -d / 2.0 + fz],
                [-w / 2.0 + fx, -h / 2.0 + fy, -d / 2.0 + fz],
                [w / 2.0 + fx, -h / 2.0 + fy, -d / 2.0 + fz],
            ])
            cube_points *= 100
            return "'manualvisual'",f"""    
    geom_{body_link_element.name} = getCubeGeometry({pos_to_json(cube_points[0])}, 
                    {pos_to_json(cube_points[1])}, 
                    {pos_to_json(cube_points[2])},
                    {pos_to_json(cube_points[3])},
                    {pos_to_json(cube_points[4])},
                    {pos_to_json(cube_points[5])},
                    {pos_to_json(cube_points[6])},
                    {pos_to_json(cube_points[7])});
"""
        elif body.geometry.__class__.__name__ == "Cylinder":
            pass
        elif body.geometry.__class__.__name__ == "Mesh":
            element_type = "'mesh'"
            mesh_url = body.geometry.path
            return element_type, f"{{url:{mesh_url}, position: {{x: {pos[0]}, y: {pos[1]}, z: {pos[2]} }}, orientation: {{w: {ori[3]}, x: {ori[0]}, y: {ori[1]}, z: {ori[2]} }}, scale: 100, autophysics: true  }}"


    def get_root_link_description(self, link):
        geometry_type, geometry_text = self.generate_geometry(link.body[0], link)
        link_desc = f"""\
        {geometry_text}
        {self.robot.name} = wom.create({geometry_type}, {{
            id: '{self.robot.name}_{link.name}',
            sections: geom_{link.name}
        }});
        """
        return link_desc + '\n'

    def robot_control(self):
        # TODO implement as socket.io
        joint_ctrl = ""
        for j in self.robot.joints.values():
            joint_ctrl += f"""{j.child.name}.setOrientation({{angle: dpos, axis: {{ x: 0, y: 1.0, z: 1.0 }} }},'relative', 'parent');\n"""
        return joint_ctrl



    def get_link_description(self, link):
        geometry_type, geometry_text = self.generate_geometry(link.body[0], link)
        pos = np.array([0.0, 0.0, 0.0])
        ori = np.array([0.0, 0.0, 0.0, 1.0])
        base_scale = 100
        if self.robot.links[link.name].parent_link is not None:
            origin = self.robot.links[link.name].parent_link[0].origin
            #
            translate = np.array([origin.translate.x, origin.translate.y, origin.translate.z])
            translate = translate.dot(np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]]))
            #
            pos[0] = translate[0] * base_scale
            pos[1] = translate[1] * base_scale
            pos[2] = translate[2] * base_scale
            # WOM has strange semantics, so we need to get pose from link-joint relations
            if origin.rotation is not None:
                ori = rpy_to_quaternion(deg_rad(origin.rotation.roll), deg_rad(origin.rotation.pitch),
                                        deg_rad(origin.rotation.yaw))
        link_desc = f"""\
                {geometry_text}
    let {link.name} = wom.create({geometry_type}, {{
        id: '{self.robot.name}_{link.name}',
        position: {{x: {pos[0]}, y: {pos[1]}, z: {pos[2]} }}, 
        orientation: {{w: {ori[3]}, x: {ori[0]}, y: {ori[1]}, z: {ori[2]} }},
        sections: geom_{link.name}
    }});
                    """
        return link_desc + '\n'


    def generate_format(self):
        wom_kinematic = ""

        links_list = list(self.robot.links.values())
        wom_kinematic += self.get_root_link_description(links_list[0])
        for link in links_list[1:]:
            wom_kinematic += self.get_link_description(link)
        wom_kinematic += f"""{links_list[0].name} = {self.robot.name}\n"""
        for joint in self.robot.joints.values():
            joint_desc = f"""{joint.parent.name}.appendChild({joint.child.name});"""
            wom_kinematic += joint_desc + '\n'
        wom_module = f"""\
const path = require('path')
const {{ wom }} = require('maxwhere')
const io = require('./socket.io.min.js');

var tickObj = null;

{self.geometry_utility_functions()}    

const socket = io();

function init(props) {{
}}

function done() {{
}}

var control_tick = function() {{
    dpos = 0.1;
    {self.robot.name}.setOrientation({{angle: dpos, axis: {{ x: 0, y: 1.0, z: 1.0 }} }},'relative', 'parent');
    
}}

function render(props, children) {{
    wom.addResources(path.resolve(__dirname, 'resources'))

    
    
    {wom_kinematic}    
    wom.appendChild({self.robot.name})
    wom.render({self.robot.name})
    
    
    if (tickObj==null){{
        tickObj = setInterval(control_tick, 50);
    }}
    

    return <node />
}}
module.exports = {{
    init,
    done,
    render
}}
        """

        return wom_module


