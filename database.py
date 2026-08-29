import sqlite3
from datetime import date

DATE = date.today()

# init_db (run once in main)

def init_db():
    with sqlite3.connect("main.db") as con:
        # cursor obj for commands
        crs = con.cursor()

        # make table

        crs.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                subreddit TEXT,
                score INTEGER
            )
        """)

        crs.close()
    return

# add a new post
# default date is today
def save_post(sub, score, date=DATE):
    with sqlite3.connect("main.db") as con:
            # cursor obj for commands
            crs = con.cursor()

            new_post = (date, sub, score)
    
            crs.execute("""
                INSERT INTO posts (
                    date, subreddit, score)
                VALUES (?,?,?) """, 
                new_post
            )

            crs.execute("COMMIT")
    
            crs.close()
    return

# return day's avg score
# default is today
def avg_day_score(target_date=DATE):
    with sqlite3.connect("main.db") as con:
        # cursor obj for commands
        crs = con.cursor()

        today_posts = crs.execute("""
            SELECT score
            FROM posts
            WHERE date = target_date
            """
        )

        results = today_posts.fetchall()
        scores = []
        for row in results:
            scores.append(row[-1])

        # if no posts added for day, return None
        if len(scores) == 0:
            print("No results for the day: " + str(target_date))
            avg = None
        else:
            avg = sum(scores) / len(scores) # return float

        crs.close()
    return avg