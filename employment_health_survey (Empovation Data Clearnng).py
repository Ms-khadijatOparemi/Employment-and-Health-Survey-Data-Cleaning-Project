#!/usr/bin/env python
# coding: utf-8

# ## Introduction
# 
# Messy Data Cleaning Challenge: Employment and Health 
# Survey
# Data Description:
# 
# ##Data 
# The dataset contains 1656 rows of data with ten columns:
# • Name: Identity of person
# 
# • Age: The current age of the individual
# 
# • Gender: The preferred gender of the individual
# 
# • City: The city in which the persona lives in
# • Education: Highest level of education attained (Missing, High School, Associate, 
# Bachelor's, Master's, PhD)
# 
# • Employment Status: Current employment status (Unemployed, Employed, 
# Student, Self-employed, Retired, Gig Worker, Employed (Part-time), Employed 
# (Contract))
# 
# • Salary: Annual or hourly income (may include inconsistencies in formatting and 
# units)
# 
# • Health Condition: Self-reported health status (Excellent, Good, Average, Poor, 
# Missing)
# 
# • Credit Score: Numerical credit score (may include "N/A" for missing values)
# 
# 
# 

# #Instruction:#
#  1. Import the Data: You can use any spreadsheet software (Excel, Google Sheets) 
# or data analysis tools (Python, R) to import the data.
# 
# 2. Identify Missing Values: Look for empty cells in each column and identify the 
# number of missing entries.
# 
# 3. Analyze Formatting: Check for inconsistencies in formatting, particularly in the 
# Salary column (e.g., presence of currency symbols, decimal places, hourly vs. 
# annual income indicators).
# 
# 4. Address Outliers: Look for extreme values in the Salary and Credit Score 
# columns that might not be representative of the data.
# 
# 5. Clean Employment Status: Review entries in the Employment Status column 
# for potential typos or ambiguities (e.g., "Self-employed (Business Closed)").
# 
# 6. Validate Health Conditions: Ensure entries in the Health Condition column are 
# consistent and represent valid options.
# 
# 7. Handle Credit Scores: Decide how to handle missing credit scores ("N/A") and 
# consider potential inconsistencies (e.g., high credit score for a high school 
# graduate).
# 
# 8. Document Your Changes: Keep track of the cleaning steps you take, the logic 
# behind your decisions, and any assumptions made.
# 
# 

# #Cleaning Strategies:#
# • Use filters or conditional formatting to identify missing values and 
# inconsistencies.
# 
# • Standardize formatting for entries in the Salary column (e.g., convert all values to 
# a single unit like yearly income).
# 
# • Decide on a strategy for handling outliers: remove them, investigate them further, 
# or cap them at a specific value.
# 
# • Consider creating new categories within the Employment Status column to better 
# represent specific situations (e.g., "Business Closed" for self-employed).
# 
# • Verify options within the Health Condition column and remove or categorize any 
# invalid entries.
# 
# • Decide whether to impute missing credit scores or leave them as "N/A" based on 
# your analysis.
# 
# #Deliverables:#
# • Provide a cleaned version of the data with addressed missing values, consistent 
# formatting, and corrected inconsistencies.
# 
# • Document your cleaning process, including the cleaning steps taken, the 
# decisions made, and any limitations of the cleaned data.

# #### load Libraries

# In[1]:


#Import libraries

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #### Read  the File

# In[2]:


employment_health= pd.read_csv(r'C:\Users\USER\Desktop\EMPOVATION\DATA CLEANING VIRTUAL INTERNSHIP\Employment Survey Data.csv')


# In[3]:


employment_health.head(3)


# In[4]:


employment_health.tail()


# #### Understand the Data

# In[5]:


#Understand the shape of the dataset

employment_health.shape  


# In[6]:


employment_health.info()


# Based on the infomation 'id' and 'gender' columns are irrelevant and should be dropped.  Also 'age','salary' and 'credit_score' data format are not in the right way. They will be converted to 'int64'.

# In[7]:


employment_health.drop(columns=['ID','Gender'],inplace =True)


# In[8]:


# Change the column names in standardize form.
#Remove space,make it lower,replace space with undercore(_) 
employment_health.columns = employment_health.columns.str.strip().str.lower().str.replace(' ', '_')
employment_health.columns


