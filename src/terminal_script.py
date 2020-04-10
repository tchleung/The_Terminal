import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as scs

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
        # plt.figtext(.5,.9,'(January 2020)',fontsize=13,ha='center')
    
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
        # plt.figtext(.5,.9,'(January 2020)',fontsize=13,ha='center')
    
def two_sample_t_test(df, city1, city2, col='DEP_DELAY'):
    # samples
    city_one = df[(df['ORIGIN_CITY_NAME'] == city1) & (df[col].isnull() == False)][col]
    city_two = df[(df['ORIGIN_CITY_NAME'] == city2) & (df[col].isnull() == False)][col]
    
    # sample size
    N1 = len(city_one)
    N2 = len(city_two)

    # sample variance
    a_var = np.var(city_one)
    b_var = np.var(city_two)

    # sample std
    a_b_std = np.sqrt(a_var/N1 + b_var/N2)

    # t score
    t_score = ((city_one.mean() - city_two.mean())/a_b_std)

    # pooled degrees of freedom
    df = (a_var/N1 + b_var/N2) ** 2 / (((a_var/N1)**2)/(N1-1) + ((b_var/N2)**2)/(N2-1))

    # p value
    p_val = 1 - scs.t.cdf(t_score,df=df)

    return N1, N2, city_one.mean(), city_two.mean(), a_b_std, t_score, p_val


def t_test_against_others(df, city, col='DEP_DELAY'):
    # samples
    city_one = df[(df['ORIGIN_CITY_NAME'] == city) & (df[col].isnull() == False)][col]
    ex_city_one = df[(df['ORIGIN_CITY_NAME'] != city) & (df[col].isnull() == False)][col]
    
    # sample size
    N1 = len(city_one)
    N2 = len(ex_city_one)

    # sample variance
    a_var = np.var(city_one)
    b_var = np.var(ex_city_one)

    # sample std
    a_b_std = np.sqrt(a_var/N1 + b_var/N2)

    # t score
    t_score = ((city_one.mean() - ex_city_one.mean())/a_b_std)

    # pooled degrees of freedom
    df = (a_var/N1 + b_var/N2) ** 2 / (((a_var/N1)**2)/(N1-1) + ((b_var/N2)**2)/(N2-1))

    # p value
    p_val = 1 - scs.t.cdf(t_score,df=df)

    return N1, N2, city_one.mean(), ex_city_one.mean(), a_b_std, t_score, p_val


def t_test_weather_quan(df, condition, col):
    # samples
    sample_one = df[(df[condition] == 1)][col]
    sample_two = df[(df[condition] == 0)][col]
    
    # sample size
    N1 = len(sample_one)
    N2 = len(sample_two)

    # sample variance
    a_var = np.var(sample_one)
    b_var = np.var(sample_two)

    # sample std
    a_b_std = np.sqrt(a_var/N1 + b_var/N2)

    # t score
    t_score = ((sample_one.mean() - sample_two.mean())/a_b_std)

    # pooled degrees of freedom
    df = (a_var/N1 + b_var/N2) ** 2 / (((a_var/N1)**2)/(N1-1) + ((b_var/N2)**2)/(N2-1))

    # p value
    p_val = scs.t.sf(t_score,df=df)*2

    return N1, N2, sample_one.mean(), sample_two.mean(), a_b_std, t_score, p_val

def t_test_weather_city(df,city1,city2,condition,cond_flag,col):
    # samples
    sample_one = df[(df['ORIGIN_CITY_NAME'] == city1) & (df[condition] == cond_flag)][col]
    sample_two = df[(df['ORIGIN_CITY_NAME'] == city2) & (df[condition] == cond_flag)][col]
    
    # sample size
    N1 = len(sample_one)
    N2 = len(sample_two)

    # sample variance
    a_var = np.var(sample_one)
    b_var = np.var(sample_two)

    # sample std
    a_b_std = np.sqrt(a_var/N1 + b_var/N2)

    # t score
    t_score = ((sample_one.mean() - sample_two.mean())/a_b_std)

    # pooled degrees of freedom
    df = (a_var/N1 + b_var/N2) ** 2 / (((a_var/N1)**2)/(N1-1) + ((b_var/N2)**2)/(N2-1))

    # p value
    p_val = scs.t.sf(t_score,df=df)*2

    return N1, N2, sample_one.mean(), sample_two.mean(), a_b_std, t_score, p_val

def airline_t_test(df, city1, city2, airline1, airline2, col='DEP_DELAY'):
    # samples
    sample_one = df[(df['ORIGIN_CITY_NAME'] == city1) & (df['OP_UNIQUE_CARRIER'] == airline1) & (df[col].isnull() == False)][col]
    sample_two = df[(df['ORIGIN_CITY_NAME'] == city2) & (df['OP_UNIQUE_CARRIER'] == airline2) & (df[col].isnull() == False)][col]
    
    # sample size
    N1 = len(sample_one)
    N2 = len(sample_two)

    # sample variance
    a_var = np.var(sample_one)
    b_var = np.var(sample_two)

    # sample std
    a_b_std = np.sqrt(a_var/N1 + b_var/N2)

    # t score
    t_score = ((sample_one.mean() - sample_two.mean())/a_b_std)

    # pooled degrees of freedom
    df = (a_var/N1 + b_var/N2) ** 2 / (((a_var/N1)**2)/(N1-1) + ((b_var/N2)**2)/(N2-1))

    # p value
    p_val = scs.t.sf(t_score,df=df)*2

    return N1, N2, sample_one.mean(), sample_two.mean(), a_b_std, t_score, p_val
