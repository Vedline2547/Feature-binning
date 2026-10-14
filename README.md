# Feature Binning with Python

## Project Description

This project demonstrates **feature binning**, a feature engineering technique used in machine learning to transform continuous numerical data into categorical groups. Using the Churn Modelling dataset, customer ages are divided into age intervals using Pandas `pd.cut()`. The project then analyzes the distribution of customers across these age groups and visualizes the results using Matplotlib.

## Objectives

- Understand feature binning in data preprocessing.
- Convert continuous numerical age values into categorical features.
- Explore customer age distributions.
- Save the transformed data to a CSV file.
- Visualize the number of customers in each age group.

## Technologies Used

- **Python** — Programming language.
- **Pandas** — Data manipulation and feature binning.
- **NumPy** — Numerical computing.
- **Matplotlib** — Data visualization.
- **Seaborn** — Statistical data visualization library.
- **Scikit-learn** — Machine learning preprocessing tools.

## Dataset

The project uses the `Churn_Modelling.csv` dataset, which contains customer information, including age and other demographic and banking-related features.

The following columns are removed during preprocessing because they are identifiers or names rather than useful numerical predictors for this exercise:

- `RowNumber`
- `CustomerId`
- `Surname`

## Feature Binning

The `Age` feature is divided into four categories:

| Age Group | Bin Boundaries |
|---|---|
| 0–20 | 0 to 20 |
| 21–40 | Greater than 20 to 40 |
| 41–60 | Greater than 40 to 60 |
| Above 61 | Greater than 60 to 100 |

Pandas `pd.cut()` assigns each customer's age to the corresponding category and stores the result in a new column named `Age_bins`.

## Implementation

The project follows these steps:

1. Import the required Python libraries.
2. Load the customer churn dataset.
3. Inspect the dataset using `head()` and `info()`.
4. Remove unnecessary identifier columns.
5. Examine the minimum and maximum customer ages.
6. Define age intervals and category labels.
7. Apply feature binning using `pd.cut()`.
8. Export the age and age-group columns to `test.csv`.
9. Count customers in each age category.
10. Plot the age-group distribution using Matplotlib.

## Output

The project produces:

- A new categorical feature called `Age_bins`.
- A CSV file named `test.csv` containing the `Age` and `Age_bins` columns.
- A bar chart showing the number of customers in each age group.

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Vedline2547/Feature-binning.git
```

### 2. Navigate to the project directory

```bash
cd Feature-binning
```

### 3. Create and activate a virtual environment (optional but recommended)

On Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 5. Run the script

Ensure `Churn_Modelling.csv` is in the project directory, then execute:

```bash
python main.py
```

The script will display the customer age distribution and generate `test.csv`.

## Key Learnings

- Understanding feature engineering and data preprocessing.
- Applying numerical-to-categorical transformations.
- Using Pandas for data manipulation.
- Exporting processed data to CSV files.
- Visualizing categorical distributions with Matplotlib.

## Future Improvements

- Compare model performance before and after feature binning.
- Experiment with different age intervals.
- Apply binning to other numerical features.
- Explore quantile-based binning with `pd.qcut()`.
- Integrate the transformed features into a customer churn prediction model.

## Author

**Vedline Ochieng**

Aspiring AI Engineer | Python Developer | Machine Learning Enthusiast

GitHub: [Vedline2547](https://github.com/Vedline2547)
