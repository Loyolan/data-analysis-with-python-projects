import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv').set_index('date')

# Clean data
lower_th = df['value'].quantile(0.025)
upper_th = df['value'].quantile(0.975)

df = df[(df['value'] > lower_th) & (df['value'] < upper_th)]


def draw_line_plot():
    # Draw line plot
    df.index = pd.to_datetime(df.index)
    fig, ax = plt.subplots(1, 1, sharey=True, figsize=(12, 4))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_ylabel("Page Views")
    ax.set_xlabel('Date')
    sns.lineplot(data=df, x='date', y='value', ax=ax)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.index = pd.to_datetime(df.index)
    df_bar = df.groupby([df.index.year, df.index.strftime('%B')])['value'].sum().unstack()
    df_bar.fillna(0, inplace=True)

    # Draw bar plot
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[months_order]
    fig, ax = plt.subplots(figsize=(10, 8))
    df_bar.plot(kind='bar', ax=ax)
    plt.xticks()
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, sharey=True, figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box, hue='year', ax=ax[0])
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)
    months_ord = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box, hue='month', ax=ax[1], order=months_ord)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.gca().ticklabel_format(style='plain', axis='y', useOffset=False)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig