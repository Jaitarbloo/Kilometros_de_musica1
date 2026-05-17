import reflex as rx


from Navbar_trasparente import Navbar_trasparente
from Navbar import Navbar
from Video_Inicial import video_inicial
from Cabecera import Cabecera
#from Los_80 import Los_80
from Los_90 import Los_90
from Prueba_componente import Los_90_Modificado
from Carretera_de_musica import Carretera_musica
from Conciertos import Conciertos
from Concierto_iconos import Concierto_iconos



def index():
    
    return rx.vstack(

                        Navbar_trasparente(),
                        #Navbar(),
                        Cabecera(),
                        #Los_80(),
                        Los_90(),
                        Los_90_Modificado(),
                        Carretera_musica(),
                        Conciertos(),
                        Concierto_iconos(),
                       
                        
                    spacing="0",    


                    )

    


app = rx.App()
app.add_page(index, title="El viaje de tu vida")