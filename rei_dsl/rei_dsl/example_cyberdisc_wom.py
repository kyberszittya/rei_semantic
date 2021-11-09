import pybullet as pb
import pybullet_data
import time
from textx import metamodel_from_str, get_children_of_type
from lxml import etree

from generator_wom import WomGenerator

def main():
    generator = WomGenerator()
    generator.setup()
    generator.load_description("./robots/cyberdisc.robot")
    generator.save_format_to_file(f"{generator.robot.name}.js")


if __name__ == '__main__':
    main()