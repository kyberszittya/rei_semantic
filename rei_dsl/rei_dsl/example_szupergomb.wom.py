from generator_wom import WomGenerator

def main():
    generator = WomGenerator()
    generator.setup()
    generator.load_description("./robots/szupergomb.robot")
    generator.save_format_to_file(f"index.js")


if __name__ == '__main__':
    main()