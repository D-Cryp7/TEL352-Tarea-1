# TEL352-Tarea-1
Repositorio asociado al desarrollo de la Tarea 1 de la asignatura TEL352 - Inteligencia Artificial en Agentes Autónomos.  
Además de los ejercicios del 1 al 3, se desarrolló el ejercicio 6, donde los detalles se comentan más abajo.

## Modificación del ambiente: Fantasmas estáticos.
Para probar la modificación, use:  
  
python pacman.py -l `<layout_name>` -p SearchAgent -a fn=`<search_alg>`,prob=StaticGhostsPositionSearchProblem,heuristic=`<heuristic_name>` -g IdleGhost -k 20  
  
Ejemplo:  
  

`python pacman.py -l mediumScaryMaze_new -p SearchAgent -a fn=astar,prob=StaticGhostsPositionSearchProblem,heuristic=manhattanHeuristic -g IdleGhost -k 20`  
  
## Sobre el Ejercicio 6  
![T1_2](https://user-images.githubusercontent.com/34047393/136698606-70eadc2b-2c2a-44a7-a96f-c8625e68e363.PNG)
