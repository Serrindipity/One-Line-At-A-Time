from calhacks import styles
from calhacks.templates import template
from calhacks.state import State

import reflex as rx

@template(route="/", title="Home")
def index() -> rx.Component:
    currCode = "print('Hello World')"
    return rx.vstack(
            rx.code_block(
                State.text,
                language="python",
                show_line_numbers=True,
                margin_top="2em",
                **styles.content_style
            ),
            rx.hstack(
                rx.input(
                    value=State.text,
                    on_change=State.set_text,
                    margin_right="5px"
                ),
                rx.button("enter", _hover={"opacity": 1,}, **styles.button_style),
                **styles.content_style
            ),
            font_size="2em",
        )