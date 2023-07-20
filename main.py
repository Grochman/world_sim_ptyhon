from World import World


def main():
    world = World.get_instance()
    # world.populate()
    world.run()


if __name__ == "__main__":
    main()
