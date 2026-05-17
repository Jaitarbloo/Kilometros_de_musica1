import reflex as rx
import math


VIDEOS = [
    "https://www.youtube.com/watch?v=SeKszb2SwsM&t=786s",
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=9bZkp7q19f0",
    "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "https://www.youtube.com/watch?v=RgKAFK5djSk",
    "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "https://www.youtube.com/watch?v=OPf0YbXqDm0",
    "https://www.youtube.com/watch?v=k2qgadSvNyU",
    "https://www.youtube.com/watch?v=nYh-n7EOtMA",
    "https://www.youtube.com/watch?v=7wtfhZwyrcc",
]


def video_circle():

    RADIUS_PCT = 40
    ITEM_SIZE_PCT = 18
    CENTER_SIZE_PCT = 28

    circle_items = []

    n = len(VIDEOS)

    for i, video_url in enumerate(VIDEOS):

        angle = 2 * math.pi * i / n

        x_pct = 50 + RADIUS_PCT * math.cos(angle)
        y_pct = 50 + RADIUS_PCT * math.sin(angle)

        circle_items.append(

            rx.box(

                rx.video(
                    url=video_url,
                    width="100%",
                    height="100%",
                    controls=True,
                ),

                position="absolute",
                left=f"{x_pct}%",
                top=f"{y_pct}%",
                width=f"{ITEM_SIZE_PCT}%",
                height=f"{ITEM_SIZE_PCT}%",

                transform="translate(-50%, -50%)",

                border_radius="50%",
                overflow="hidden",

                border="0.2rem solid white",

                bg="black",

                _hover={
                    "transform": "translate(-50%, -50%) scale(1.08)",
                    "border": "0.2rem solid gold",
                    "transition": "0.3s",
                },
            )
        )

    return rx.box(

        *circle_items,

        # VIDEO CENTRAL
        rx.box(

            rx.video(
                url="https://www.youtube.com/watch?v=SeKszb2SwsM&t=786s",
                width="100%",
                height="100%",
                controls=True,
            ),

            position="absolute",
            left="50%",
            top="50%",

            width=f"{CENTER_SIZE_PCT}%",
            height=f"{CENTER_SIZE_PCT}%",

            transform="translate(-50%, -50%)",

            border_radius="50%",
            overflow="hidden",

            border="0.25rem solid gold",

            bg="black",
        ),

        position="relative",

        width="min(92vw, 900px)",
        aspect_ratio="1 / 1",
    )


def Los_90():

    return rx.box(

        # FONDO NORMAL (YA NO FIJO)
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
app.add_page(Los_90)