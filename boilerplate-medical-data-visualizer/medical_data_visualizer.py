import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height']/100)**2)).apply(lambda x: 1 if x > 25 else 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x>1 else 0)
df['gluc'] = df['gluc'].apply(lambda x: 1 if x>1 else 0)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='variable')


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat =  pd.melt(df,id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='variable')


    # Draw the catplot with 'sns.catplot()'
    variable_order = sorted(df_cat['variable'].unique())
    g = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count', height=6, aspect=1, order=variable_order, alpha=1)
    g.set_axis_labels("variable", "total")
    g.set_titles(col_template="cardio = {col_name}")

    # Get the figure for the output
    fig = g.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo']<=df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr().apply(lambda x: round(x, 1))

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool_)
    mask[np.triu_indices_from(mask)] = True


    # Set up the matplotlib figure
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, ax=ax, fmt='.1f')

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
