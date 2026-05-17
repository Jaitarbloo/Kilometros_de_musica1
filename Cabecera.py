import reflex as rx

def Cabecera() -> rx.Component:
    return rx.box(
        # Contenedor con imagen de fondo y overlay degradado
        
        # Imagen de fondo + overlay negro degradado
        background_image="linear-gradient(to right, rgba(0,0,0,0.7) 0%, rgba(0,0,0,0.4) 40%, rgba(0,0,0,0) 60%), url('/bacalao_parking_puzol.jpg')",
        background_size="cover",
        background_position="center",
        min_height="100vh",
        width="100%"
    )

app = rx.App()
app.add_page(Cabecera)
