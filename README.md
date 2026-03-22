Title: COVID-19 Global Trend Analysis

Project Overview:
This project analyzes global COVID-19 data using Python to identify trends, growth patterns, and country-wise insights. The dataset is transformed from wide format to long format to enable effective time-series analysis.

Objective:
- Analyze worldwide COVID-19 trends  
- Identify most affected countries  
- Study growth rate patterns  
- Detect peak infection periods  

Dataset:
- COVID-19 time series dataset  
- Initially in wide format (dates as columns)  
- Converted into long format using Pandas  

Technologies Used:
- Python  
- Pandas  
- Matplotlib  
- Seaborn  

Project Structure:
covid19-analysis-project/

data/ → dataset files  
src/ → source code  
main.py → main execution file  
data_loader.py → data loading  
data_cleaning.py → data transformation  
analysis.py → analysis logic  
visualization.py → plotting functions  

outputs/ → saved charts  
README.md  
requirements.txt  

Data Processing:
- Removed unnecessary columns  
- Converted wide format to long format using melt()  
- Converted date column to datetime  
- Removed null values and duplicates  

Analysis Performed:
- Global daily trend analysis  
- Country-wise total confirmed cases  
- Growth rate calculation  
- Peak day identification  
- Top affected countries  

Visualizations:
- Global trend line chart  
- Top countries bar chart  
- Growth rate plot  
- Distribution histogram  
- Scatter plot  

Key Insights:
- Identified the most affected country  
- Detected peak day of global cases  
- Observed growth rate fluctuations  
- Analyzed global spread patterns  

Skills Demonstrated:
- Data Cleaning  
- Exploratory Data Analysis  
- Data Transformation  
- Data Visualization  
- Python Programming  

Conclusion:
This project demonstrates how raw COVID-19 data can be transformed and analyzed to extract meaningful insights about global trends and the spread of the pandemic.