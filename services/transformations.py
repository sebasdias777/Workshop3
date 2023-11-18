import pandas as pd 

def transformaciones():
    
    df1 = pd.read_csv("C:/Users/CHZ/Desktop/ETL/Workshop3/Data/2015.csv")
    df2 = pd.read_csv("C:/Users/CHZ/Desktop/ETL/Workshop3/Data/2016.csv")
    df3 = pd.read_csv("C:/Users/CHZ/Desktop/ETL/Workshop3/Data/2017.csv")
    df4 = pd.read_csv("C:/Users/CHZ/Desktop/ETL/Workshop3/Data/2018.csv")
    df5 = pd.read_csv("C:/Users/CHZ/Desktop/ETL/Workshop3/Data/2019.csv")

##  Df1 
    dff1 = df1.drop(['Region', 'Standard Error', 'Dystopia Residual'], axis=1)
    dff1 = dff1.rename(columns={
    'Economy (GDP per Capita)': 'GDP per capita',
    'Family': 'Social support',
    'Health (Life Expectancy)': 'Healthy life expectancy',
    'Trust (Government Corruption)': 'Perceptions of corruption'
    })

##  Df2 
    dff2 = df2.drop(['Region', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia Residual'], axis=1)
    dff2 = dff2.rename(columns={
    'Economy (GDP per Capita)': 'GDP per capita',
    'Family': 'Social support',
    'Health (Life Expectancy)': 'Healthy life expectancy',
    'Trust (Government Corruption)': 'Perceptions of corruption'
})
    
##  Df3
    dff3 = df3.drop(['Whisker.high', 'Whisker.low', 'Dystopia.Residual'], axis=1)
    dff3 = dff3.rename(columns={
    'Happiness.Rank': 'Happiness Rank',
    'Happiness.Score': 'Happiness Score',
    'Economy..GDP.per.Capita.': 'GDP per capita',
    'Family': 'Social support',
    'Health..Life.Expectancy.': 'Healthy life expectancy',
    'Trust..Government.Corruption.': 'Perceptions of corruption',
})
    
##  DF4
    dff4 = df4.rename(columns={
    'Overall rank': 'Happiness Rank',
    'Country or region': 'Country',
    'Score': 'Happiness Score',
    'Freedom to make life choices': 'Freedom',
})
    
##  DF5 
    dff5 = df5.rename(columns={
    'Overall rank': 'Happiness Rank',
    'Country or region': 'Country',
    'Score': 'Happiness Score',
    'Freedom to make life choices': 'Freedom',
})
    
### Concat 
    combined_df = pd.concat([dff1, dff2, dff3, dff4, dff5], ignore_index=True)
    combined_df['Happiness Score'] = combined_df['Happiness Score'].round(3)
    combined_df['Social support'] = combined_df['Social support'].round(3)
    combined_df['GDP per capita'] = combined_df['GDP per capita'].round(3)
    combined_df['Freedom'] = combined_df['Freedom'].round(3)
    combined_df['Healthy life expectancy'] = combined_df['Healthy life expectancy'].round(3)
    combined_df = combined_df.drop(['Country','Happiness Rank','Perceptions of corruption','Generosity'], axis=1)
    combined_df.to_csv("C:/Users/CHZ/Desktop/ETL/Workshop3/Data/combinated.csv", index=False)
    return combined_df
    

