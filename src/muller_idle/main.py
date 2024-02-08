import logging
import os

from nicegui import ui

from muller_idle.utils import int_to_float, set_icon

set_icon("src/muller_idle/assets/icon.ico")


ui.header(value="Muller Idle")

with ui.row() as row1:
    ui.button("Start", on_click=lambda: timer.activate())
    ui.button(
        "Stop",
        on_click=lambda: [timer.deactivate(), slider.set_value(0.0)],
    )
    ui.button("Reset", on_click=lambda: slider.set_value(0.0))

# ui.separator()

with ui.row().classes("w-96 gap-1 no-wrap") as row2:
    time_label = ui.label("Time:")
    slider = ui.linear_progress(
        value=float(f"{0.0:.2f}"), size="30px", show_value=False
    )
    timer = ui.timer(
        1,
        lambda: slider.set_value(
            (slider.value + 0.1) % int_to_float(100, multiplier=1.0)
        ),
    )

    timer.deactivate()

    ui.button("Start", on_click=lambda: timer.activate())
    ui.button(
        "Stop",
        color="red",
        on_click=lambda: [timer.deactivate(), slider.set_value(0.0)],
    )


logging.basicConfig(level=logging.INFO)
ui.run(
    native=True,
    # window_size=(800, 400),
    # fullscreen=False,
    # frameless=True,
    reload=True,
    dark=True,
    title="Muller Idle",
)
