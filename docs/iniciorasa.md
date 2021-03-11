# Uso de RASA 🚀

## ¿Cómo funciona RASA? 
El usuario pregunta algo al sistema conversacional, por ejemplo "quiero comprar una camiseta", entonces RASA analiza el mensaje usando sus tecnologías de reconocimiento del lenguaje y obtiene y clasifica los datos obtenidos, de esta forma entiende que tiene la intención de realizar una compra (intent: comprar), la entidad a la que hace referencia es una pizza (entity: pizza) y la acción que debe serle respondida al usuario es, por ejemplo una confirmación de compra (action: confirmar_compra), una vez esto es realizado, la repuesta que da el bot es "¿Estas seguro de tu compra?"

## ¿Qué hay en cada archivo de Rasa?
- nlu.md: En él escribimos las intenciones del usuario al expresar algo, conocidos en la plataforma como intents. Ejemplo: si el usuario dice "hola" su intención (intent) es saluar.
- stories.md: Indica los diferentes caminos que deberá de tomar el bot ante los diferentes mensajes (utter) que reciba.
- domain.yml: Registra los diferentes intents, utter y actions del bot.
- config.yml: Especifica toda la configuración del sistema y se rige por políticas, las más destacables y además incluidas en nuestro proyecto son:
    * TEDpolicy: para redes neuronales y entrenamiento
    * MemorizationPolicy: Para memorizar una acción si existieran las anteriores
    * MappingPolicy: Ejecuciones basadas en mapeo
- rules.md: En este fichero se guardan todo tipo de reglas obligatorias que siempre se han de realizar durante la conversación.

## Comandos útiles para RASA 

> rasa init 

Para iniciar tu proyecto en rasa desde 0 con los archivos por defecto

> rasa train 

Para comenzar con el entrenamiento de tu bot y de su NLU y generar un modelo nuevo

> rasa shell

Iniciar el bot en tu terminal local a partir del último modelo generado ( que reside en models/ )

> rasa shell nlu

Similar a rasa shell a diferencia de que añade la funcionalidad de indicar las probabilidades de elección de los intents y las actions que se han elegido.

> rasa run actions

Cuando desarrollamos acciones para nuestro asistente conversacional es importante activar dichas acciones con este comando

> rasa x

Activa y pone en marcha la versión de rasa con interfaz gráfica que resulta muy útil para poner a prueba las conversaciones con el bot o ver estadisticas y resultados de otras conversaciones anteriores entre sus múltiples funcionalidades

## GitHub de Rasa

En el [perfil de GitHub de Rasa](https://github.com/RasaHQ) se puede encontrar una amplia variedad de de ejemplos de bots y de lenguajes de entrenamiento (NLU) muy útiles para ejemplificar o servir de guía a la hora de desarrollar un bot.

## Cuestiones y temas en los que todavía debo indagar más:
¿Qué pasa cuando el usuario dice algo que no está previsto por el desarrollador?
El sistema intenta calcular cual de las posibles intenciones del usuario se aproxima mas a lo que quería decir, pero esto muchas veces puede fallar o inducir a problemas que generen cierta sensación de que el bot es inestable o no está bien hecho. 
Por ello existe una política conocida como Fallback Policy que permite al bot volver atrás en su toma de decisiones y hacerle al usuario repetir lo que le quería decir.