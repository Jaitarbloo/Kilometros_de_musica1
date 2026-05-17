import reflex as rx
import math


class State(rx.State):

    current_video: str = "https://www.youtube.com/embed/SeKszb2SwsM"

    def set_video(self, url: str):
        self.current_video = url


VIDEOS = [
    {
        "url": "https://www.youtube.com/embed/SeKszb2SwsM",
        "thumb": "https://img.youtube.com/vi/SeKszb2SwsM/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/dQw4w9WgXcQ",
        "thumb": "https://img.youtube.com/vi/dQw4w9WgXcQ/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/9bZkp7q19f0",
        "thumb": "https://img.youtube.com/vi/9bZkp7q19f0/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/kJQP7kiw5Fk",
        "thumb": "https://img.youtube.com/vi/kJQP7kiw5Fk/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/RgKAFK5djSk",
        "thumb": "https://img.youtube.com/vi/RgKAFK5djSk/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/JGwWNGJdvx8",
        "thumb": "https://img.youtube.com/vi/JGwWNGJdvx8/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/OPf0YbXqDm0",
        "thumb": "https://img.youtube.com/vi/OPf0YbXqDm0/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/k2qgadSvNyU",
        "thumb": "https://img.youtube.com/vi/k2qgadSvNyU/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/nYh-n7EOtMA",
        "thumb": "https://img.youtube.com/vi/nYh-n7EOtMA/0.jpg",
    },
    {
        "url": "https://www.youtube.com/embed/7wtfhZwyrcc",
        "thumb": "https://img.youtube.com/vi/7wtfhZwyrcc/0.jpg",
    },
]


def video_circle():

    RADIUS_PCT = 40
    ITEM_SIZE_PCT = 18
    CENTER_SIZE_PCT = 30

    circle_items = []

    n = len(VIDEOS)

    for i, video in enumerate(VIDEOS):

        angle = 2 * math.pi * i / n

        x_pct = 50 + RADIUS_PCT * math.cos(angle)
        y_pct = 50 + RADIUS_PCT * math.sin(angle)

        circle_items.append(

            rx.box(

                rx.image(
                    src=video["thumb"],
                    width="100%",
                    height="100%",
                    object_fit="cover",
                ),

                on_click=State.set_video(video["url"]),

                position="absolute",
                left=f"{x_pct}%",
                top=f"{y_pct}%",

                width=f"{ITEM_SIZE_PCT}%",
                height=f"{ITEM_SIZE_PCT}%",

                transform="translate(-50%, -50%)",

                border_radius="50%",
                overflow="hidden",

                border="0.2rem solid white",

                cursor="pointer",

                bg="black",

                z_index="10",

                _hover={
                    "transform": "translate(-50%, -50%) scale(1.08)",
                    "border": "0.2rem solid gold",
                    "transition": "0.3s",
                },
            )
        )

    return rx.box(

        # CIRCULOS EXTERIORES
        *circle_items,

        # VIDEO CENTRAL
        rx.box(

            rx.el.iframe(
                src=State.current_video,

                width="100%",
                height="100%",

                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",

                allow_fullscreen=True,

                border="none",
            ),

            position="absolute",

            left="50%",
            top="50%",

            width=f"{CENTER_SIZE_PCT}%",
            height=f"{CENTER_SIZE_PCT}%",

            transform="translate(-50%, -50%)",

            border_radius="50%",
            overflow="hidden",

            border="0.3rem solid gold",

            bg="black",

            z_index="20",
        ),

        position="relative",

        width="min(92vw, 900px)",
        aspect_ratio="1 / 1",
    )


def Los_90_Modificado():

    return rx.box(

        # FONDO
        rx.image(
            src="/cinco-culo-gordo.jpg",

            position="absolute",

            top="0",
            left="0",

            width="100%",
            height="100%",

            object_fit="cover",

            z_index="-1",
        ),

        # CONTENIDO CENTRADO
        rx.center(

            rx.vstack(

                rx.heading(
                    "Los 90 - Música Retro",
                    size="8",
                    color="gold",
                ),

                video_circle(),

                align="center",
                spacing="6",
            ),

            width="100%",
            min_height="100vh",
        ),

        position="relative",

        width="100%",
        min_height="100vh",

        overflow="hidden",
    )


app = rx.App()
app.add_page(Los_90_Modificado)