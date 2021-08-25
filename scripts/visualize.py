import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt


def catplot(df,x,y,kind,title,hue=None,palette='Set3',xlabel=None,ylabel=None,w_size=12,h_size=7,size=None):
    plt.figure(figsize=(w_size, h_size))
    ax = sn.catplot(data=df,x=x,y=y,hue=hue,kind=kind, palette=palette,size=size)
    ax.set(xlabel=xlabel, ylabel=ylabel)
    plt.title(title)
    plt.show()

def scatterplot(df,x,y,title,hue=None,style=None,w_size=12,h_size=7,size=None):
    plt.figure(figsize=(w_size, h_size))
    sn.scatterplot(data=df, x=x, y=y, hue=hue, style=style,size=size)
    plt.title(title,fontsize=23)
    plt.show()

def histplot(df,x,y,title,hue=None,palette='Set2',w_size=12,h_size=7,size=None):
    plt.figure(figsize=(w_size, h_size))
    sn.distplot(data=df,x=x,y=y,hue=hue,palette=palette,size=size)
    plt.title(title)
    plt.show()

def correlation_heatmap(corr,title):
    plt.figure(figsize=(20, 10))
    ax = sn.heatmap(
    corr, 
    annot=True, cmap="coolwarm"
)
    plt.title("Correlation Map of"+title)
    ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)
    

def lineplot(df,x=None,y=None,title=None,w_size=12,h_size=7,size=None):
    plt.figure(figsize=(w_size, h_size))
    sn.lineplot(data=df, x=x, y=y,size=size)
    plt.title(title)
    plt.show()

def displot(df,x=None,title=None):
    plt.figure(figsize=(12, 7))
    sn.displot(data=df, x=x)
    plt.title(title)
    plt.show()
