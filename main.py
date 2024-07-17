
###import library
from ulits import process_new
import streamlit as st
import numpy as np
import joblib


##load the model
model = joblib.load("model_xgboost")

def top_leagues():

    st.title("Top Football Leagues Scores.....")
    st.markdown("<hr>",unsafe_allow_html=True)
##input filed
    Country=st.selectbox('country',options=['Spain', 'Italy', 'Germany', 'England', 'Brazil', 'France', 'USA','Portugal ', ' Netherlands'])
    League=st.selectbox('League',options=['La Liga', 'Serie A', 'Bundesliga', 'Premier League',
       'Brasileiro league', 'France Ligue 11', 'France Ligue 20',
       'France Ligue 2', 'France Ligue 12', 'France Ligue 9',
       'France Ligue 15', 'France Ligue 6', 'France Ligue 3',
       'France Ligue 16', 'France Ligue 14', 'France Ligue 4',
       'France Ligue 1', 'France Ligue 10', 'France Ligue 7',
       'France Ligue 13', 'France Ligue 8', 'France Ligue 5',
       'France Ligue 19', 'France Ligue 18', 'France Ligue 17', 'MLS',
       'Primeira Liga', 'Eredivisie'])
    club=st.selectbox('club',options=['BET', 'BAR', 'ATL', 'CAR', 'VAL', 'JUV', 'RMA', 'PSG', 'CEL',
       'EIB', 'HUE', 'VIL', 'MON', 'SOC', 'Florin', 'LIV', 'SAS', 'LAZ',
       'VER', 'NAP', 'ATA', 'FIO', 'BEN', 'CAG', 'CRZ', 'Cyril', 'ROM',
       'SAM', 'Marco', 'IMI', 'TOR', 'HKI', 'BMG', 'BAY', 'Sandro', 'HOF',
       'FCA', 'RBL', 'CHE', 'SCF', 'SCH', 'WOB', 'MAI', 'ARS', 'STP',
       'UNB', 'LAG', 'KOL', 'GRO', 'INT', 'TOT', 'LEI', 'CRY', 'MNC',
       'RAN', 'WHU', 'ACM', 'BOU', 'GRE', 'SAP', 'CEA', 'SAN', 'HUR',
       'BOT', 'FLA', 'CAM', 'FLU', 'CFC', 'GET', 'LEV', 'GIR', 'SEV',
       'PAR', 'UDI', 'SVW', 'DOR', 'NAN', 'VfB', 'OPE', 'CRU', 'FOR',
       'COR', 'SCR', 'BIL', 'OSA', 'ESP', 'GRA', 'Mario', 'BSC', 'BOR',
       'CAE', 'LIL', 'REN', 'MNU', 'ANG', 'SIV', 'MAR', 'STE', 'GAL',
       'MPE', 'LYO', 'STR', 'LOK', 'BUR', 'WAT', 'EVE', 'NEW', 'WOL',
       'ALA', 'VDG', 'SJE', 'TIG', 'BAH', 'Bruno', 'PAL', 'LAF', 'ORL',
       'PHI', 'MIN', 'CHF', 'CCR', 'NYC', 'HDY', 'COL', 'SKC', 'SOU',
       'VID', 'NYC FC', 'Santi', 'LIS', 'FAR', 'BRA', 'AVE', 'FAM', 'POR',
       'GIL', 'VGU', 'FER', 'NAC', 'FEY', 'BOA', 'MIJ', 'Sassuolo ',
       'LEC', 'DUS', 'FRA', 'NIC', 'NOR', 'RBB',
       'chongqing dangdai lifan f.c', 'GOI', 'AJA', 'VIT', 'EMM', 'TWE',
       'SPR', 'PSV', 'WIL', 'HEE', 'HER', 'VVV', 'RSL', 'NER', 'BOL',
       'MET', 'REI', 'LEN', 'BRE', 'DIJ', 'AVL', 'LEE', 'BHA', 'CAP',
       'AZA', 'Aitor', 'Tim', 'CSK', 'RZA', 'UTR'])
    player_name=st.selectbox('player name',options=['Juanmi Callejon', 'Antoine Griezmann', 'Luis Suarez',
       'Ruben Castro', 'Kevin Gameiro', 'Cristiano Ronaldo',
       'Karim Benzema', 'Neymar ', 'Iago Aspas', 'Sergi Enrich',
       'Sandro Ramlrez', 'Lionel Messi', 'Gerard Moreno', 'Morata',
       'Wissam Ben Yedder', 'Willian Jose', 'Andone ', 'Cedric Bakambu',
       'Isco', 'Mohamed Salah', 'Gregoire Defrel', 'Ciro Immobile',
       'Nikola Kalinic', 'Dries Mertens', 'Alejandro Gomez',
       'Jose CallejOn', 'Iago Falque', 'Giovanni Simeone', 'Mauro Icardi',
       'Diego Falcinelli', 'Cyril Thereau', 'Edin Dzeko',
       'Lorenzo Insigne', 'Fabio Quagliarella', 'Borriello ',
       'Carlos Bacca', 'Gonzalo Higuain', 'Keita Balde', 'Andrea Belotti',
       'Fin Bartels', 'Lars Stindl', 'Serge Gnabry', 'Wagner ',
       'Andrej Kramaric', 'Florian Niederlechner', 'Robert Lewandowski',
       'Emil Forsberg', 'Timo Werner', 'Nils Petersen', 'Vedad Ibisevic',
       'Maximilian Philipp', 'A\x81dam Szalai',
       'Pierre-Emerick Aubameyang', 'Guido Burgstaller', 'Max Kruse',
       'Chicharito ', 'Anthony Modeste', 'Arjen Robben', 'Alexis Sanchez',
       'Romelu Lukaku', 'Harry Kane', 'Jamie Vardy', 'Christian Benteke',
       'Pedro None', 'Eden Hazard', 'Roberto Firmino', 'Sadio Mane',
       'Philippe Coutinho', 'Diego Costa', 'Dele Alli', 'Sergio Aguero',
       'Jermain Defoe', 'Fernando Llorente', 'Michail Antonio',
       'Zlatan Ibrahimovic', 'Olivier Giroud', 'Son Heung-Min',
       'Joshua King', 'Diego Souza', 'Pablo ', 'Gabriel Jesus',
       'Rogerio ', 'Vitor Bueno', 'Marinho ', 'Andres Chavez',
       'Cicero Semedo', 'Giorgian de Arrascaeta', 'Keno ', 'Fred ',])
    Matches_Played=st.slider('Matches_Played',min_value=2,max_value=37,step=1)
    Substitution=st.slider('Substitution',min_value=0,max_value=26,step=1)
    mins=st.slider('mins',min_value=264,max_value=4177)
    Goals=st.slider('Goals',min_value=2,max_value=37)
    xG_Avg_Match=st.slider('xG_Avg_Match',min_value=0.07,max_value=1.35)
    Shots=st.slider('shots',min_value=0.07,max_value=1.35)
    OnTarget=st.slider('OnTarget',min_value=2,max_value=102)
    Shots_Per_Avg_Match=st.slider('Shots Per Avg Match',min_value=0.8,max_value=7.2)
    On_Target_Per_Avg_Match=st.slider('On Target Per Avg Match',min_value=0.24,max_value=3.63)
    Year=st.selectbox('Year',options=[2016,2017,2018,2019,2020])
    Minutes_Per_Match=st.slider('Minutes_Per_Match',min_value=63.111111111111114,max_value=193.0)
    Shooting_Accuracy=st.slider('Shooting_Accuracy',min_value=0.225,max_value=0.9166666666666666)

    st.markdown("<hr>",unsafe_allow_html=True)

    if st.button('predict xG ....'):

      new_data=np.array([Country,League,club,Matches_Played,Substitution,mins,Goals,xG_Avg_Match,Shots,OnTarget,Shots_Per_Avg_Match
                      ,Shooting_Accuracy,On_Target_Per_Avg_Match,Year,Minutes_Per_Match,player_name])
      ##call the function from ulits.py to aplly the pipline
      x_processed=process_new(x_new=new_data)
      
      ##predict using model 
      y_pred=model.predict(x_processed)

      ##Display Result 
      st.success(f'predict xG is{y_pred}')

    return None


if __name__ == "__main__":
    ##call function
    top_leagues()
