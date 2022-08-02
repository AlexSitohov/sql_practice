import psycopg2
from config import *

try:
    conn = psycopg2.connect(
        password=password,
        user=user,
        database=db_name_2
    )
    print('database connection is up')
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute('''create table if not exists book(
                        id serial primary key,
                        name_of_book varchar(50),
                        author int,
                        publisher int)''')

    with conn.cursor() as cursor:
        cursor.execute('''create table if not exists author(
                        id serial primary key,
                        name_of_author varchar(50))''')

    with conn.cursor() as cursor:
        cursor.execute('''create table if not exists publisher(
                        id serial primary key,
                        name_of_publisher varchar(50))''')

    # with conn.cursor() as cursor:
    #     cursor.execute('''alter table book add constraint pk_book_author foreign key (author) references author(id)''')

    # with conn.cursor() as cursor:
    #     cursor.execute(
    #         '''alter table book add constraint pk_book_publisher foreign key (publisher) references publisher(id)''')

    # with conn.cursor() as cursor:
    #     cursor.execute('''alter table book rename author to author_id''')
    #

    # with conn.cursor() as cursor:
    #     cursor.execute('''alter table book rename publisher to publisher_id''')

    # with conn.cursor() as cursor:
    #     cursor.execute('''insert into author (name_of_author) values ('Miyadzakich')''')

    # with conn.cursor() as cursor:
    #     cursor.execute('''insert into publisher (name_of_publisher) values ('fromsoftware')''')

    # with conn.cursor() as cursor:
    #     cursor.execute('''insert into book (name_of_book, author_id, publisher_id) values (%s,%s,%s)''',
    #                    ('Elden Ring', 1, 1))

    with conn.cursor() as cursor:
        cursor.execute('''select name_of_book,name_of_author,name_of_publisher from book
                        natural join author 
                        natural join publisher 
                ''')
        print(cursor.fetchall())


except Exception as ex:
    print(ex)

finally:
    if conn:
        conn.close()
        print('database connection was close')
