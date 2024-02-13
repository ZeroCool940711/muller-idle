import logging

from nicegui import app, server, ui

from muller_idle import color, icon
from muller_idle.utils import set_icon

set_icon()

app.native.window_args["resizable"] = True


title = "Muller Idle"

ui.query(".nicegui-content").classes("p-0")

ui.page_title(title)


class Aligments:
    def __init__(self):
        self.start = "start"
        self.end = "end"
        self.center = "center"
        self.space_between = "space-between"
        self.space_around = "space-around"
        self.space_evenly = "space-evenly"


def close_app():
    if app.native.main_window:
        if app.native.start_args.get("reload", False):
            app.shutdown()
        else:
            app.native.main_window.destroy()
    else:
        server.Server.instance.should_exit = True


class SideBar(ui.element):
    def __init__(self, *args, **kwargs):
        self.build()

    def build(self, controls=None):
        self.menu_width = "width: 100%"

        with ui.left_drawer().style("gap: 1px") as self.left_drawer:
            ui.label(title).style("font-size: 2rem; align-items: center; ")
            ui.separator().style(self.menu_width)
            ui.button(
                "Home",
                icon=icon.HOME,
                color=color.PRIMARY,
                on_click=lambda e: ui.open("/"),
            ).style(self.menu_width)

            ui.button(
                "Settings",
                icon=icon.SETTINGS,
                color=color.PRIMARY,
                on_click=lambda e: ui.open("/settings"),
            ).style(self.menu_width)

            ui.button(
                "About",
                icon=icon.INFO,
                color=color.PRIMARY,
                on_click=lambda e: ui.open("/about"),
            ).style(self.menu_width)

            ui.space().classes("end-0")

            ui.button(
                "Exit",
                icon=icon.EXIT_TO_APP,
                color=color.RED,
                on_click=lambda e: close_app(),
            ).style(self.menu_width).classes("end-0")

        ui.button(on_click=lambda: self.left_drawer.toggle(), icon=icon.MENU)


@ui.page("/")
async def index() -> None:
    SideBar()
    ui.label("Home Page")


@ui.page("/settings")
async def settings():
    SideBar()
    ui.label("Settings Page")


@ui.page("/about")
def about() -> None:
    SideBar()
    ui.label("About Page")


if __name__ in {"__main__", "__mp_main__"}:
    logging.basicConfig(level=logging.DEBUG)  # noqa
    ui.run(
        native=True,
        # viewport="width=100%, height=100%",
        window_size=(1900, 1000),
        # frameless=True,
        reload=True,
        dark=True,
        title=title,
    )
