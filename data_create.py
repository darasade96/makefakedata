columns_headers = [
    'cholesterol_level', 'diabetes_pedigree_function', 'family_diabetes_history', 'diet_type', 
    'star_sign', 'social_media_usage', 'physical_activity_level', 'sleep_duration'
]

# dara = 'cholesterol_level, family_diabetes_history, social_media_usage, sleep_duration

# irene = diabetes_pedigree_function, diet_type, physical_activity_level, 

import random
import pandas as pd
import numpy as np

#import the existing csv file to get the features 
existing_df = pd.read_csv('diabetes_prediction_dataset.csv')
num_patients = len(existing_df)


def generate_cholesterol_data ():
    data = []
    
    for _ in range (num_patients):
        cholesterol_level = round (random.uniform(120, 250), 2) #generate cholesterol levels between 120 and 250 mg/dL

        data.append (cholesterol_level)
        
    return data 

def generate_family_diabetes_history():
    np.random.seed(42)

    history_choice = np.random.choice(
        ['None', 'One Type 1', 'One Type 2', 'Multiple Type 1 & Type 2'], 
        p=[0.45, 0.1, 0.25, 0.2], # Adjust probabilities as needed
        size=num_patients
    )

    #print (pd.DataFrame(family_diabetes_history, columns=['family_diabetes_history']))
    return history_choice

def generate_social_media_usage ():
    np.random.seed(42)

    usage_choice = np.random.choice(
        ['None', 'Low', 'Medium', 'High'], 
        p=[0.25, 0.25, 0.25, 0.25],  # Adjust probabilities as needed
        size = num_patients
    )

    #print(pd.DataFrame(social_media_usage, columns=['social_media_usage']))
    return usage_choice

def generate_sleep_duration ():
    np.random.seed(42)

    sleep_duration = np.random.randint(4, 11, size=num_patients)  # Generate sleep duration between 4 and 10 hours
    
    #print (pd.DataFrame(sleep_duration, columns=['sleep_duration']))
    return sleep_duration


cholesterol_levels = generate_cholesterol_data()
family_diabetes_history = generate_family_diabetes_history()
social_media_usage = generate_social_media_usage()
sleep_duration = generate_sleep_duration()


# Add new features to the existing DataFrame
existing_df['cholesterol_levels'] = cholesterol_levels
existing_df['family_diabetes_history'] = family_diabetes_history
existing_df['social_media_usage'] = social_media_usage
existing_df['sleep_duration'] = sleep_duration

# Saving the updated DataFrame back to a CSV file
existing_df.to_csv('updated_dataset.csv', index=False,)  


