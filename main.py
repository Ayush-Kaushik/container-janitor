from classes.Janitor import Janitor


def main():
    janitor = Janitor()
    janitor.check_status()

    if janitor.get_exist():
        janitor.remove_exited()
        janitor.remove_image()


if __name__ == "__main__":
    main()
