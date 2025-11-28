def on_up_pressed():
    global seleccion
    seleccion = (seleccion - 1) % 4
    mostrarOpciones()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    validarRespuesta()
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    # Mostrar la ventana de opciones cuando el usuario pulse A
    mostrarOpciones()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

# ============================
# Mostrar solo opciones abajo
# ============================
def mostrarOpciones():
    global opciones_str
    opciones_str = ""
    for k in range(4):
        if k == seleccion:
            opciones_str = opciones_str + "> " + opciones_text[k] + "\n"
        else:
            opciones_str = opciones_str + "  " + opciones_text[k] + "\n"
    # Mostrar únicamente las opciones en la parte inferior (no volver a mostrar la pregunta)
    game.show_long_text(opciones_str, DialogLayout.BOTTOM)

# ============================
# Validar respuesta
# ============================
def validarRespuesta():
    global puntos, rachas
    # Respuesta correcta
    if opciones_text[seleccion] == expected:
        puntos += 2
        rachas += 1
        music.ba_ding.play()

        # Mostrar la bandera
        scene.set_background_image(banderas[indice])
        pause(1200)

        # GANAR si rachas = 3
        if rachas == 3:
            game.over(True)
            return

        mostrarpregunta()
    else:
        # Respuesta incorrecta → perder
        music.wawawawaa.play()
        scene.set_background_color(2)
        pause(500)
        game.over(False)

# ============================
# Crear nueva pregunta (muestra solo la pregunta)
# ============================
def mostrarpregunta():
    global indice, preguntaActual, expected, seleccion, opciones_text, n, pregunta_texto
    indice = randint(0, len(paises) - 1)
    preguntaActual = paises[indice]
    expected = capitales[indice]
    seleccion = 0

    scene.set_background_color(9)

    opciones_text = [expected]
    # incorrectas
    while len(opciones_text) < 4:
        idx = randint(0, len(capitales) - 1)
        if capitales[idx] not in opciones_text:
            opciones_text.append(capitales[idx])

    # Mezcla manual
    n = len(opciones_text)
    i = n - 1
    while i > 0:
        j = randint(0, i)
        tmp = opciones_text[i]
        opciones_text[i] = opciones_text[j]
        opciones_text[j] = tmp
        i = i - 1

    # Mostrar solo la pregunta arriba; las opciones se muestran al pulsar A
    pregunta_texto = "Puntos: " + convert_to_text(puntos) + "\n¿Capital de " + preguntaActual + "?"
    game.show_long_text(pregunta_texto, DialogLayout.TOP)

def on_down_pressed():
    global seleccion
    seleccion = (seleccion + 1) % 4
    mostrarOpciones()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

n = 0
indice = 0
puntos = 0
rachas = 0
expected = ""
opciones_str = ""
preguntaActual = ""
pregunta_texto = ""
seleccion = 0
banderas: List[Image] = []
capitales: List[str] = []
paises: List[str] = []
opciones_text: List[str] = []
texto = ""

paises = ["Colombia", "Francia", "Alemania", "Japon"]
capitales = ["Bogota", "Paris", "Berlin", "Tokio"]
banderas = [assets.image("""
        Col
        """),
    assets.image("""
        FRA
        """),
    assets.image("""
        GRM
        """),
    assets.image("""
        Jap
        """)]

scene.set_background_color(9)
mostrarpregunta()
