import psycopg2
from config import *

try:
    conn = psycopg2.connect(
        user=user,
        password=password,
        database=db_name_1,
    )

    conn.autocommit = True
    print('[INFO] database connection start')

    # create table

    with conn.cursor() as cursor:
        create_script = '''CREATE TABLE if not exists user_test(
            id serial PRIMARY KEY,
            name varchar(32),
            second_name varchar(32),
            age int
        )'''

        cursor.execute(create_script)

    # insert into table some test data

    # with conn.cursor() as cursor:
    #     insert_script = '''insert into user_test (name, second_name, age) values (%s,%s,%s)'''
    #     insert_value = ('Aleksandr', 'Merc', 22)
    #
    #     cursor.execute(insert_script, insert_value)

    # select from table some data

    # with conn.cursor() as cursor:
    #     delete_lines_script = '''delete FROM USER_TEST where id between 6 and 16'''
    #     cursor.execute(delete_lines_script)

    # with conn.cursor() as cursor:
    #     cursor.execute('''DELETE from user_test where id in (3,4,5)''')

    # with conn.cursor() as cursor:
    #     change_script = '''UPDATE USER_TEST SET NAME = 'Aleksandr', SECOND_NAME = 'Merc', AGE = 22 where id = 2 '''
    #     cursor.execute(change_script)

    # with conn.cursor() as cursor:
    #     cursor.execute('''insert into user_test (name, second_name, age) values (%s,%s,%s)''',
    #                    ('Aleksandr', 'Merc', 22))

    with conn.cursor() as cursor:
        select_script = '''select * from user_test'''

        cursor.execute(select_script)
        content = cursor.fetchall()
        for line in content:
            print(line)

except Exception as _ex:
    print('[INFO] error', _ex)


finally:
    if conn:
        conn.close()
        print('[INFO] database connection end')
