## Vacation Planner UI simulation
# This UI is created using streamlit API
# It has real time interaction

from click import option
import pandas as pd
import numpy as np
from random import randint
import random
import copy
import time

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

import streamlit as st
import altair as alt
from streamlit_folium import folium_static
import folium
from PIL import Image


# Main program
def main():
    
    # Side menu panel
    radioOptions = np.array(["GA Application", "GA Analysis"]) 
    sideBar = st.sidebar.radio("Menus", radioOptions, index=0)

    ## UI Components:
    # If side menu option is "GA Application" / Page 1
    # Default Page
    if (sideBar == radioOptions[0]):

        # Main Heading
        head1 = '<p style="font-family:arial; color:Yellow; font-size:45px; font-weight: bold; text-align: center">Genetic Algorithm - Vacation Planner Application</p>'
        st.markdown(head1, unsafe_allow_html=True)
        
        count = 200 # population number for GA
        # Estimated Total Expenses
        target = st.number_input("Estimated Budget (RM)", min_value=2000, max_value=None, value=2000, step=None, format=None, key=None, help=None)

        col1,col2 = st.columns(2) # Columns

        with col1: # column 1
            # Days
            days = st.number_input("Vacation Duration (days)", min_value=1, max_value=None, value=5, step=None, format=None, key=None, help=None)
            # Hotel price per night
            night_price= st.number_input("Estimated Hotel Price per Night (RM)", min_value=100, max_value=None, value=200, step=None, format=None, key=None, help=None)
            # Price per spot
            spot_price = st.number_input("Estimated Price per Spot (RM)", min_value=100, max_value=None, value=100, step=None, format=None, key=None, help=None)

        with col2: # column 2
            # Number of tourist spot
            spots = st.number_input("Number of Tourist Spots", min_value=1, max_value=None, value=5, step=None, format=None, key=None, help=None)
            # meal price per day
            meal_price = st.number_input("Estimated Meal Price per Day (RM)", min_value=50, max_value=None, value=50, step=None, format=None, key=None, help=None)
            # Trip price per day
            trip_price = st.number_input("Estimated Trip Price per Day (RM)", min_value=100, max_value=None, value=200, step=None, format=None, key=None, help=None)

        # Comppute button
        compute = st.button("Compute", key=None, help=None, on_click=None)

        if compute:
            # GA implementation function, find the best price combination for the vacation
            implementation(target, count, days, spots, night_price, spot_price, meal_price, trip_price)
    
    # If side menu option is "GA Analysis" / Page 2
    else:
        # Main Heading 
        head2 = '<p style="font-family:arial; color:Yellow; font-size:45px; font-weight: bold; text-align: center">Genetic Algorithm - Evolution Methods Analysis</p>'
        st.markdown(head2, unsafe_allow_html=True)
        # Header 1
        st.header("Part 1: Default Genetic Algorithm")

        # Default parameters
        # For genetic algoritm computation 
        # Unchangeable (Samples)
        target = 2000
        count = 200
        days = 5
        spots = 5
        night_price = 200
        spot_price = 100
        meal_price = 50
        trip_price = 200

        # Brief explanation
        # Bunch of markdowns
        # Nothing special
        intro = '<p style="font-family:arial; text-align: justify">This section is to visualize the analysis of different parameters used for randomness percentage, selection percentage and mutation percentage. The default paramters values are:</p>'
        st.markdown(intro, unsafe_allow_html=True)
        
        st.markdown("* Retaining Percentage = 0.2")
        st.markdown("* Random Selected Percentage = 0.05")
        st.markdown("* Mutation Percentage = 0.01")

        intro1 = '<p style="font-family:arial; text-align: justify">Real time interaction is implemented below. Try them with different value and see how the fitness score vs generation graph changes. The graph trend should be fitness score is very high initially then decreases until the value is near 0.</p>'
        st.markdown(intro1, unsafe_allow_html=True)
        st.markdown("---")

        st.subheader("Default Price Combination")
        st.markdown(f"Estimated Budget (RM) = {target}")
        st.markdown(f"Vacation Duration (days) = {days}")
        st.markdown(f"Number of Tourist Spots = {spots}")
        st.markdown(f"Hotel Price per Night (RM) = {night_price}")
        st.markdown(f"Price per Spot (RM) = {spot_price}")
        st.markdown(f"Meal Price per Day (RM) = {meal_price}")
        st.markdown(f"Trip Price per Day (RM) = {trip_price}")

        st.subheader(f"Data Visualization with Real Time Interaction")

        # Columns
        col1,col2,col3 = st.columns(3)

        with col1: # Column 1 - Retain percentage adjustment
            retain = st.number_input("Retain Percentage", min_value=0.1, max_value=None, value=0.2, step=None, format=None, key=None, help=None)
        with col2: # Column 2 - Random select percentage adjustment
            random_select = st.number_input("Random Select Percentage", min_value=0.01, max_value=None, value=0.05, step=None, format=None, key=None, help=None)
        with col3: # Column 3 - Mutate percentage adjustment
            mutate = st.number_input("Mutate Percentage", min_value=0.01, max_value=None, value=0.01, step=None, format=None, key=None, help=None)
        
        # GA implementation function for Page 2
        implementation1(target, count, days, spots, night_price, spot_price, meal_price, trip_price, retain, random_select, mutate)

        # Markdowns exlanation
        # Nothing special
        st.markdown("---")
        st.header("Part 2: Genetic Algorithm Comparison Analysis with Different Evolution Methods")
        intro2 = '<p style="font-family:arial; text-align: justify"> This section is about the analysis of different Selection methods, Mutation methods and Crossover methods used for comparisons. Three different methods of selection, mutation and crossover are being used for comparisons. Below are some sample graphs used for the fitness score across generation rough visualization. </p>'
        st.markdown(intro2, unsafe_allow_html=True)
        
        st.markdown("### Selection Methods")
        st.markdown("* Tournament Selection")
        st.markdown("* Roulette Wheel Selection")
        st.markdown("* Stochastic Universal Sampling")

        st.markdown("### Mutation Methods")
        st.markdown("* Scramble Mutation")
        st.markdown("* Swap Mutation")
        st.markdown("* Inversion Mutation")

        st.markdown("### Crossover Methods")
        st.markdown("* Two-points Crossover")
        st.markdown("* Multipoints Crossover")
        st.markdown("* Uniform Crossover")

        # Graphs Images here
        Image.open("Components/selection.jpeg").convert("RGB")
        im = Image.open("Components/selection.jpeg")
        st.image(im, caption="Selection Comparison Analysis")

        Image.open("Components/mutation.jpeg").convert("RGB")
        im1 = Image.open("Components/mutation.jpeg")
        st.image(im1, caption="Mutation Comparison Analysis")
        
        Image.open("Components/crossover.jpeg").convert("RGB")
        im2 = Image.open("Components/crossover.jpeg")
        st.image(im2, caption="Crossover Comparison Analysis")

        # Brief explanation
        st.markdown("More details can be found at the main_report.ipynb notebook. The notebook explains every backend process in details. Also follow my github for more information in README.md - https://github.com/Yong-Wai-Chun/Vacation-Planner")

