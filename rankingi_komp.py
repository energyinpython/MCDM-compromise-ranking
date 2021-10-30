import numpy as np
import pandas as pd

data = pd.read_csv('rankings.csv', index_col ="Ai")

methods = list(data.columns)

#ranking of Borda method
borda_df = pd.DataFrame()

for col in methods:
    borda_df[col] = data[col].max() - data[col]

borda_df['Total'] = borda_df.sum(axis = 1)
rank = np.argsort(-borda_df['Total'])
borda_df['Final rank'] = np.argsort(rank) + 1


#ranking of Copeland method
copeland_df = pd.DataFrame()
copeland_df['Wins'] = borda_df['Total']

losses = np.zeros(len(borda_df))
el = 0
for i, j in borda_df['Total'].iteritems():
    losses[el] = borda_df['Total'].sum() - j
    el += 1

copeland_df['Losses'] = losses
copeland_df['Final score'] = copeland_df['Wins'] - copeland_df['Losses']
rank = np.argsort(-copeland_df['Final score'])
copeland_df['Final rank'] = np.argsort(rank) + 1
copeland_df.to_csv('compromise_ranking.csv')
