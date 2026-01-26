import reflex as rx

config = rx.Config(
    app_name="Kilometros_de_musica1",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
        api_url="https://kilometros-de-musica1.onrender.com",
    
                   			cors_allowed_origins=[ "http://localhost:3000",
        
                                          "https://www.kilometrosdemusica.com",
        
                                        			]
    
)