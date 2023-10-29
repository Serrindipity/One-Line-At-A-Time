"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""
    text: str = "Type your line here."


def index() -> rx.Component:
    currCode = "print('Hello World')"
    return (rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        
        rx.vstack(
            rx.code_block(
            State.text,
            language="python",
            show_line_numbers=True,
            ),
            rx.text(State.text, color_scheme="green"),
            rx.input(
            value=State.text,
            on_change=State.set_text,
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
