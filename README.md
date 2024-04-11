# Plagiarism-detection-in-documents


# Descripción del problema
Se desea detectar si existe algun porciento de plagio entre dos documentos dados.

# Consideraciones tomadas
Se realiza el calculo de plagio en documentos escritos en ingles.

Para ejecutar el programa se debe correr en el cmd el archivo main.py
``` py main.py```

# Explicación de la solución


## Interfaz visual
Este código crea una interfaz gráfica de usuario (GUI) simple para una herramienta de detección de plagio utilizando Tkinter. La GUI consta de:

- Una ventana principal con el título "Plagiarism Detection".
Un marco (content_frame) para organizar los elementos de la GUI.
- Dos etiquetas (text_area1_label y text_area2_label) para indicar las áreas de texto donde los usuarios pueden ingresar los textos a comparar.
- Dos áreas de texto (text_area1 y text_area2) para ingresar los textos.
- Un botón (button) que, al ser presionado, debería activar la función detect_plagiarism para comparar los textos ingresados. Sin embargo, hay un error en la definición del botón, ya que la función detect_plagiarism se llama inmediatamente al definir el botón, en lugar de pasar una referencia a la función que se llamará cuando se presione el botón.
- Una etiqueta (similarity_score_label) para mostrar el resultado de la comparación de similitud entre los textos ingresados.

La GUI permite a los usuarios ingresar dos textos y compararlos para detectar plagio. Sin embargo, debido al error mencionado, el botón no funcionará como se espera. Además, la etiqueta para mostrar el resultado de la comparación no se actualiza con el resultado de la comparación, lo que significa que el usuario no puede ver el resultado de la detección de plagio.