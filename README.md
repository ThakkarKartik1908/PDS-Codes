# Python for Data Science Lab

This repository contains the practical programs and mini-projects performed as part of the **Python for Data Science Lab.** 

## Practical List

### Practical 1: Python Fundamentals & Control Flow

**Objective:**  
To understand Python syntax, variables, data types, and control structures.

**Tasks:**

1. Write a program to check if a given year is a leap year.
2. Write a program to generate the Fibonacci series up to `n` terms using a while loop.
3. Write a program to print various star patterns such as right-angled triangle and pyramid using nested for loops.
4. Build a simple command-line Calculator using if-elif-else statements that performs addition, subtraction, multiplication, and division based on user input.

---

### Practical 2: Strings, Functions, and Data Structures

**Objective:**  
To implement functions and manipulate Python data structures such as Lists, Tuples, Sets, and Dictionaries.

**Tasks:**

1. Write a function to check whether a given string is a palindrome.
2. Create a list of numbers. Find the maximum and minimum number without using built-in functions and remove duplicates by converting the list to a set.
3. Write a program to count the frequency of each character in a given string using a Dictionary.
4. Create a dictionary of students with their names as keys and marks as values. Sort the dictionary by values (marks) in descending order.

---

### Practical 3: File Handling & Exception Handling

**Objective:**  
To read/write text, CSV, and JSON files, and handle runtime errors using exceptions.

**Tasks:**

1. Write a program to read a text file, count the number of words, lines, and characters, and write the output to a new file.
2. Use the `csv` module to create a CSV file containing student details (Name, Roll No, CGPA). Read the CSV and display only students with CGPA greater than 7.5.
3. Create a JSON file containing book details (Title, Author, Price). Read and parse the JSON file to display the details.
4. Write a program that deliberately divides a number by zero and handles the `ZeroDivisionError`. Also handle `FileNotFoundError` when trying to open a non-existent file.

---

### Practical 4: Basic Statistics & Probability

**Objective:**  
To calculate measures of central tendency, dispersion, and understand basic probability using Python.

**Tasks:**

1. Write a Python program using the `statistics` module to calculate Mean, Median, Mode, Variance, and Standard Deviation for a given list of student marks.
2. Create two lists representing Math and Science scores. Calculate the Covariance and Correlation Coefficient between them using basic Python formulas or NumPy.
3. Simulate rolling a six-sided die 1000 times using the `random` module. Plot the frequency distribution of the outcomes using basic text output or a simple bar chart.
4. Calculate the probability of drawing an Ace from a standard deck of 52 cards using a Python simulation.

---

### Practical 5: Introduction to NumPy

**Objective:**  
To perform numerical computations using NumPy arrays.

**Tasks:**

1. Create a 1D array of 10 elements and a 2D array of shape `(3,4)`. Perform basic arithmetic operations such as addition and multiplication.
2. Demonstrate NumPy indexing and slicing. Extract the 2nd row and 3rd column from a 4×4 matrix. Replace all even numbers in the matrix with `-1`.
3. Use NumPy built-in functions: `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, and `np.reshape`.
4. Generate two random 3×3 matrices. Perform matrix multiplication, find the transpose, and calculate the determinant of the result.

---

### Practical 6: Data Manipulation with Pandas (Series & DataFrames)

**Objective:**  
To create and manipulate Pandas Series and DataFrames.

**Tasks:**

1. Create a Pandas Series from a list and a dictionary. Perform slicing and basic arithmetic on the Series.
2. Create a DataFrame from a dictionary containing Employee details (ID, Name, Dept, Salary).
3. Load a sample CSV file such as `train.csv` or `iris.csv` into a DataFrame. Display the first 5 and last 5 rows. Use `.info()`, `.describe()`, and `.shape` to understand the data.
4. Select specific columns and filter rows where the Salary/Age is greater than a certain threshold using `.loc` and `.iloc`.

---

### Practical 7: Data Cleaning & Aggregation with Pandas

**Objective:**  
To handle missing data and perform grouping operations.

**Tasks:**

1. Create a DataFrame with some NaN (null) values. Practice dropping rows with `dropna()` and filling missing values with mean/median using `fillna()`.
2. Given a dataset of sales containing Region, Salesperson, and Profit columns, use `groupby()` to find the total profit per Region and the average profit per Salesperson.
3. Use the `merge()` or `join()` function to combine two DataFrames, such as an Employee Details DataFrame and a Salary Details DataFrame, based on Employee ID.
4. Use `pivot_table()` to summarize data, such as average sales by Region and Product Category.

---

### Practical 8: Data Visualization with Matplotlib

**Objective:**  
To create standard plots using Matplotlib to find trends in data.

**Tasks:**

1. Plot a Line graph showing the monthly sales of a company. Add a title, x-axis label, y-axis label, and a legend.
2. Create a Bar chart comparing the marks of 5 students in Math vs. Science.
3. Generate a Scatter plot to show the relationship between study hours and exam scores.
4. Create a Histogram to show the distribution of ages in a given dataset.

---

### Practical 9: Advanced Visualization with Seaborn

**Objective:**  
To create statistical and aesthetically pleasing graphics using Seaborn.

**Tasks:**

1. Load the built-in `tips` or `iris` dataset from Seaborn.
2. Create a Boxplot to visualize the distribution of total bills across different days of the week.
3. Plot a Heatmap of the correlation matrix of the Iris dataset. Annotate the heatmap with correlation values.
4. Create a Pairplot to visualize pairwise relationships in the dataset, colored by the species/target column.

---

### Practical 10: Mini-Project – Exploratory Data Analysis (EDA)

**Objective:**  
To apply data loading, cleaning, and statistical analysis to a real-world dataset.

**Tasks:**

1. Download a real-world dataset, such as the Titanic Dataset from Kaggle.
2. Load the data using Pandas. Identify and handle missing values appropriately.
3. Extract statistical insights such as Mean, Median, and Standard Deviation for numerical columns.
4. Identify and remove duplicate rows if any. Convert categorical text data into numerical formats if necessary, such as Gender to 0/1.

---

## Beyond Syllabus

### B.S. Practical 1: Mini-Project – Exploratory Data Analysis (EDA)

**Objective:**  
To perform advanced data manipulation and visual storytelling.

**Tasks:**

1. Use `groupby()` to find survival rates by gender and passenger class or equivalent dataset metrics.
2. Create at least 4 different visualizations using Matplotlib/Seaborn to represent findings, such as:
   - Bar chart for survival by class
   - Histogram for age distribution
   - Heatmap for feature correlation
3. Write a brief text summary within the Jupyter Notebook/Python script explaining what each graph represents and the business insights derived from it.

---

### B.S. Practical 2: Revision & Open-ended Problem Solving

**Objective:**  
To test the overall understanding of the Python for Data Science pipeline within a time limit.

**Tasks:**

1. Instructor provides a messy CSV dataset.
2. Students are required to write a complete Python script within the 2-hour window that:
   - Reads the CSV.
   - Cleans the data by handling nulls and outliers.
   - Computes basic statistics.
   - Merges or groups the data to answer a specific analytical question provided by the instructor.
   - Generates one final visualization that answers the question.

---

## Datasets

The following standard datasets are used for Practicals 6, 7, 10, and Beyond Syllabus practicals.

### Titanic Dataset

Used for data analysis, cleaning, and exploratory data analysis.

[Download Titanic Dataset](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv)

### Iris Dataset

Used for Pandas and Seaborn data analysis and visualization.

[Download Iris Dataset](https://github.com/mwaskom/seaborn-data/blob/master/iris.csv)

---

## Technologies & Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Statistics
- Random
- CSV
- JSON

---

