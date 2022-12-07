import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = df = pd.read_csv("fcc-forum-pageviews.csv",sep=",",index_col="date")

# Clean data
df2=df.nlargest(round(df["value"].count()*0.025),columns="value").append(df.nsmallest(round(df["value"].count()*0.025),columns="value"))
df = df.drop(index=df2.index)


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(df.index, df["value"])
    ax.xaxis.set_major_locator(plt.MaxNLocator(6))
    plt.ticklabel_format(style='plain', axis='y')
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    fig.subplots_adjust(bottom=0.500)
    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Years"] = pd.to_datetime(df_bar.index).year
    df_bar["Months"] = pd.to_datetime(df_bar.index).month_name()
    df_bar = df_bar.groupby(["Years", "Months"])["value"].mean().astype(int)
    df_bar = df_bar.reset_index()
    df_bar
    

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")

    chart = sns.barplot(data=df_bar, x="Years", y="value", hue="Months")
    ax.set(xlabel='Years', ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    print(df_box)
    df_box['year'] = [d.year for d in pd.to_datetime(df_box.index)]
    df_box['month'] = [d.strftime('%b') for d in pd.to_datetime(df_box.index)]
    
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(32, 5), dpi=100)
    sns.boxplot(x = "year", y = "value", data = df_box,ax=ax[0])
    plt.ylim(min(df_box["value"]), max((df_box["value"])))
    ax[0].ticklabel_format(style='plain', axis='y',useOffset=False)
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=month_order, ax=ax[1])
    ax[1].ticklabel_format(style='plain', axis='y')
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
