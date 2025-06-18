from abstract_factory import WindowsFactory, MacFactory, LinuxFactory, GUIAbstractFactory

def client_app(factory: GUIAbstractFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    treeview = factory.create_treeview()

    print(button.render())
    print(checkbox.check())
    print(checkbox.interact_with(button))
    print(treeview.expand())


if __name__ == "__main__":
    print("===============================\nClient: Windows GUI\n===============================")
    client_app(WindowsFactory())

    print("\n===============================\nClient: MacOS GUI\n===============================")
    client_app(MacFactory())

    print("\n===============================\nClient: Linux GUI\n===============================")
    client_app(LinuxFactory())
