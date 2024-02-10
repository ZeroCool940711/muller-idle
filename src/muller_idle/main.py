import logging

from colorama import init
from nicegui import app, context, ui

from muller_idle import colors, icons
from muller_idle.utils import int_to_float, set_icon

set_icon()

app.native.window_args["resizable"] = True


title = "Muller Idle"

ui.query(".nicegui-content").classes("p-0")

ui.page_title(title)

# with ui.scroll_area().style("width: 50vh; height: 100vh;"):


class SideBar(ui.element):
    def __init__(self, *args, **kwargs):
        self.build()

    def build(self, controls=None):
        self.menu_width = "width: 100%"

        with ui.left_drawer().style("gap: 1px") as self.left_drawer:
            ui.label(title).style("font-size: 2rem; align-self: center;")
            ui.separator()
            ui.button(
                "Home",
                icon=icons.HOME,
                color=colors.PRIMARY,
                on_click=lambda e: ui.open("/"),
            ).style(self.menu_width)

            ui.button(
                "Settings",
                icon=icons.SETTINGS,
                color=colors.PRIMARY,
                on_click=lambda e: ui.open("/settings"),
            ).style(self.menu_width)

            ui.button(
                "About",
                icon=icons.INFO,
                color=colors.PRIMARY,
                on_click=lambda e: ui.open("/about"),
            ).style(self.menu_width)

            ui.separator().style(self.menu_width)

            ui.button("Exit", icon=icons.EXIT_TO_APP, color=colors.RED).style(
                self.menu_width
            )

        ui.button(on_click=lambda: self.left_drawer.toggle(), icon=icons.MENU)


@ui.page("/")
async def index():
    SideBar()
    ui.label("Home Page")


@ui.page("/settings")
async def settings():
    SideBar()
    ui.label("Settings Page")


@ui.page("/about")
def settings():
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
