import pytest
from abstract_factory import WindowsFactory, MacFactory, LinuxFactory, AndroidFactory
from abstract_factory import Button, Checkbox, TreeView


@pytest.mark.parametrize("factoryClass, expectedButton, expectedCheckbox, expectedTreeview", [
    (WindowsFactory, "Rendering Windows-style Button", "Checking Windows-style Checkbox", "Expanding Windows-style TreeView"),
    (MacFactory, "Rendering MacOS-style Button", "Checking MacOS-style Checkbox", "Expanding MacOS-style TreeView"),
    (LinuxFactory, "Rendering Linux-style Button", "Checking Linux-style Checkbox", "Expanding Linux-style TreeView"),
    (AndroidFactory, "Rendering Android-style Button", "Checking Android-style Checkbox", "Expanding Android-style TreeView")
])
def test_gui_elements(factoryClass, expectedButton, expectedCheckbox, expectedTreeview):
    factory = factoryClass()
    button: Button = factory.create_button()
    checkbox: Checkbox = factory.create_checkbox()
    treeview: TreeView = factory.create_treeview()

    assert button.render() == expectedButton
    assert checkbox.check() == expectedCheckbox
    assert treeview.expand() == expectedTreeview


def test_factory_instance_types():
    factory = MacFactory()
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    treeview = factory.create_treeview()

    assert isinstance(button, Button)
    assert isinstance(checkbox, Checkbox)
    assert isinstance(treeview, TreeView)


@pytest.mark.parametrize("factoryClass, expectedButtonText", [
    (WindowsFactory, "Rendering Windows-style Button"),
    (MacFactory, "Rendering MacOS-style Button"),
    (LinuxFactory, "Rendering Linux-style Button"),
    (AndroidFactory, "Rendering Android-style Button")
])
def test_checkbox_interaction_across_platforms(factoryClass, expectedButtonText):
    factory = factoryClass()
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    interaction = checkbox.interact_with(button)

    assert expectedButtonText in interaction
    assert interaction.endswith(f"({expectedButtonText})")


def test_failing_temp_test():
    assert False, "Test supposed to fail for demo" # temp test, rm next time
