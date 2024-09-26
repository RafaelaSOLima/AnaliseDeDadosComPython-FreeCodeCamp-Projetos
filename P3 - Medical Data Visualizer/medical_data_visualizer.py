import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# 1
df = pd.read_csv('P3 - Medical Data Visualizer/medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5. 
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. 
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. 
    print(df_cat.head())

    # 8.
    fig = sns.catplot(x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat).fig
    
    # 9. Não modifique as duas próximas linhas
    fig.savefig(os.path.join('P3 - Medical Data Visualizer', 'catplot.png'))  
    return fig



# 10
def draw_heat_map():

    # 11
    df_heat = df[  
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    

    # 12
    corr = df_heat.corr().round(1)  

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 15
    sns.heatmap(corr, annot=True, mask=mask, cmap='coolwarm', fmt=".1f", ax=ax)  # fmt=".1f" para 1 casa decimal

    # 16
    fig.savefig(os.path.join('P3 - Medical Data Visualizer', 'heatmap.png'))
    return fig
