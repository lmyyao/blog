import psycopg2
import random

with psycopg2.connect("dbname=lmy") as conn:
    cur = conn.cursor()
    score = 1

    for u in range(1, 10000):
        scores = []
        for i in range(random.choice(range(1,20))):
            userid = "user{0}".format(u)
            scores.append(score)
            score +=1
        cur.execute("insert into test1(userid, score) values (%s, %s)", (userid, scores))

        conn.commit()
    cur.close()
