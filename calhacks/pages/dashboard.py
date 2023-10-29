"""The dashboard page."""
from calhacks import styles
from calhacks.templates import template
from calhacks.state import State

import reflex as rx

@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.spacer(),
        rx.box(
            rx.heading("about", font_size="2em"),
            rx.text(
                "information"
            ),
            rx.button("continue", **styles.button_style),
            border="3px solid #BA9EF6",
            margin_top="1em",
            **styles.content_style
        )
    )
