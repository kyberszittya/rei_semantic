from textx import metamodel_from_str, get_children_of_type

from kinematic_elements import Robot, KinematicLink, KinematicJoint


class AbstractRobotFormatGenerator(object):

    def __init__(self):
        super().__init__()
        self.mm = None
        self.robot = None

    def setup(self):
        f = open('grammar/kinematic_grammar.tx', 'r')
        self.mm = metamodel_from_str(''.join(f.readlines()), classes=[Robot])

    def load_description(self, path):
        model_str = open(path, "r").read()
        self.robot: Robot
        self.robot = self.mm.model_from_str(model_str)
        # Add template
        # Add links
        for elem in filter(lambda x: x.__class__.__name__ == "KinematicLink", self.robot.elements):
            self.robot.add_link(elem.name, elem)
        # Add joints
        for elem in filter(lambda x: x.__class__.__name__ == "KinematicJoint", self.robot.elements):
            self.robot.add_joint(elem.name, elem)
        for template in filter(lambda x: x.__class__.__name__ == "TemplateInstantiation", self.robot.elements):
            links, joints = self.instantiate_template(template, self.robot)
            if links is not None and joints is not None:
                for l in links:
                    self.robot.add_link(l, links[l])
                for j in joints:
                    self.robot.add_joint(j, joints[j])

    def save_format_to_file(self, path):
        with open(path, "w") as f:
            f.writelines(self.model_to_text())

    def instantiate_template(self, template_use, target: Robot):
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
            j = KinematicJoint(joint_name, old_links[elem.parent.name], old_links[elem.child.name], elem.axis,
                               elem.joint_type,
                               elem.origin, elem.control_type, elem.limit)
            joints[j.name] = j
        # Select root node
        parent_links = set(links.keys())
        for j in joints.values():
            parent_links.remove(j.child.name)
        # Setup connecting joint
        origin_joint = KinematicJoint(f"jnt_{template_use.name}_connect",
                                      target.links[template_use.origin_link.name], links[list(parent_links).pop()],
                                      None, "FIXED", template_use.origin, None, None)
        joints[origin_joint.name] = origin_joint
        return links, joints

    def model_to_text(self):
        raise NotImplementedError

    def generate_geometry(self, body, body_link_element):
        raise NotImplementedError

    def generate_format(self):
        raise NotImplementedError


