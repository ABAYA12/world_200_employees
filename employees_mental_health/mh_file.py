import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read the csv file
file = pd.read_csv('survey.csv')
# convert the file to a dataframe
mh_file_df = pd.DataFrame(file)
# replace null values with N/A
mh_file_df.fillna('N/A')

# find the average mental health score
mh_file_df['average_mental_health_score'] = mh_file_df['mental_health_score'].mean().round(2)
# Calculate the average mental health score for males and females separately.
male_avg = mh_file_df[mh_file_df['gender']
                      == 'Male']['mental_health_score'].mean().round(2)
female_avg = mh_file_df[mh_file_df['gender']
                        == 'Male']['mental_health_score'].mean().round(2)


# save to csv file
mh_file_df.to_csv('survey.csv', index=False)
