controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    seleccion = (seleccion - 1) % 4
    mostrarOpciones()
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    validarRespuesta()
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    // Mostrar la ventana de opciones cuando el usuario pulse A
    mostrarOpciones()
})
// ============================
// Mostrar solo opciones abajo
// ============================
function mostrarOpciones () {
    opciones_str = ""
    for (let k = 0; k <= 3; k++) {
        if (k == seleccion) {
            opciones_str = "" + opciones_str + "> " + opciones_text[k] + "\n"
        } else {
            opciones_str = "" + opciones_str + "  " + opciones_text[k] + "\n"
        }
    }
    // Mostrar únicamente las opciones en la parte inferior (no volver a mostrar la pregunta)
    game.showLongText(opciones_str, DialogLayout.Bottom)
}
// ============================
// Validar respuesta
// ============================
function validarRespuesta () {
    // Respuesta correcta
    if (opciones_text[seleccion] == expected) {
        puntos += 2
        rachas += 1
        music.baDing.play()
        // Mostrar la bandera
        scene.setBackgroundImage(banderas[indice])
        pause(1200)
        // GANAR si rachas = 3
        if (rachas == 3) {
            game.over(true)
            return
        }
        mostrarpregunta()
    } else {
        // Respuesta incorrecta → perder
        music.wawawawaa.play()
        scene.setBackgroundColor(2)
        pause(500)
        game.over(false)
    }
}
// ============================
// Crear nueva pregunta (muestra solo la pregunta)
// ============================
function mostrarpregunta () {
    let idx: number;
let j: number;
let tmp: string;
indice = randint(0, paises.length - 1)
    preguntaActual = paises[indice]
    expected = capitales[indice]
    seleccion = 0
    scene.setBackgroundColor(9)
    opciones_text = [expected]
    // incorrectas
    while (opciones_text.length < 4) {
        idx = randint(0, capitales.length - 1)
        if (opciones_text.indexOf(capitales[idx]) < 0) {
            opciones_text.push(capitales[idx])
        }
    }
    // Mezcla manual
    n = opciones_text.length
    i = n - 1
    while (i > 0) {
        j = randint(0, i)
        tmp = opciones_text[i]
        opciones_text[i] = opciones_text[j]
        opciones_text[j] = tmp
        i = i - 1
    }
    // Mostrar solo la pregunta arriba; las opciones se muestran al pulsar A
    pregunta_texto = "Puntos: " + convertToText(puntos) + "\n¿Capital de " + preguntaActual + "?"
    game.showLongText(pregunta_texto, DialogLayout.Top)
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    seleccion = (seleccion + 1) % 4
    mostrarOpciones()
})
let pregunta_texto = ""
let i = 0
let n = 0
let preguntaActual = ""
let indice = 0
let rachas = 0
let puntos = 0
let expected = ""
let opciones_text: string[] = []
let opciones_str = ""
let seleccion = 0
let banderas: Image[] = []
let capitales: string[] = []
let paises: string[] = []
let texto = ""
paises = [
"Colombia",
"Francia",
"Alemania",
"Japon"
]
capitales = [
"Bogota",
"Paris",
"Berlin",
"Tokio"
]
banderas = [
assets.image`Col`,
assets.image`FRA`,
assets.image`GRM`,
assets.image`Jap`
]
scene.setBackgroundColor(9)
mostrarpregunta()
