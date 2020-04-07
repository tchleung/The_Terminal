import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data(path):
    '''Initializes pandas dataframe'''
    df = pd.read_csv(path)
    return df

def plot_top_10_by_state(df,state_abr,colorhex1,colorhex2):
    fig, ax = plt.subplots(figsize=(16,7))
    index = np.arange(0,10)
    bar_width = 0.35

    if state_abr != 'US':
        most_popular_index = df[(df['ORIGIN_STATE_ABR'] == state_abr)]['ORIGIN_CITY_NAME'].value_counts().head(10).index
        height1 = df[(df['ORIGIN_STATE_ABR'] == state_abr)]['ORIGIN_CITY_NAME'].value_counts().head(10)
        height2 = df[(df['DEST_STATE_ABR'] == state_abr)]['DEST_CITY_NAME'].value_counts().head(10)
        origin = ax.bar(index, height1, bar_width, color = colorhex1)
        destination = ax.bar(index+bar_width, height2, bar_width, color = colorhex2)

        origin.set_label('As Origin')
        destination.set_label('As Destination')

        ax.set_xlabel('City')
        ax.set_xticklabels(most_popular_index)
        ax.set_xticks(index + bar_width / 2)
        ax.set_ylabel('Frequency')
        ax.legend()
        plt.xticks(rotation=45)
        plt.figtext(.5,.95,f'Most Popular {state_abr} Airport By Flight Count', fontsize=20, ha='center')
        plt.figtext(.5,.9,'(January 2020)',fontsize=13,ha='center')
    
    else:
        most_popular_index = df['ORIGIN_CITY_NAME'].value_counts().head(10).index
        height1 = df['ORIGIN_CITY_NAME'].value_counts().head(10)
        height2 = df['DEST_CITY_NAME'].value_counts().head(10)
        origin = ax.bar(index, height1, bar_width, color = colorhex1)
        destination = ax.bar(index+bar_width, height2, bar_width, color = colorhex2)

        origin.set_label('As Origin')
        destination.set_label('As Destination')

        ax.set_xlabel('City')
        ax.set_xticklabels(most_popular_index)
        ax.set_xticks(index + bar_width / 2)
        ax.set_ylabel('Frequency')
        ax.legend()
        plt.xticks(rotation=45)
        plt.figtext(.5,.95,f'Most Popular US Airport By Flight Count', fontsize=20, ha='center')
        plt.figtext(.5,.9,'(January 2020)',fontsize=13,ha='center')
    
