# Vacation Planner Program

## Introduction and Problem Statement

<p align="justify">
  Greetings, this is an extension of one of my A.I subject's assignment. Initially, it is about creating a vacation planner application using Genetic Algorithm through Python. In this project, I added more analysis and UI improvement. This project is split into 2 parts, one is application based, developed using streamlit API. The file is called mainUI.py. The other one is main_report.ipynb. It is a research based program with details analysis written as a report. Both can be run. For mainUI.py, user can interact more with the frontend UI whereas for main_report.ipynb, users can get more details and information on backend process with explanation.
</p>

## Contribution and Motivation
<p align="justify">
  Genetic Algorithm adopts the concept of natural selection which the fittest individuals are chosen for reproduction. With this instinct, stronger and more competent offsprings will be produced for the next generation. Genetic algorithm consists of 5 phases, they are population creation, fitness score assignment, selection, crossover and mutation. The last three phases are called evolution. Similar to nature, fittest individual will be selected to cross breed and create offspring with occasional mutation. This is the concept of evolution, also known as survival of the fittest. The main motivation of this project is to experiment different genetic algorithms with different evolution methods. In this project, 3 different types of selections, crossover and mutation methods are implemented for comparison analysis. In the end of this project, three graphs are used to plot different types of evolution methods' fitness score across generation. Through this project, we can learn more on different evolution functions will have different effects.
</p>

## Part A: Application Based (mainUI.py)
### Instructions and explanation
<p align="justify">
  !!! PLEASE MAKE SURE ALL THE FILES AND FOLDERS INCLUDING THE COMPONENTS FOLDER ARE INCLUDED IN THE SAME DIRECTORY !!!
  
  Part A is about mainUI.py. To run this program, I used Microsoft Visual Studio. First got to VS code and create a new terminal, make sure it is in cmd. At the top navigation panel, go to Terminal -> New Terminal. Then, at the terminal right side, there is a drop down arrow beside a plus sign, click it and choose cmd. After that at the terminal, type in 'streamlit run mainUI.py' and you will get a browser window pops up. That means you have successfully run the program. Before that, make sure to download the streamlit library on your machine because this program heavily depends on streamlit API.
</p>

<p align="center">
  <img width="35%" src="https://github.com/Yong-Wai-Chun/Vacation-Planner/blob/main/Components/cmd1.png?raw=true">
  <br> Figure 1: VS code CMD
</p>

<p align="justify">
  Figure 2 is the first thing you saw when the browser pops up. On the left hand side, there is a menu panel which options of GA application and GA Analysis. The page of figure 2 is GA application, it means genetic application which is the vacation planner. In this page, users can adjust their desired parameters. After that, just press the compute button and it will generate and output a result. As for the parameters, estimated budget(RM) is the expected total expense users wish to spend on the vacation. Here a default value is given with RM 2000, it means total spending will be less than or equal to RM 2000. Vacation duration is how many days users wish to spend. Number of tourist spots is the amount of tourist spots user wish to visit. Estimated hotel price per night (RM) is accommodation price per night, default value of RM 200 is given which means less than or equal to RM 200. Estimated meal price per day (RM) is the total meal price user wish to spend per day, in this case less than or equal to RM 50 value is given. Estimated price per spot (RM) is the maximum spending on one spot. Lastly, estimated trip rice per day (RM) is the maximum spending of trip price per day.
</p>

<p align="center">
  <img width="100%" src="https://github.com/Yong-Wai-Chun/Vacation-Planner/blob/main/Components/output1.png?raw=true">
  <br> Figure 2: Page 1 (GA Application)
</p>

<p align="justify">
  After done adjusting the parameter values, hit the compute button and the program will compute through genetic algorithm and the result will be output.
</p>

<p align="center">
  <img width="70%" src="https://github.com/Yong-Wai-Chun/Vacation-Planner/blob/main/Components/output2.png?raw=true">
  <br> Figure 3: Computed result
</p>

<p align="justify">
  Figure 4 is the second page of the program, users can click the GA Analysis on the menu panel on left hand side to navigate to this page. This page is more of an  analysis with some brief information. There are 3 crucial parameters used in the genetic algorithm evolution. They are retain, random_select and mutate. The retain parameter means what percentage of inidividuals should be kept as parents, default value here is 20%. The random_select means what percentage of individuals should be randomly chosen. Lastly, mutate is what percentage of parents' individuals should be mutated.
