# **Parte 1**

#### 1. ¿Cuáles son las diferencias entre concurrencia y paralelismo?. ¿En qué escenario es preferible usar concurrencia sobre paralelismo y viceversa?
La diferencia entre concurrencia y paralelismo. Es que concurrencia no necesariamente se ejecuta las tareas simultaneamente y utiliza un solo nucleo (CPU). Por otra parte, el paralelismo ejecuta de manera simultanea tanto las tareas o procesos en multiple nucleos(CPUs).

...  Es prefireble utilizar concurrencia cuando se tiene multiples tareas que estan esperando E/S, ya que la concurrencia hace que mientras espera permite que otras tareas se ejecuten de esta forma mejora el rendimiento.

...  Es preferible utilizar paralelismo cuando se calculos computacionales intesivos, procesamiento de big data. El paralelismo es preferible ya que permite que una tarea se divide en subtareas indenpendientemente y se ejecute simultaneamente. Reduciendo de esta forma el tiempo de ejecución.
### 2. Presenta un repaso sobre los módulos multiprocessing, asyncio, y concurrent.futures.
1. Multiprocessing: Ofrece concurrencia
2. Asyncio: Aprovecha el hecho de que las operaciones de E/S liberan el GIL para brindarnos concurrencia, incluso con un solo subproceso.
3. Concurrent.futures: Proporcionan interfaces para ejecutar tareas utilizando grupos de subprocesos o trabajadores de proceso.
   
### 3. Explica cómo Docker puede ser usado para simular entornos distribuidos y la importancia de la contenerización en proyectos paralelos y distribuidos.
link: https://sistemasdistribuidos.foroactivo.com/t211-docker-creacion-de-sistemas-altamente-distribuidos
Simulación de entornos distribuidos:
Docker permite crear contenedores ligeros y portables que encapsulan aplicaciones y sus dependencias. Cada contenedor se puede considerar como un nodo independiente en un sistema distribuido. Los contenedores se pueden comunicar entre sí a través de redes virtuales, simulando la comunicación entre nodos en un entorno distribuido real.

Reproducibilidad y portabilidad:
Docker garantiza que las aplicaciones se ejecuten de manera consistente en diferentes entornos, ya que los contenedores incluyen todas las dependencias necesarias.
Los contenedores son portables y se pueden desplegar fácilmente en diferentes sistemas operativos y plataformas de hardware.

Escalabilidad y gestión de recursos:
Docker permite escalar horizontalmente los servicios distribuyendo la carga entre múltiples contenedores.
Los contenedores se pueden replicar y distribuir en diferentes máquinas físicas o virtuales para aprovechar los recursos disponibles.
Docker proporciona herramientas para orquestar y gestionar contenedores a gran escala, como Docker Swarm o Kubernetes.


Aislamiento y seguridad:
Los contenedores proporcionan un alto nivel de aislamiento entre aplicaciones, evitando conflictos de dependencias y reduciendo los riesgos de seguridad.
Cada contenedor tiene su propio espacio de nombres y recursos asignados, lo que limita el impacto de un contenedor comprometido en el sistema general.

Desarrollo y pruebas:
Docker simplifica el proceso de desarrollo al permitir a los desarrolladores crear entornos de desarrollo locales que reflejan de cerca los entornos de producción.
Los contenedores facilitan las pruebas y la integración continua, ya que se pueden crear y destruir rápidamente para probar diferentes configuraciones y versiones.


 ## Ejercicio 1: Modelos de concurrencia en sistemas distribuidos
 Investiga y comparar diferentes modelos de concurrencia aplicados en sistemas distribuidos.
Escribir un ensayo donde comparen al menos tres modelos de concurrencia que se utilizan en
sistemas distribuidos, como el modelo de actores, CSP (Communicating Sequential Processes) y la
concurrencia basada en eventos. Deberán discutir las ventajas, desventajas, y casos de uso típicos
para cada modelo, citando ejemplos reales o hipotéticos.
Preguntas guía:
• ¿Cómo maneja cada modelo los problemas de concurrencia como el deadlock y el livelock?
• ¿Qué tipo de aplicaciones se beneficiarían más de cada modelo?
• ¿Cómo influyen estos modelos en el rendimiento y escalabilidad de una aplicación?
## Ejercicio 2: Investiga sobre Docker y Kubernetes en la gestión de cargas de trabajo distribuidas
Explora cómo Docker y Kubernetes facilitan la gestión de aplicaciones en entornos de computación
distribuida.
Deberás investigar y presentar un informe sobre cómo Docker y Kubernetes pueden ser utilizados
para orquestar y manejar aplicaciones distribuidas. Deben enfocarse en características como la
escalabilidad, balanceo de carga, y la recuperación de fallos.

