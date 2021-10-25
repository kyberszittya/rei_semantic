import pybullet as pb
import pybullet_data
import time
from textx import metamodel_from_str, get_children_of_type
from lxml import etree


from rei_dsl_node import Robot, robot_to_urdf, instantiate_template, load_robot_from_file


def main():
    robot, urdf = load_robot_from_file("./robots/diff_robot.robot")
    physicsClient = pb.connect(pb.GUI)
    pb.setAdditionalSearchPath(pybullet_data.getDataPath())
    pb.setGravity(0, 0, -10)
    planeId = pb.loadURDF("plane.urdf")
    startPos = [0, 0, 1]
    startOrientation = pb.getQuaternionFromEuler([0, 0, 0])
    robot_urdf = pb.loadURDF("temp.urdf", startPos, startOrientation)
    cnt_jnt = pb.getNumJoints(robot_urdf)
    print(f"Number of joints: {cnt_jnt}")
    print(robot.controlled_joints)
    for j in range(cnt_jnt):
        jnt_name = pb.getJointInfo(robot_urdf, j)[1].decode("UTF-8")
        robot.joints[jnt_name].set_joint_idx(j)
        #if jnt_name in robot.controlled_joints:
        #    jnt_dict[jnt_name] = j
    for i in range(10000):
        pb.stepSimulation()
        for _, jnt in robot.controlled_joints.items():
            if jnt.control_type == "VELOCITY":
                pb.setJointMotorControl2(robot_urdf, jnt.idx, pb.VELOCITY_CONTROL,
                                         targetVelocity=1, force=1000)

        time.sleep(1. / 240.)


if __name__ == '__main__':
    main()
