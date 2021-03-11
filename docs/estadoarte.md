# Estado del arte
## Sistemas conversacionales y uso de RASA

En el mundo de la tecnologia ...

Los sistemas conversacionales están a la orden del día, estos nos permiten conducir una conversación, ya sea de forma hablada o escrita, con un sistema automático capaz de emular a un ser humano a través del uso de tecnologías del lenguaje especializadas en la compleja comprensión del mismo.

De esta forma, los sistemas de diálogo ofrecen grandes ventajas a aquellos que requieran de esta tecnología ya que aportan un servicio extra con una gran disponibilidad y accesible a todo el mundo desde cualquier lugar o dispositivo. 

Es por ello que estos sistemas se han hecho un importante hueco en el área de la salud y podemos encontrar todo tipo de asistentes, desde aquellos que permiten pedir o gestiona citas médicas hasta otros más especializados en el seguimiento y los consejos para llevar una vida más saludable.

***INFORMACIÓN QUE DEBO PONER EN ALGÚN MOMENTO
Gartner incluye chatbots, Inteligencia Artificial (IA) y Asistentes Virtuales de Clientes (AVC) entre las cinco tendencias principales de Experiencia del Cliente para observar a los CIO, afirmando que el 70% de las interacciones de los clientes involucrarán tales tecnologías emergentes para el 2022. McKinsey también, en su 2019 Global AI Survey, informa un crecimiento constante en la adopción de IA (aumento de casi 25% año tras año), con la mayoría de las empresas declarando beneficios medibles de tecnologías como el aprendizaje automático y las interfaces de conversación.

## Herramientas para desarrollar sistemas conversacionales

Podemos encontrar una gran variedad de herramientas a la hora de crear nuestro asistente conversacional, desde aquellas ofrecidas por grandes plataformas como Google o Amazon ( Dialogflow y Amazon Lex respectivamente) hasta frameworks de código abierto como Open Dialog o Rasa.

Aunque todas estas herramientas ofrecen grandes ventajas


Como ya habíamos comentado anteriormente, Rasa es una plataforma open-source para la creación y desarrollo de chatbots de forma local y en Python.

El framework de Rasa está dividido en dos partes claramente definidas, por un lado tenemos la parte que se encarga de procesar el lenguaje natural dado por el mensaje y transformarlo en datos para el asistente, este componente es conocido como Rasa NLU. Por otro lado tenemos la parte encargada de gestionar todo el diálogo y de tomar decisiones acerca de la conversación y es conocida como Rasa Core

Además existe una versión conocida como Rasa X que añade una mejora al desarrollo del sistema conversacional al añadir una interfaz gráfica que permite tener una vista previa de lo que se está probando, testear y entrenar todas las funcionalidades y tener acceso de una forma más cómoda y sencilla a todos los aspectos de creación del asistente

Mencionar que una importante ventaja del uso de Rasa es la amplia y colaborativa comunidad que posee, que facilita la resolución rápida de dudas a través de su [foro](https://forum.rasa.com)

Otra ventaja de Rasa que resulta particularmente importante para el tema que se quiere desarrollar en este trabajo es que al ser código libre los datos del usuario que son usados por el asistente no se usan después para empresas de terceros, como podría pasar si usaramos por ejemplo la plataforma de Google. Teniendo en cuenta que los datos que se van a usar para el asistente son datos médicos y confidenciales, se hace más importante aún el uso de código libre para el desarrollo.

Puedes encontrar más información sobre Rasa y como usarla [aquí]