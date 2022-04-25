# imports
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# used to embed matplot lib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#####

# Data

df = pd.read_csv(r'C:\Users\Chris\Desktop\UlsterUniversity\Final Project\PySimpleGUI\Closedf.csv', parse_dates = True, index_col = 'Date')
df = df['EURUSD=X']
df = df[('2005, 01, 01'):, ]
df = df.asfreq('D') # changes frequency to daily
df.index # checks the frequency at bottom of printout
df = df.fillna(method = 'backfill')  # takes the close rows and fills in missing values back
df = df.fillna(method = 'ffill')  # takes the close rows and fills in missing values forwards, for some markets operating at different days

# EURUSD data is 'df'

## main chart ##

# create plot function - matplotlib

def main_plot(df):
    plt.plot(df)
    plt.title("EURUSD", fontsize = 14)
    plt.xlabel('DATE', fontsize = 14)
    plt.ylabel('PRICE', fontsize = 14)
    return plt.gcf() # plt.show()

# function to draw on chart

def draw_main_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side = 'top', fill = 'both', expand = 1)
    return figure_canvas_agg


# application layout

layout = [
    [sg.Canvas(key = ("MAIN_CHART"))],  ## top row
   # [[sg.Canvas(1)], [sg.Canvas(1)], sg.Text('Statistics here')], ## 
    [sg.Exit()]
]

# create window

window = sg.Window("APPLICATION - AMBITIOUS, BUT RUBBISH", layout, resizable = True, finalize = True, element_justification="center")

draw_main_figure(window['MAIN_CHART'].TKCanvas, main_plot(df))


# exit button

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()