"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from .backend import Lines
import datetime

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    text: str = "Type your line here."
    PastCode: str = ""
    ip: str = '1'

    def addLine(State):
        current_time = datetime.datetime.now()
        with rx.session() as session:
            session.add(Lines(ip=State.ip,line=State.text,timestamp=f"{current_time.year}-{current_time.month}-{current_time.day}"))
            session.commit()

    def getLines(State):
        with rx.session() as session:
            Lines = session.exec(session.query(Lines).options(load_only('line')).all())
            for row in Lines:
                pass

def index() -> rx.Component:
    State.addLine()
    
    return (rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.code_block(
            State.PastCode + State.text,
            language="python",
            show_line_numbers=True,
            ),
            rx.input(
            value=State.text,
            on_change=State.set_text,
            margin_left='100em',
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
