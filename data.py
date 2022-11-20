import pandas as pd
import numpy as np

# ssdata = pd.read_csv('recommender/stratascratch.csv')
# print(ssdata.iloc[50]['video_title'])

card = {'How I Learned Data Science (resources to get a job) in 2021': ['0GpgMvyN0Fg', 'https://i.ytimg.com/vi/0GpgMvyN0Fg/hqdefault.jpg'], 'Most Common Coding Mistakes on Data Science Interviews': ['Bgpp99iz0I0', 'https://i.ytimg.com/vi/Bgpp99iz0I0/hqdefault.jpg'], '18 Most Recommended Data Science Platforms To Learn Python And SQL': ['wqxDfVdZ8wM', 'https://i.ytimg.com/vi/wqxDfVdZ8wM/hqdefault.jpg'], 'Automating Your Data Science Tasks In Python (importing CSV files to database AUTOMATION TUTORIAL)': ['TDwy1lSjEZo', 'https://i.ytimg.com/vi/TDwy1lSjEZo/hqdefault.jpg'], 'Applying Software Engineering Principles To Your Data Science Tasks In Python': ['N0aHeKyNEto', 'https://i.ytimg.com/vi/N0aHeKyNEto/hqdefault.jpg']}

print(len(card))
for i in card:
    print(i)
    print(card[i][1])