import datetime

import flet
from flet import Column, ElevatedButton, Page, Text


def start_timer(e):
    time_display = e.control.data
    target_time = datetime.datetime.now() + datetime.timedelta(seconds=10)

    while True:
        timer_value = target_time - datetime.datetime.now()

        if timer_value.total_seconds() > 0:
            time_display.value = f"0:0{timer_value.seconds + 1}"
            time_display.update()
        else:
            time_display.value = "0:00"
            time_display.update()
            break


def main(page: Page):
    time_display = Text(value="0:05")
    start_button = ElevatedButton(text="Start", on_click=start_timer, data=time_display)

    page.add(Column([time_display, start_button]))
    page.update()


flet.app(target=main)
