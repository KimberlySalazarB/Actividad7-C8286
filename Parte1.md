# **Parte 1**

#### 1. ¿Cuáles son las diferencias entre concurrencia y paralelismo?. ¿En qué escenario es preferible usar concurrencia sobre paralelismo y viceversa?
La diferencia entre concurrencia y paralelismo. Es que concurrencia no necesariamente se ejecuta las tareas simultaneamente y utiliza un solo nucleo (CPU). Por otra parte, el paralelismo ejecuta de manera simultanea tanto las tareas o procesos en multiple nucleos(CPUs).

. Es prefireble utilizar concurrencia cuando se tiene multiples tareas que estan esperando E/S, ya que la concurrencia hace que mientras espera permite que otras tareas se ejecuten de esta forma mejora el rendimiento.

. Es preferible utilizar paralelismo cuando se calculos computacionales intesivos, procesamiento de big data. El paralelismo es preferible ya que permite que una tarea se divide en subtareas indenpendientemente y se ejecute simultaneamente. Reduciendo de esta forma el tiempo de ejecución.
