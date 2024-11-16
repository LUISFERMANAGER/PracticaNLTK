# Práctica NLTK análisis de frecuencia de palabras

import nltk
from nltk.tokenize import word_tokenize #Divide el texto en palabras
from nltk.corpus import stopwords # Elimina los conectores
from nltk.probability import FreqDist # Calcula la frecuencia de las palabras 

texto = """Árboles de decisión. Para obtener el árbol óptimo y valorar cada subdivisión entre todos
los árboles posibles y conseguir el nodo raiz y los subsiguientes, el
algoritmo deberá medir de alguna manera las predicciones logradas y
valorarlas para comparar de entre todas y obtener la mejor."""

# Tokenizar el texto 

palabras = word_tokenize(texto, language='spanish')
print(palabras)

# Stopwords Eliminar los conectores

stopwords = set(stopwords.words('spanish'))

# Filtramos las palabras que no estan en la lista de stop words 

palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stopwords and palabra.isalpha()]
print(palabras_filtradas)

# Analisis de frecuencia de palabras
frecuencia_palabras = FreqDist(palabras_filtradas)

# Mostrar la frecuencia de las 10 palabras más comunes 

print(frecuencia_palabras.most_common(5))


