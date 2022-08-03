<<<<<<< HEAD
import psycopg2

conn = psycopg2.connect(
    database="anythink-market",
    user='postgres',
    password='postgres',
    host='postgres',
    port='5432'
)

cursor = conn.cursor()

for i in range(100):
    cursor.execute("""INSERT INTO users(username, email, password) VALUES("user{i}", "user{i}@mail.com", "passwd{i}")""")
    cursor.execute("""INSERT INTO items(slug, title, description) VALUES("item{i}", "title{i}", "description for item {i}")""")
    cursor.execute("""INSERT INTO comments(body, item_id) VALUES("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ", {i})""")

cursor.close()
conn.close()
=======
print('Please fill the seeds file')
>>>>>>> origin/main
