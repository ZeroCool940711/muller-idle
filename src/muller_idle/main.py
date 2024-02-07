import flet as ft
import flet_easy as fs

from muller_idle.utils import first_run, get_options

if_first_run = first_run()

options = get_options()

app = fs.FletEasy(route_init="/")


# We add a page
@app.page(route="/")
def index_page(data: fs.Datasy):
    page = data.page

    # Most of these hardcoded options bellow will later go into the Options menu, to a db or config file and loaded from there.

    # Set the page title and theme mode.
    page.title = options["app_title"]
    page.theme_mode = options["theme_mode"]

    # Set the page transitions for each platform.
    theme = ft.Theme()
    theme.page_transitions.macos = ft.PageTransitionTheme.FADE_UPWARDS
    theme.page_transitions.linux = ft.PageTransitionTheme.ZOOM
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE
    page.theme = theme

    # set padding to 0 to remove the default padding or the menu bar and bottom bar will look out of place.
    page.padding = 0

    # set to auto to enable scrollbars so we can see if anything have been pushed off the screen
    # page.scroll = "AUTO"

    page.window_maximized = True

    def go_counter(e):
        page.go("/counter")

    return ft.View(
        route="/",
        controls=[
            ft.Text("Home page"),
            ft.FilledButton("Go to Counter", on_click=go_counter),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


# We add a second page
@app.page(route="/counter")
def counter_page(data: fs.Datasy):
    page = data.page

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    def go_home(e):
        page.go("/")

    return ft.View(
        route="/counter",
        controls=[
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),
            ft.FilledButton("Go to Home", on_click=go_home),
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


# We run the application
app.run()
