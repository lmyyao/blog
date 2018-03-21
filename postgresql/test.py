import psycopg2
import random

with psycopg2.connect("dbname=lmy") as conn:
    cur = conn.cursor()
    score = 1

    for u in range(1, 10000):
        for i in range(random.choice(range(1,20))):
            userid = "user{0}".format(u)

            cur.execute("insert into test(userid, score) values (%s, %s)", (userid, score))
            score +=1
        conn.commit()
    cur.close()
