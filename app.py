#ULTIMO CÓDIGO
import pandas as pd
import scipy.stats
import streamlit as st
import time

# estas son variables de estado que se conservan cuando Streamlin vuelve a ejecutar este script
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iteraciones', 'media'])

st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toss_coin(n):

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')
    mean = toss_coin(number_of_trials)


#CUARTA PARTE DEL CÓDIGO
#import scipy.stats
#import streamlit as st
#import time

#st.header('Lanzar una moneda')

#chart = st.line_chart([0.5])

#def toss_coin(n):

    #trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    #mean = None
    #outcome_no = 0
    #outcome_1_count = 0

    #for r in trial_outcomes:
        #outcome_no +=1
        #if r == 1:
            #outcome_1_count += 1
        #mean = outcome_1_count / outcome_no
        #chart.add_rows([mean])
        #time.sleep(0.05)

    #return mean

#number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
#start_button = st.button('Ejecutar')

#if start_button:
    #st.write(f'Experimento con {number_of_trials} intentos en curso.')
    #mean = toss_coin(number_of_trials)

#TERCER PARTE DEL CÓDIGO
#import scipy.stats
#import streamlit as st
#import time

#st.header('Lanzar una moneda')

#chart = st.line_chart([0.5])

#def toss_coin(n): # función que emula el lanzamiento de una moneda

#    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

#    mean = None
#    outcome_no = 0
#    outcome_1_count = 0

#    for r in trial_outcomes:
#        outcome_no +=1
#        if r == 1:
#            outcome_1_count += 1
#        mean = outcome_1_count / outcome_no
#        chart.add_rows([mean])
#        time.sleep(0.05)

#    return mean

#number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
#start_button = st.button('Ejecutar')

#if start_button:
#    st.write(f'Experimento con {number_of_trials} intentos en curso.')


#SEGUNDA ETAPA DEL CÓDIGO
#import streamlit as st

#st.header('Lanzar una moneda')

#number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
#start_button = st.button('Ejecutar')

#if start_button:
    #st.write(f'Experimento con {number_of_trials} intentos en curso.')

#st.write('Esta aplicación aún no es funcional. En construcción.')




#PRIMERA ETAPA DEL PROYECTO
#import streamlit as st
#st.header('Lanzar una moneda')
#st.write('Esta aplicación aún no es funcional. En construcción.')