## Genetic Algortihm Implementation Function 
# This function is for Page 2 (GA Analysis)
# This function takes in all the parameters that are needed to compute
# After the computation, it will generate a graph for visualization
def implementation1(target, count, days, spots, night_price, spot_price, meal_price, trip_price ,retain1, random_select1, mutate1):
    value_lst =[] # All the combination
    fitness_history = [] # Fitness Value history

    n_generation = 100

    # Population 
    p = population(count, days, spots, night_price, spot_price, meal_price, trip_price)

    # Loop thro the generation
    for i in range(n_generation):
        p = evolve(p, target, retain=retain1, random_select=random_select1, mutate=mutate1)
        value = grade(p, target)
        fitness_history.append(value)
        value_lst.append(p[0])
        value_lst.append(value)

    # Graph visualization 
    gen = [y+1 for y in range(n_generation)]
    dictt = {'Fitness_Score': fitness_history,
            'Generation': gen}
    data = pd.DataFrame.from_dict(dictt)

    line = alt.Chart(data, title="Fitness Score versus Generation").mark_line().encode(
        x='Generation',
        y='Fitness_Score'
    )

    st.markdown(" ")
    st.altair_chart(line,use_container_width=True)

    # Brief explanation
    exp = '<p style="font-family:arial; text-align: justify"> This is a graph of Fitness Score of a Genetic Algorithm across the Generation. The lower the value of fitness score, the fitter the genetic algoritm is. Different parameter values will affect the shape of the graph. </p>'
    st.markdown(exp, unsafe_allow_html=True)

