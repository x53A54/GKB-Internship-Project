Genre-Based Movie Recommender

I. Problem Statement
This project provides users with top-rated movie recommendations based on a selected genre. The results are based on aggregated user ratings from a publicly available dataset and are filtered to ensure they are reliable and relevant.

II. Technologies and Tools Used

1. Python 3
2. Pandas
3. Visual Studio Code (IDE)
4. CSV files: movies.csv, ratings.csv
5. Command Line Interface (CLI)

III. Project Description
The application processes two datasets — movies.csv and ratings.csv, taken from the MovieLens dataset.
When a user enters a genre, the program filters the movies by that genre, calculates the average rating and total number of ratings for each movie, and displays the top 5 results that have at least 10 user ratings.
If multiple movies have the same rating, you may optionally shuffle them to add variety.

IV. Key Features

1. Filters movies based on the user’s selected genre
2. Calculates average rating and counts how many people rated each movie
3. Shows only movies with a minimum of 10 ratings
4. Displays the top 5 highest-rated movies
5. Simple command-line interaction with clear output

V. How to Run the Project

1. Clone the repository:
   git clone <https://github.com/x53A54/GKB-Internship-Project>

2. Navigate to the project folder:
   cd Movie_Recommender


3. Install dependencies: (ensure Python and pip are installed)
   pip install pandas

4. Open the project in VS Code or Jupyter Notebook:
   Open main.py using your preferred IDE.

5. Run the cells in main.py sequentially

6. When prompted, enter a genre (e.g., Comedy, Action, Drama) to receive top movie recommendations.

VI. Note
The dataset used in this project is sourced from MovieLens(https://grouplens.org/datasets/movielens/).
If the output movies appear repetitive, it is because the sorting is done strictly by average rating. You can add randomization within movies having equal ratings if variety is needed.

Walkthrough Video:(https://www.loom.com/share/e84c25c828d344408fb73740c8c3ce54?sid=1b6b3c31-3877-4644-b0db-1fa61c35245c)

