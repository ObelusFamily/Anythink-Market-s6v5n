<<<<<<< HEAD

from sqlalchemy import create_engine

database_url = "postgresql://postgres:@postgres-python:5432/anythink-market"

engine = create_engine(database_url, echo=True)

with engine.connect() as con:
    for i in range(100):
        con.execute("""INSERT INTO users(username, email, hashed_password) VALUES("user{i}", "user{i}@mail.com", "passwd{i}")""")
        con.execute("""INSERT INTO items(slug, title, description, seller_id) VALUES("item{i}", "title{i}", "description for item {i}", {i}{i})""")
        con.execute("""INSERT INTO comments(body, seller_id, item_id) VALUES("comment{i}", {i}{i}, {i})""")
=======
print('Please fill the seeds file')
>>>>>>> refs/remotes/origin/main