# In[9]:


# Convert data types

#convert 'age' column to numeric
employment_health['age'] = pd.to_numeric(employment_health['age'], errors='coerce').astype('Int64')

# Remove non-numeric characters from salary and convert to numeric
employment_health['salary'] = employment_health['salary'].replace('[\$,]', '', regex=True).str.extract('(\d+\.?\d*)')[0].astype('Int64')

# Convert "credit_score" column to numeric
employment_health['credit_score'] = pd.to_numeric(employment_health['credit_score'], errors='coerce').astype('Int64')


# In[10]:


employment_health.info()


# In[11]:


employment_health.head(3)


# In[12]:


employment_health.duplicated().sum()


# In[13]:


employment_health.nunique()


# ### Data Cleaning

# In[14]:


# List of columns(Categogical variables) in your dataset
columns = employment_health[['city','education','employment_status','health_condition'
                       ]]

# Loop through each column and print the unique values
for column in columns:
    unique_values =employment_health[column].unique()
    print(f"Unique values in '{column}': {unique_values}")


# In[15]:


#Consolidated similar names into a single standardized form by using 'Mapping Approach'

# Define a mapping for the city names
city_mapping = {
    'Albuquerque': 'Albuquerque',
    'Albuque': 'Albuquerque',
    'ALBUQUERQUE': 'Albuquerque',
    'Atlanta': 'Atlanta',
    'Atl': 'Atlanta',
    'Baltimore': 'Baltimore',
    'Balti': 'Baltimore'
}

# Replace the city names in the dataset using the mapping
employment_health['city'] = employment_health['city'].replace(city_mapping)

# Verify the changes
unique_cities = employment_health['city'].unique()
print(unique_cities)


# In[16]:


# Define a mapping for the education
education_mapping = {
    'Bachelor': "Bachelor's",
    'Bachelors ': "Bachelor's",
    
}

# Replace the education names in the dataset using the mapping
employment_health['education'] = employment_health['education'].replace(education_mapping)



# Verify the changes
unique_education = employment_health['education'].unique()
print(unique_education)


# In[17]:


# Handle missing values
employment_health['education'] = employment_health['education'].fillna('Unspecified')

employment_health['education'].unique()


# In[18]:


#Use conditional statements to perform replacements

# Original list
employment_status = ['Employed', 'Unemployed', 'Self-employed', 'Retired', 'Student',
                 'Freelance', 'Student (Part-time)', 'Retired (Early)',
                 'Employed (Gig Work)', 'Student (Full-time)',
                 'Employed (Part-time)', 'Gig Worker', 'Employed (Contract)',
                 'Self-employed (Business Closed)', 'Student (Internship)']

# Define replacements
replacements = {
    'Employed':'Employed(Full-time)',
    'Self-employed (Business Closed)': 'Former Business Owner',
    'Employed (Gig Work)': 'Gig Worker'
}

# Perform replacements in the DataFrame
employment_health['employment_status'] = employment_health['employment_status'].replace(replacements)

# Verify the changes
unique_employment_status = employment_health['employment_status'].unique()
print(unique_employment_status)





# In[19]:


# Define a mapping for health_condition
health_mapping = {
    'Excellent (?!)': "Excellent",
    'Excellent ': "Excellent",
    
}

# Replace the healt_condition names in the dataset using the mapping
employment_health['health_condition'] = employment_health['health_condition'].replace(health_mapping)

# Verify the changes
unique_health_condition = employment_health['health_condition'].unique()
print(unique_health_condition)


# In[20]:


# Handle missing values
employment_health['health_condition'] = employment_health['health_condition'].fillna('Unspecified')

employment_health['health_condition'].unique()


# In[21]:


# Loop through each column and print the unique values
for column in columns:
    unique_values =employment_health[column].unique()
    print(f"Unique values in '{column}': {unique_values}")


# In[22]:


employment_health.info()


# 

# In[23]:


employment_health.head()


# ### Exploratory Data Analysis (EDA)
# 
# ##### Check for outliers in age, credit score and salary

# In[38]:


# Conducting descriptive analysis using the describe function and refining the output for better readability
employment_health.describe().T


# In[39]:


