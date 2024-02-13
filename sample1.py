import ctypes

from nicegui import app, ui

from src.muller_idle import color, icon

ui.page_title("test")

ui.run(
    native=True,
    reload=True,
)
