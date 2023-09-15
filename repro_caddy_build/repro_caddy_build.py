import reflex as rx


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", font_size="2em"),
            rx.link("Other Page", href="/other"),
        ),
    )


def other():
    return rx.center(rx.image(src="/2023-08-24_11.23.04.png"))


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(other)
app.compile()