## Genetic Algortihm Implementation Function 
# This function is for Page 1 (GA Application)
# This function takes in all the parameters that are needed to compute
# After the computation, it will display the vacation price combination
def implementation(target, count, days, spots, night_price, spot_price, meal_price, trip_price):
    value_lst =[]
    fitness_history = []

    n_generation = 100

    p = population(count, days, spots, night_price, spot_price, meal_price, trip_price)

    for i in range(n_generation):
        p = evolve(p, target)
        value = grade(p, target)
        fitness_history.append(value)
        value_lst.append(p[0])
        value_lst.append(value)

    target_list = value_lst[-2]
    summ1 = sum(value_lst[-2])
    final1 = value_lst[-2]

    nights = days - 1

    st.subheader("Price Combinations")
    st.markdown("Total Expenses: RM " + str(summ1))
    st.markdown("Hotel rental price for total " +  str(nights) + " nights: RM " + str(final1[0]/nights) + " * " + str(nights) + " nights")
    st.markdown("Total " + str(spots) + " spots price: RM " + str(final1[1]))
    st.markdown("Total meals price for " + str(days) + " days: RM " + str(final1[2]))
    st.markdown("Total trips price per day: RM " + str(final1[3]/days) + " * " + str(days) + " days")

## Individual Initialization Function
# Generate individuals with parameters taken in
# Return all the price in list
def individual(days, spots, night_price, spot_price, meal_price, trip_price):
    d_price = randint(50,night_price)*(days-1)
    s_price = randint(50,spot_price)*spots
    m_price = randint(20,meal_price)*days
    t_price = randint(50,trip_price)*days
    return [d_price, s_price, m_price, t_price]

## Population Initialization Function
# Generate population of individuals by taking the same parameters
# Return the individuals in list
def population(count, days, spots, night_price, spot_price, meal_price, trip_price):
    return [individual(days, spots, night_price, spot_price, meal_price, trip_price) for x in range(count)]

## Fitness score evaluation function
# Find the distance between targeted value and the individual's sum.
# lower the value, fitter the individual is
# if the value is negative, then a large fitness score will be return
def fitness(individual, target):
    total = sum(individual)
    if (target-total) < 0:
        return 10000
    return abs(target-total)

# Grading function
def grade(pop,target):
    summed = [sum(i)-target for i in pop]
    return abs( sum(summed) / len(pop))

# Evolve function with Selection, mutation and crossover function
def evolve(pop, target, retain=0.2, random_select=0.05, mutate=0.01):
    
    # Truncation
    graded = [(fitness(x, target),x) for x in pop]
    graded = [x[1] for x in sorted(graded)] 
    retain_length = int(len(graded)*retain)
    parents = graded[0:retain_length] 
    for individual in graded[retain_length:]: 
        if random_select > random.random():
            parents.append(individual)
    
    # Random min-max mutation
    for individual in parents:
        if mutate > random.random():
            pos_to_mutate = randint(0, len(individual)-1)
            individual[pos_to_mutate] = randint(min(individual), max(individual))
    
    # Single point crossover
    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length-1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = int(len(male)/2)
            child = male[:half]+female[half:]
            children.append(child)
    
    parents.extend(children)
    return parents

if __name__ == '__main__':
    main()
