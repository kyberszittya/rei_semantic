from generator_wom import WomGenerator
from kinematic_elements import Robot

import os
from shutil import copyfile

def create_maxwhere_component(robot_desc_path: str):
    generator = WomGenerator()
    generator.setup()
    generator.load_description(robot_desc_path)
    robot = generator.robot
    if not os.path.exists(f"./{robot.name}"):
        os.mkdir(f"./{robot.name}")
    generator.save_format_to_file(f"./{robot.name}/index.js")
    with open(f"./{robot.name}/component.json","w") as f:
        f.write(f"""{{
  "name": "{robot.name}",
  "main": "index.js"
}}
""")
        copyfile("./rei_maxwhere_utilities.js", f"./{robot.name}/rei_maxwhere_utilities.js")