import pandas as pd
import matplotlib.pyplot as plt

#load excel file
def load_data():
    df = pd.read_excel("movies.xlsx")
    return df

def avg_movie(df):
    result = df.groupby("MovieName")["Rating"].mean()
    print("\nAverage Rating per Movie:")
    print(result)
    return result   # needed for graph

# Average per user
def avg_user(df):
    result = df.groupby("UserId")["Rating"].mean()
    print("\nAverage Rating per User:")
    print(result)

# Top movie (simple loop)
def top_movie(df):
    avg = df.groupby("MovieName")["Rating"].mean()
    max_rating = max(avg)

    print("\nTop Rated Movie:")
    for movie, rating in avg.items():
        if rating == max_rating:
            print(movie, rating)

# Bar chart
def bar_chart(avg):
    avg.plot(kind="bar",color="skyblue")
    plt.title("Average Rating per Movie")
    plt.xlabel("Movie")
    plt.ylabel("Rating")
    plt.show()

# Histogram
def histogram(df):
    plt.hist(df["Rating"], bins=10, color="orange", edgecolor="black")
    plt.title("Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Count")
    plt.show()

# Menu
def menu():
    df = load_data()

    while True:
        print("\n===== MENU =====")
        print("1. Avg per movie")
        print("2. Avg per user")
        print("3. Top movie")
        print("4. Bar chart")
        print("5. Histogram")
        print("6. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            avg = avg_movie(df)

        elif ch == "2":
            avg_user(df)

        elif ch == "3":
            top_movie(df)

        elif ch == "4":
            avg = df.groupby("MovieName")["Rating"].mean()
            bar_chart(avg)

        elif ch == "5":
            histogram(df)

        elif ch == "6":
            break

        else:
            print("Invalid choice")

menu()