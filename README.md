# Plagiarism-detection-in-documents


# Descripción del problema
Se desea detectar si existe algún porciento de plagio entre dos documentos dados.

# Consideraciones tomadas

Para ejecutar el programa se debe correr en el cmd el archivo main.py:

``` py main.py```

# Explicación de la solución

## Preprocesamiento de los datos

En este archivo existen dos métodos que consisten en procesar los documentos dados para obtener una lista de tokens los cuales podemos calcular su similitud mas eficientemente:

- preprocess_text: Este método recibe un documento(string), le remueve todas las minúsculas, lo divide en párrafos  apoyándose en el método conver_to_paragraph, luego por cada oración en cada párrafo tokeniza sus palabras con la función de nltk word_tokenize y esta lista de listas es lo que se devuelve.

- convert_to_paragraph: Este método recibe un documento(string) y devuelve una lista con los párrafos de dicho documento, donde se asume que cada párrafo es un cambio de línea, apoyandose de la función del nltk sent_tokenize.

## Detección de plagio entre dos documentos:
En este archivo se tiene una clase llamada Plagiarism la cual contiene dos variables globales que son max_sim y path, las cuales llevan las mayores similitud entre los bloques y el texto el cual estamos buscando el plagio respectivamente, esta clase también contiene dos métodos:

- detect_plagiarism: Este método recibe dos documentos(string) se preprocesa el primer texto apoyándose de preprocess_text, luego se crea un diccionario con ayuda de gensim, con la lista de tokens recibidos de preprocess_text donde cada palabra(distinta) tiene un único id. Luego a partir de esto se crea el corpus(BOW) que es básicamente un objeto que contiene el id de la palabra y su frecuencia en cada documento. 
Luego de esto se realiza TF_IDF que lo que se hace es multiplicar un componente local(TF) con un componente global, por lo que se obtiene que una palabra que ocurre con mucha frecuencia tiene un "peso" pequeño.
Luego se crea un objecto Sim en una carpeta (simObjectDir) con el objetivo de guardar los índices de la matriz utilizando la clase Similarity en gensim: Similarity construye un índice a partir de un conjunto de documentos(párrafos) dado, esta clase divide el índice en muchos pequenos sub-índices.
Una vez creado esto se procede a calcular la similitud entre los dos textos, donde primero se preprocesa el segundo documento y se actualiza el diccionario con las palabra nuevas(si lo requiere) que contiene dicho documento y se guarda en un array la similitud de cada párrafo del segundo documento con respecto a cada párrafo del primer documento. Luego de esto se escoge la mayor similitud existente por cada párrafo del segundo texto con respecto al primero y se devuelve el promedio de estas similitudes máximas.

- most_similar_path: Este método devuelve el párrafo que contiene la mayor similitud con respecto al primer documento, de manera que dado las mayores similitudes de los párrafos del segundo documento con respecto al primero, se escoge el índice de este y se busca en el párrafos del documento.
## Interfaz visual
Este código crea una interfaz gráfica de usuario (GUI) simple para una herramienta de detección de plagio utilizando Tkinter. La GUI consta de:

- Una ventana principal con el título "Plagiarism Detection".
Un marco (content_frame) para organizar los elementos de la GUI.
- Dos etiquetas (text_area1_label y text_area2_label) para indicar las áreas de texto donde los usuarios pueden ingresar los textos a comparar.
- Dos áreas de texto (text_area1 y text_area2) para ingresar los textos.
- Un botón (button) que, al ser presionado, debería activar la función detect_plagiarism para comparar los textos ingresados.
- Otro botón que, al ser presionado devuele el resultado de most_similar_path que es el párrafo con mayor similitud con respecto al primer documento
- Una etiqueta (similarity_score_label) para mostrar el resultado de la comparación de similitud entre los textos ingresados.

La GUI permite a los usuarios ingresar dos textos y compararlos para detectar plagio. Sin embargo, debido al error mencionado, el botón no funcionará como se espera. Además, la etiqueta para mostrar el resultado de la comparación no se actualiza con el resultado de la comparación, lo que significa que el usuario no puede ver el resultado de la detección de plagio.