Computación Paralela y Distribuida
Preguntas guía:
• ¿Cómo facilitan Docker y Kubernetes la implementación y gestión de microservicios?
• Describa un escenario donde el uso de Kubernetes proporciona una ventaja significativa
sobre el uso de Docker solo.
• Explica el rol de los volúmenes persistentes y las redes en Kubernetes cuando se manejan
servicios distribuidos.
## Ejercicio 3: Análisis crítico de la arquitectura de microservicios
Analiza los desafíos y beneficios de implementar una arquitectura de microservicios en grandes
empresas.
Redacta un análisis crítico sobre la implementación de microservicios en un contexto empresarial.
Deberán considerar tanto los aspectos técnicos como los operativos, incluyendo la seguridad, la
monitorización, y la integración continua.
Preguntas guía:
• ¿Cuáles son los principales desafíos técnicos y organizativos al adoptar microservicios en una
gran empresa?
• ¿Cómo contribuyen los microservicios a la agilidad y escalabilidad de los sistemas
empresariales?
• Evalúa el impacto de la adopción de microservicios en el mantenimiento y la gestión de la
deuda técnica.
## Ejercicio 4: Patrones de diseño en sistemas concurrentes y distribuidos
Investiga y discute varios patrones de diseño utilizados en la programación concurrente y distribuida.
Prepara una presentación o seminario sobre patrones de diseño específicos que se utilizan
frecuentemente en sistemas concurrentes y distribuidos, como el patrón de singletons distribuidos,
el patrón de saga, o el patrón de circuit breaker.
Preguntas guía:
• Describa cómo cada patrón aborda un problema específico en sistemas distribuidos.
• ¿Qué patrones serían más adecuados para manejar fallos en un sistema altamente
disponible?
• Proporciona ejemplos de cómo estos patrones se han implementado en aplicaciones
comerciales conocidas.
## Ejercicio 5: Estudio de caso sobre la tolerancia a fallos en sistemas distribuidos
Analiza estrategias de tolerancia a fallos en sistemas distribuidos utilizando casos de estudio reales.
Selecciona y estudia uno o más sistemas distribuidos reales (como bases de datos distribuidas,
sistemas de archivos distribuidos, o sistemas de procesamiento de datos en tiempo real) y analiza
cómo implementan la tolerancia a fallos. Deberán considerar aspectos como replicación de datos,
particionamiento, y manejo de errores.
Preguntas guía:
• ¿Qué técnicas de tolerancia a fallos se emplean en el sistema elegido y por qué son
efectivas?
• ¿Cómo se manejan los fallos de red o de hardware sin afectar la disponibilidad del servicio?
• Discute las compensaciones entre consistencia, disponibilidad y partición de tolerancia (CAP
Theorem) que enfrenta el sistema estudiado.
## Ejercicio 6: Docker y microservicios: desafíos de seguridad
Explora y discute los desafíos de seguridad específicos asociados con la implementación de
microservicios utilizando Docker.
Investiga los desafíos de seguridad inherentes a la arquitectura de microservicios y cómo Docker
puede tanto mitigar como exacerbar estos problemas. Deberán explorar temas como el aislamiento
de contenedores, la gestión de secretos, y las políticas de red.
Preguntas guía:
• ¿Cuáles son los principales riesgos de seguridad al utilizar contenedores para microservicios
y cómo se pueden mitigar?
• Explica la importancia de la gestión de secretos en un entorno de microservicios.
• ¿Cómo pueden las políticas de red y las herramientas de orquestación como Kubernetes
ayudar a mejorar la seguridad de los microservicios?
## Ejercicio 7: Performance y escalabilidad en Kubernetes
Investiga cómo Kubernetes maneja la performance y la escalabilidad en aplicaciones distribuidas de
gran escala.
Deberás investigar y escribir un informe sobre los mecanismos que Kubernetes utiliza para mejorar
la performance y permitir la escalabilidad de las aplicaciones que orquesta. Deberán considerar
aspectos como la programación de pods, balanceo de carga, y autoescalado.
Preguntas guía:
• ¿Cómo afectan las decisiones de programación de pods a la performance general de una
aplicación en Kubernetes?
• Describe el proceso de autoescalado en Kubernetes y cómo contribuye a la gestión eficiente
de recursos.
• Analiza el impacto del balanceo de carga en la escalabilidad y la disponibilidad de los
servicios.

## Ejercicio 8: Principios de diseño de sistemas distribuidos
Examina y discute los principios fundamentales de diseño en la creación de sistemas distribuidos
robustos y eficientes.
Debes escribir un ensayo donde discutan los principios de diseño esenciales para los sistemas
distribuidos, como transparencia, escalabilidad, seguridad y manejo de fallos. Deberán proporcionar
ejemplos de cómo estos principios se aplican en sistemas conocidos.
Preguntas guía:
• ¿Qué es la transparencia en un sistema distribuido y por qué es importante?
• ¿Cómo se puede lograr la escalabilidad en sistemas distribuidos sin comprometer la
seguridad?
• Discute cómo el diseño de sistemas distribuidos puede influir en la facilidad de manejo de
fallos.
