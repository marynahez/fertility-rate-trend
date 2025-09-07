# fertility-rate-trend
A small Python program that analyzes fertility rates over time.  
It allows users to input multiple data points (year + fertility rate),
then calculates the **average fertility rate** between a chosen start and end year
and identifies whether the trend is **upward**, **downward**, or **sideways**.  

---

## Features
- Accepts multiple fertility rate data points (year + value).  
- Prevents duplicate years (updates fertility rate instead).  
- Calculates average fertility rate between selected years.  
- Detects trends: upward 📈, downward 📉, or sideways ➡️.  

---

## How to run
1. Open the project in your Python environment (PyCharm, VS Code, or terminal).  
2. Run the file `main.py`.  
3. Enter the number of data points, then provide year + fertility rate for each.  
4. Choose start and end years to calculate the trend.  

---

## Examples

### Example 1 — Upward Trend  
How many data points do you have? 3  
What is the year of data point 1? 1000  
What is the fertility rate of data point 1? 2  
What is the year of data point 2? 2000  
What is the fertility rate of data point 2? 4  
What is the year of data point 3? 3000  
What is the fertility rate of data point 3? 6  
Which year would you like to start with? 1000  
Which year would you like to end with? 3000  
The average fertility rate of these two years is 4.00.  
There is an upward trend.  

### Example 2 — Sideways Trend  
How many data points do you have? 2  
What is the year of data point 1? 2024  
What is the fertility rate of data point 1? 2  
What is the year of data point 2? 2023  
What is the fertility rate of data point 2? 2  
Which year would you like to start with? 2023  
Which year would you like to end with? 2024  
The average fertility rate of these two years is 2.00.  
There is a sideways trend.  
