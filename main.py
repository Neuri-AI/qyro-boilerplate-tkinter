import tkinter as tk
from qyro_engine import ApplicationContext
from qyro_engine.ui.component import Component


class ${class_name}(tk.Tk, Component, ApplicationContext):

    def component_will_mount(self):
        self.geometry("640x480")
        self.minsize(640, 480)

    def render(self):
        label = tk.Label(
            self,
            text=(
                f"Hello, World!\n\n\n"
                f"App Title: {self.window_title}\n\n"
                f"Active Icon: {self.app_icon}\n\n"
                f"Platform: {self.platform.value} (Frozen: {self.is_frozen})\n"
                f"Build Settings:\n{self.app_settings}\n"
            ),
            justify="left",
            anchor="w",
        )
        label.place(x=50, y=50)


if __name__ == "__main__":
    window = TkApp()
    window.exec()
