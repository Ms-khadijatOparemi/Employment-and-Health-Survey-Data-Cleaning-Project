# Employment-and-Health-Survey-Data-Cleaning-Project
This is an Employment and Health Survey data cleaning project from the Empovation virtual internship.



### Introduction
 
#### Messy Data Cleaning Challenge: Employment and Health Survey

#### Data Description:

The dataset contains 1656 rows of data with ten columns:
 • Name: Identity of person
 
 • Age: The current age of the individual
 
 • Gender: The preferred gender of the individual
 
 • City: The city in which the persona lives in
 
 • Education: Highest level of education attained (Missing, High School, Associate, 
 Bachelor's, Master's, PhD)
 
 • Employment Status: Current employment status (Unemployed, Employed, 
 Student, Self-employed, Retired, Gig Worker, Employed (Part-time), Employed 
 (Contract))
 
 • Salary: Annual or hourly income (may include inconsistencies in formatting and units)

 • Health Condition: Self-reported health status (Excellent, Good, Average, Poor, Missing)
 
• Credit Score: Numerical credit score (may include "N/A" for missing values)


#### Instruction:
1. Import the Data: You can use any spreadsheet software (Excel, Google Sheets) or data analysis tools (Python, R) to import the data.

 2. Identify Missing Values: Look for empty cells in each column and identify the number of missing entries.

 3. Analyze Formatting: Check for inconsistencies in formatting, particularly in the Salary column (e.g., presence of currency symbols, decimal places, hourly vs. annual income indicators).

 4. Address Outliers: Look for extreme values in the Salary and Credit Score columns that might not be representative of the data.
 
 5. Clean Employment Status: Review entries in the Employment Status column for potential typos or ambiguities (e.g., "Self-employed (Business Closed)").

 6. Validate Health Conditions: Ensure entries in the Health Condition column are consistent and represent valid options.

 7. Handle Credit Scores: Decide how to handle missing credit scores ("N/A") and consider potential inconsistencies (e.g., high credit score for a high school
graduate).
 
8. Document Your Changes: Keep track of the cleaning steps you take, the logic behind your decisions, and any assumptions made.


#### Cleaning Strategies:
• Use filters or conditional formatting to identify missing values and inconsistencies.
 
• Standardize formatting for entries in the Salary column (e.g., convert all values to a single unit like yearly income).

• Decide on a strategy for handling outliers: remove them, investigate them further, or cap them at a specific value.

• Consider creating new categories within the Employment Status column to represent better specific situations (e.g., "Business Closed" for self-employed).
 
• Verify options within the Health Condition column and remove or categorize any invalid entries.

• Decide whether to impute missing credit scores or leave them as "N/A" based on your analysis.

#### Deliverables:

• Provide a cleaned data version with addressed missing values, consistent formatting, and corrected inconsistencies.

• Document your cleaning process, including the cleaning steps taken, the decisions made, and any limitations of the cleaned data.




