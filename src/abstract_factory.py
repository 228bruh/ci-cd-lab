from abc import ABC, abstractmethod



# abs factory
class GUIAbstractFactory(ABC):
    @abstractmethod
    def create_button(self) -> "Button":
        pass

    @abstractmethod
    def create_checkbox(self) -> "Checkbox":
        pass

    @abstractmethod
    def create_treeview(self) -> "TreeView":
        pass



# abs products
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Checkbox(ABC):
    @abstractmethod
    def check(self) -> str:
        pass

    @abstractmethod
    def interact_with(self, button: Button) -> str:
        pass


class TreeView(ABC):
    @abstractmethod
    def expand(self) -> str:
        pass



# conc products WIN
class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering Windows-style Button"


class WindowsCheckbox(Checkbox):
    def check(self) -> str:
        return "Checking Windows-style Checkbox"

    def interact_with(self, button: Button) -> str:
        return f"Windows Checkbox interacting with ({button.render()})"


class WindowsTreeView(TreeView):
    def expand(self) -> str:
        return "Expanding Windows-style TreeView"


# conc products MAC
class MacButton(Button):
    def render(self) -> str:
        return "Rendering MacOS-style Button"


class MacCheckbox(Checkbox):
    def check(self) -> str:
        return "Checking MacOS-style Checkbox"

    def interact_with(self, button: Button) -> str:
        return f"MacOS Checkbox interacting with ({button.render()})"


class MacTreeView(TreeView):
    def expand(self) -> str:
        return "Expanding MacOS-style TreeView"


# conc products LINUX
class LinuxButton(Button):
    def render(self) -> str:
        return "Rendering Linux-style Button"


class LinuxCheckbox(Checkbox):
    def check(self) -> str:
        return "Checking Linux-style Checkbox"

    def interact_with(self, button: Button) -> str:
        return f"Linux Checkbox interacting with ({button.render()})"


class LinuxTreeView(TreeView):
    def expand(self) -> str:
        return "Expanding Linux-style TreeView"


# conc products ANDROID
class AndroidButton(Button):
    def render(self) -> str:
        return "Rendering Android-style Button"


class AndroidCheckbox(Checkbox):
    def check(self) -> str:
        return "Checking Android-style Checkbox"

    def interact_with(self, button: Button) -> str:
        return f"Android Checkbox interacting with ({button.render()})"


class AndroidTreeView(TreeView):
    def expand(self) -> str:
        return "Expanding Android-style TreeView"



# conc factories
class WindowsFactory(GUIAbstractFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_treeview(self) -> TreeView:
        return WindowsTreeView()


class MacFactory(GUIAbstractFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

    def create_treeview(self) -> TreeView:
        return MacTreeView()


class LinuxFactory(GUIAbstractFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()

    def create_treeview(self) -> TreeView:
        return LinuxTreeView()

class AndroidFactory(GUIAbstractFactory):
    def create_button(self) -> Button:
        return AndroidButton()

    def create_checkbox(self) -> Checkbox:
        return AndroidCheckbox()

    def create_treeview(self) -> TreeView:
        return AndroidTreeView()