</p>

<p align="center">
  <img width="100%" src="https://github.com/Yong-Wai-Chun/Vacation-Planner/blob/main/Components/output3.png?raw=true">
  <br> Figure 4: Page 2 (GA Application)
</p>

<p align="justify">
  Figure 5 shows a real time interaction to visualize different percentage of paramters will have different effects. The graph shows the fitness score across generation. The natural trend of the graph is fitness score values started on a very high number then it drastically decreases until it gets to a very low number or near to 0. Users can play around with the adjustments to see the impact of the percentage to the genetic algorithm. 
  
  In this part, the vacation planner's paramters are fixed. The values are:
</p>

- Estimated Budget (RM) = 2000
- Vacation Duration (days) = 5
- Number of Tourist Spots = 5
- Hotel Price per Night (RM) = 200
- Price per Spot (RM) = 100
- Meal Price per Day (RM) = 50
- Trip Price per Day (RM) = 200

  
<p align="center">
  <img width="100%" src="https://github.com/Yong-Wai-Chun/Vacation-Planner/blob/main/Components/output4.png?raw=true">
  <br> Figure 5: Real Time Interaction
</p>

<p align="justify">
  As for the part 2 of this page. It is a visualization on comparison nalysis of different evolution methods. Three different methods of selection, mutation and crossover are being used for comparisons. The graphs are all sample outputs, more details can be found at main_report.ipynb. The evolution methods are:
</p>

- Selection Methods
  - Tournament Selection
  - Roulette Wheel Selection
  - Stochastic Universal Sampling
- Mutation Methods
  - Scramble Mutation
  - Swap Mutation
 - Inversion Mutation
- Crossover Methods
  - Two-points Crossover
  - Multipoints Crossover
  - Uniform Crossover
  
That is all for Part A. The program is fairly easy to use. Just adjust the parameters value and press compute. More infos can be found at main_report.ipynb

## Part B: Research Based (main_report.ipynb)

!!! INSTRUCTIONS !!!
1. Nothing especially complicated just run every cell in order.
2. If you want to look back some outputs n visualization
    
    a. To run for different outputs. Run cell that has --> ## Run this cell to view for the outputs of the implementation
    
    b. To run for visualization. Run cell that has --> # Visualization

3. To understand more, look at the markdown cells for more information on the process and function used.
4. For parameters inputs, there are 2 sets of default parameters given.
5. If want to use the default parameters, uncomment either one set.
6. If want to have self customized parameters, uncomment the code block that is labeled --> ## Customize 

<p align="justify">
  For Part B report. The process and algorithms are explained in the notebook. Try to run each cell in order. If you want to look back at some vacation planner outputs, run the cell that has comments of ## Run this cell to view for the outputs of the implementation. If you want to look at the graph visualization on different evolutions' comparison, run the cell that has comments of # Visualization. Three different methods of selection, mutation and crossover are being used for comparisons. The graphs are all sample outputs, more details can be found at main_report.ipynb. The evolution methods are:
</p>

- Selection Methods
  - Tournament Selection
  - Roulette Wheel Selection
  - Stochastic Universal Sampling
- Mutation Methods
  - Scramble Mutation
  - Swap Mutation
  - Inversion Mutation
- Crossover Methods
  - Two-points Crossover
  - Multipoints Crossover
  - Uniform Crossover

<p align="justify">
  This report is very straight forward, it is mainly about analysis and explanation of the backend process. That is all from me, thank you very much.
</p>

## Summary and Findings
In the nutshell, different evolution has different pros and cons. As for selection method, tournament selection is fairly easier to implement but roulette wheel has more diversity but quite slow because of the time complexity. As for mutation methods, inversion mutation provides the most consistent fitness score whereas the other two has high complexity and it can provide better variety. Lastly crossover methods, multipoints crossover and uniform crossover are the most ideal because they have provides high diversity.

<p align="center">
  <img width="40%" src="https://github.com/Yong-Wai-Chun/Python-Maze-Library-Mod/blob/main/components/giphy.gif?raw=true">
</p>