# Function to detect outliers using the IQR method
def detect_outliers_iqr(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = column[(column < lower_bound) | (column > upper_bound)]
    return outliers

# Check for outliers in the 'age' column
age_outliers = detect_outliers_iqr(employment_health['age'])
print("Outliers in 'age' column:")
print(age_outliers)


# In[26]:


# Check for outliers in the 'salary' column
salary_outliers = detect_outliers_iqr(employment_health['salary'])
print("\nOutliers in 'salary' column:")
print(salary_outliers)


# In[27]:


# Check for outliers in the 'credit_score' column
credit_score_outliers = detect_outliers_iqr(employment_health['credit_score'])
print("\nOutliers in 'credit_score' column:")
print(credit_score_outliers)


# ###### Visualize outliers

# In[28]:


# Create a 1x3 subplot to visualize outliers for age, salary, and credit score
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Box plot for 'age'
sns.boxplot(x=employment_health['age'], ax=axes[0])
axes[0].set_title('Age Distribution',fontweight='bold')
axes[0].set_xlabel('Age')

# Box plot for 'salary'
sns.boxplot(x=employment_health['salary'], ax=axes[1])
axes[1].set_title('Salary Distribution',fontweight='bold')
axes[1].set_xlabel('Salary')

# Box plot for 'credit_score'
sns.boxplot(x=employment_health['credit_score'], ax=axes[2])
axes[2].set_title('Credit Score Distribution',fontweight='bold')
axes[2].set_xlabel('Credit Score')


# Display the plots
plt.tight_layout()
plt.show()


# From the above:
# 
# age: With a median age of 30 years, older Indivuduals are the outliers as their age is significantly above the 75%(percentile) 41 years
# 
# There are no outliers in salary and credit_score distribution.

# ##### Find Correlation

# In[29]:


# Correlation analysis

corr_matrix = employment_health[['age','salary','credit_score']].corr()

print('Correlation Matrix:')
print(corr_matrix)


#Visualization (reate a scatterplot matrix)
sns.pairplot(corr_matrix)
plt.suptitle('Scatter Plot Matrix', y=1.02)
plt.show()




# In[30]:


# Heatmap of the correlation matrix
plt.figure(figsize = (8,6))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.show()



# There is no correlation between age and _credit_score
# There is a week correlation between age and salary
# There is a strong correlation between 'salary' and 'credit_score'

# In[31]:


employment_health.info()


# ### Since there are few null values in 'age', 'salary', and 'credit_score column' we will fill them with median value of each variable respectively.

# In[32]:


employment_health['age'] = employment_health['age'].fillna(employment_health['age'].median())
employment_health['salary'] = employment_health['salary'].fillna(employment_health['salary'].median())
employment_health['credit_score'] = employment_health['credit_score'].fillna(employment_health['credit_score'].median())



#The median is used because it is a nbetter measure than mean when daeling with outliers because:
#It is more roboust to ouliers because it focuses on middle values
#It is less affected by skewed distributions
#It provides a better representation of the typical valuein a datasese expeciallywhen utliers are present


# In[33]:


employment_health.info()


# In[34]:


employment_health.head()


# ### Pre-Processing
# 
# #### Create a categorized credit score column based on FICO system which isthe most widely used credit score system used in the USA

# In[35]:


# Define the function to categorize credit scores based on the FICO system
def categorize_credit_score(score):
    if pd.isna(score):
        return 'Unspecified'  # Handle NaN values
    elif score >= 300 and score <= 579:
        return 'Poor'
    elif score >= 580 and score <= 669:
        return 'Fair'
    elif score >= 670 and score <= 739:
        return 'Good'
    elif score >= 740 and score <= 799:
        return 'Very Good'
    elif score >= 800 and score <= 850:
        return 'Excellent'
    else:
        return 'Unspecified'  # For scores outside the FICO range or invalid scores

# Apply the function to create a new categorical column
employment_health['credit_score_category'] = employment_health['credit_score'].apply(categorize_credit_score)

# Display the first few rows of the updated dataset
print(employment_health[['credit_score', 'credit_score_category']].head())


# In[36]:


employment_health.head()


# In[37]:


employment_health.info()


# #### We have a clean and complete dataset with the right data type format

# In[ ]:




