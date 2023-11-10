# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 00:17:02 2023

@author: USER
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


def lineplot(head,headers):
    """ Function to create a lineplot. Arguments:
        A dataframe with a column "Year" and other columns to be taken as y.
        A list containing the headers of the columns to plot.
        
        This is a very general version. You do not need to do something
        like that. A simple plot function will do. But transferring the data 
        as argument would be nice. Scoping (= having no arguments and pulling variables from the 
        main program) should better be avoided for simple programs. 
        It can be a source of hard to find errors.
    """

    plt.figure()

    #

    for head in headers:
        plt.plot(df_africa_pv["Year"], df_africa_pv[head], label=head)

    #plt.xlim(min(df_africa_pv["Year"]), df_africa_pv["Year"].max())

    # labelling
    plt.title("North Afircan continent populations from 2000 to 2020")
    plt.xlabel("Year")
    plt.ylabel("Population per 100 millions")
    #plt.legend()
    plt.legend(loc="upper right")
    # save as png
    plt.savefig("lineplot_NAfrica.png")
    plt.show()

    return
#end of function 1



def pieplot():
    """ Function to create a pie plot. Arguments:
        A dataframe with a column "Continent" polplation to be taken as y.
        A list containing the headers of the columns to plot.
        
        
    """
    
    plot = df_africa.groupby(['Continent'],sort=False).sum().plot.pie(y='Population ', autopct='%1.0f%%', figsize=(10, 10))
    plt.title(("Population of African Continent from 2000 to 2020 \n"))
    #plt.title("Population of African Continent from 2010 to 2020 \n" , bbox={'facecolor':'0.8', 'pad':5})                                                    
    plt.legend(loc="upper right")
    plt.savefig("piechart_africa.png")




#end of function 2


def barplot():
    """ Function to create a pie plot. Arguments:
        A dataframe with a column "Continent" polplation to be taken as y.
        A list containing the headers of the columns to plot.
        
        
    """
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(df_africa_south['Country'],df_africa_south['GDP (USD)'])
  
    plt.title(("GDP of South African contries "))
    plt.show()                                 
    #plt.legend(loc="upper right")
    #plt.savefig("piechart_southafrica.png")

#end of function 3



#Readig the csv file and create the data frame 
df_africa = pd.read_csv("Data_Africa.csv")

#print(df_africa.groupby(['Continent']).count( ))

#create a new data frame only including 'North Africa' Continent 
df_africa_1 = df_africa[(df_africa["Continent"] =='North Africa')]

#print (df_africa.info())
#print(df_africa_1)
#print(df_africa_1['Country'].unique())

#pivoting the table to and reset index to 
df_africa_pv = df_africa_1.pivot(index='Year', columns='Country', values='Population ').reset_index()

print(df_africa_pv)



#create and array with columna value except index 1 
contries = df_africa_pv.columns[1:]

#Calling the lineplot function 
lineplot(df_africa_pv, contries )


#Calling the pieplot function 
pieplot()

# select conties from South Africa
df_africa_south = df_africa[(df_africa["Continent"] =='South Africa')]


#Calling the barchart function 
barplot()

