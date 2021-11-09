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


class KinematicLink(object):
    def __init__(self, name, body, inertia):
        self.name = name
        self.body = body
        self.inertia = inertia
        # Store children relations as well (for CG oriented approaches like MaxWhere) alongside with the very parents
        self.children_links = {}
        self.parent_link = None

    def add_child(self,  jnt):
        self.children_links[jnt.child.name] = (jnt, jnt.child)

    def add_parent(self, jnt):
        self.parent_link = (jnt, jnt.parent)


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

    def get_root(self):
        for link in self.links.values():
            if link.parent_link is None:
                return link
        return None

    def add_link(self, name, lk):
        link = KinematicLink(lk.name, lk.body, lk.inertia)
        self.links[name] = link

    def add_joint(self, name, jnt):
        orig = Transform(jnt.origin.translate, jnt.origin.rotation)
        j = KinematicJoint(name,
                           self.links[jnt.parent.name],
                           self.links[jnt.child.name],
                           jnt.axis,
                           jnt.joint_type, orig, jnt.control_type, jnt.limit)
        if jnt.control_type is not None:
            self.controlled_joints[name] = j
        # Handle child-parent relations
        self.links[jnt.parent.name].add_child(jnt)
        self.links[jnt.child.name].add_parent(jnt)
        # Append joint
        self.joints[name] = j

    def __str__(self):
        return "{},{}".format(self.name)