import pandas as pd              # Import pandas for data handling
import matplotlib.pyplot as plt  # Import matplotlib for creating graphs


# ===========================================================
#               LOAD DATA FROM EXCEL FILE
# ===========================================================
# This function reads the Excel file and stores it
# in a DataFrame.

def load_data():
    df = pd.read_excel("movies.xlsx")
    return df


# ===========================================================
#           FIND AVERAGE RATING OF EACH MOVIE
# ===========================================================
# groupby("MovieName") creates groups based on movie names.
# mean() calculates the average rating of each movie.

def avg_movie(df):
    result = df.groupby("MovieName")["Rating"].mean()

    print("\nAverage Rating per Movie:")
    print(result)

    # Return the result so it can also be used for the bar chart.
    return result


# ===========================================================
#           FIND AVERAGE RATING GIVEN BY EACH USER
# ===========================================================
# Movies are grouped according to UserId and the
# average rating is calculated for every user.

def avg_user(df):
    result = df.groupby("UserId")["Rating"].mean()

    print("\nAverage Rating per User:")
    print(result)


# ===========================================================
#               FIND THE TOP RATED MOVIE
# ===========================================================
# First, calculate the average rating of every movie.
# Then find the highest average rating.
# Finally, display the movie whose rating matches
# the highest value.

def top_movie(df):
    avg = df.groupby("MovieName")["Rating"].mean()

    max_rating = max(avg)

    print("\nTop Rated Movie:")

    for movie, rating in avg.items():
        if rating == max_rating:
            print(movie, rating)


# ===========================================================
#               DISPLAY BAR CHART
# ===========================================================
# Creates a bar graph showing the average rating
# of every movie.

def bar_chart(avg):
    avg.plot(kind="bar", color="skyblue")

    plt.title("Average Rating per Movie")
    plt.xlabel("Movie")
    plt.ylabel("Rating")

    plt.show()


# ===========================================================
#               DISPLAY HISTOGRAM
# ===========================================================
# A histogram shows how ratings are distributed.
# bins=10 divides the graph into 10 sections.

def histogram(df):
    plt.hist(df["Rating"], bins=10, color="orange", edgecolor="black")

    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")

    plt.show()


# ===========================================================
#                     MENU DRIVEN PROGRAM
# ===========================================================
# Displays different options to the user and
# performs the selected operation.

def menu():

    # Load the Excel data once.
    df = load_data()

    while True:

        print("\n===== MENU =====")
        print("1. Average Rating per Movie")
        print("2. Average Rating per User")
        print("3. Top Rated Movie")
        print("4. Bar Chart")
        print("5. Histogram")
        print("6. Exit")

        ch = input("Enter your choice: ")

        # Average rating of every movie
        if ch == "1":
            avg = avg_movie(df)

        # Average rating given by every user
        elif ch == "2":
            avg_user(df)

        # Display the highest-rated movie
        elif ch == "3":
            top_movie(df)

        # Show bar graph
        elif ch == "4":
            avg = df.groupby("MovieName")["Rating"].mean()
            bar_chart(avg)

        # Show histogram
        elif ch == "5":
            histogram(df)

        # Exit the program
        elif ch == "6":
            print("Program Ended...")
            break

        # If user enters an invalid option
        else:
            print("Invalid Choice! Please try again.")


# ===========================================================
#               START THE PROGRAM
# ===========================================================

menu()


# ===========================================================
#                    EXAM SUMMARY
# ===========================================================
# ✔ read_excel() -> Reads an Excel file into a DataFrame.
#
# ✔ groupby() -> Groups data based on a column.
#
# ✔ mean() -> Calculates the average value.
#
# ✔ max() -> Finds the highest value.
#
# ✔ plot(kind="bar") -> Creates a bar chart.
#
# ✔ plt.hist() -> Creates a histogram.
#
# ✔ while True -> Repeats the menu until the user exits.
#
# ✔ Functions make the program modular, readable,
#   and easier to maintain.
# ===========================================================
