import pymysql
import os
from dotenv import load_dotenv, find_dotenv
import locale


def connect_to_db():
    load_dotenv(find_dotenv())
    connection = pymysql.connect(
        host = os.getenv('host'),
        port = int(os.getenv('port')),
        user = os.getenv('user'),
        password = os.getenv('password'),
        database = os.getenv('db_name'),
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

def show_cars(connection : pymysql.connections.Connection):
    sort_filter = ''

    print('=' * 48)
    print('{:^48s}'.format("1. ID"))
    print('{:^48s}'.format("2. Release Year"))
    print('{:^48s}'.format("3. Engine Capacity"))
    print('{:^48s}'.format("4. Price"))
    print('=' * 48)
    print()
    select = int(input("Choose sort filter: "))
    match select:
        case 1: sort_filter += 'id'
        case 2: sort_filter += 'release_year'
        case 3: sort_filter += 'engine_capacity'
        case 4: sort_filter += 'price'
    
    print('=' * 48)
    print('{:^48s}'.format("1. Ascending"))
    print('{:^48s}'.format("2. Descending"))
    print('=' * 48)
    print()
    select = int(input("Choose sort filter: "))
    match select:
        case 1: sort_filter += ' ASC'
        case 2: sort_filter += ' DESC'

    query = f"""
        SELECT *
        FROM cars
        ORDER BY {sort_filter};
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        print('=' * 48)
        for row in rows:
            print(f"{row['id']}: {row['brand']} {row['model']} ({row['engine_capacity']}L)\nYEAR: {row['release_year']}\nCOLOR: {row['color']}\nPRICE: {locale.currency(row['price'], grouping = True)}")
        print('=' * 48)
        print()

def add_new_car(connection : pymysql.connections.Connection):
    print('=' * 48)
    brand = input('Car Brand: ')
    model = input('Model: ')
    release_year = int(input("Release Year: "))
    engine_capacity = float(input("Engine Capacity: "))
    color = input("Color: ")
    price = int(input("Price: "))
    query = f"""
        INSERT INTO cars (`brand`, `model`, `release_year`, `engine_capacity`, `color`, `price`)
        VALUES
        ('{brand}', '{model}', {release_year}, {engine_capacity}, '{color}', {price})
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
        print(f"CAR ADDED: {brand} {model} ({engine_capacity})\nYEAR: {release_year}\nCOLOR: {color}\nPRICE: {locale.currency(price, grouping = True)}\n")
        print('=' * 48)
        print()

def update_car_price(connection : pymysql.connections.Connection):
    print('=' * 48)
    id = int(input("ID: "))
    new_price = int(input("New price: "))
    old_price_query = f"""
        SELECT price
        FROM cars
        WHERE id = {id}
    """
    with connection.cursor() as cursor:
        cursor.execute(old_price_query)
        old_price = cursor.fetchall()[0]['price']
    set_new_price_query = f"""
        UPDATE cars
        SET price = {new_price}
        WHERE id = {id}
    """
    with connection.cursor() as cursor:
        cursor.execute(set_new_price_query)
        connection.commit()
    print(f'{old_price} -> {new_price}')

def show_cars_by_filter(connection : pymysql.connections.Connection):
    print('=' * 48)
    brand = input("(Leave the field blank if not needed)\nBrand: ")
    model = input("(Leave the field blank if not needed)\nModel: ")
    release_year_min = input("(Leave the field blanks if not needed)\nRelease Year:\nMIN_YEAR: ")
    release_year_max = input("MAX_YEAR: ")
    engine_capacity_min = input("(Leave the field blank if not needed)\nEngine Capacity:\nMIN_CAPACITY: ")
    engine_capacity_max = input("MAX_CAPACITY: ")
    color = input("(Leave the field blank if not needed)\nColor: ")
    price_min = input("(Leave the field blank if not needed)\nPrice:\nMIN_PRICE: ")
    price_max = input("MAX_PRICE: ")
    query = f"""
        SELECT *
        FROM CARS
        WHERE 
        brand {"IS NOT NULL" if len(brand) == 0 else f" = '{brand}'"} AND
        model {"IS NOT NULL" if len(model) == 0 else f" = '{model}'"} AND
        release_year {"IS NOT NULL" if len(release_year_min) == 0 and len(release_year_max) == 0 else f"BETWEEN {int('0' if len(release_year_min) == 0 else release_year_min)} AND {int('99999999' if len(release_year_max) == 0 else release_year_max)}"} AND
        engine_capacity {"IS NOT NULL" if len(engine_capacity_min) == 0 and len(engine_capacity_max) == 0 else f"BETWEEN {float('0.0' if len(engine_capacity_min) == 0 else engine_capacity_min)} AND {float('0' if len(engine_capacity_max) == 0 else engine_capacity_max)}"} AND
        color {"IS NOT NULL" if len(color) == 0 else f" = '{color}'"} AND
        price {"IS NOT NULL" if len(price_min) == 0 and len(price_max) == 0 else f"BETWEEN {int('0' if len(price_min) == 0 else price_min)} AND {int('0' if len(price_max) == 0 else price_max)}"}
    """
    print('=' * 48)
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        if len(rows) != 0:
            for row in rows:
                print(f"{row['id']}: {row['brand']} {row['model']} ({row['engine_capacity']}L)\nYEAR: {row['release_year']}\nCOLOR: {row['color']}\nPRICE: {locale.currency(row['price'], grouping = True)}")
        else:
            print("Nothing found... :(")
    print('=' * 48)
    print()

def delete_car(connection : pymysql.connections.Connection):
    print('=' * 48)
    id = int(input("ID: "))
    get_removed_car_query = f"""
        SELECT *
        FROM cars
        WHERE id = {id}
    """
    with connection.cursor() as cursor:
        cursor.execute(get_removed_car_query)
        removed_car_info = cursor.fetchall()
    print(f"{removed_car_info[0]['id']}: {removed_car_info[0]['brand']} {removed_car_info[0]['model']} ({removed_car_info[0]['engine_capacity']}L)\nYEAR: {removed_car_info[0]['release_year']}\nCOLOR: {removed_car_info[0]['color']}\nPRICE: {locale.currency(removed_car_info[0]['price'], grouping = True)}")
    print('{:^48s}'.format("WAS REMOVED"))
    query = f"""
        DELETE
        FROM cars
        WHERE id = {id}
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

def menu(connection):
    print()
    print()
    print()
    while True:
        print('=' * 48)
        print('{:^48s}'.format("Car Dealership Menu"))
        print('=' * 48)
        print('{:^48s}'.format('1. Add new car...'))
        print('{:^48s}'.format('2. View all cars...'))
        print('{:^48s}'.format('3. Edit car price...'))
        print('{:^48s}'.format('4. View all cars by filter...'))
        print('{:^48s}'.format('5. Delete car...'))
        print('{:^48s}'.format('0. Exit...'))
        print('=' * 48)
        print()
        select = int(input("Select an action: "))
        match select:
            case 1:
                add_new_car(connection)
            case 2:
                show_cars(connection)
            case 3:
                update_car_price(connection)
            case 4:
                show_cars_by_filter(connection)
            case 5:
                delete_car(connection)
            case _:
                break

def main():
    locale.setlocale(locale.LC_ALL, 'US')

    try:
        connection = connect_to_db()
        print("Successfully connected!")
        menu(connection)

    except Exception as ex:
        print('=' * 48)
        print('{:^48s}'.format("Connection refused... :("))
        print('=' * 48)
        print(ex)
        
    finally:
        print('=' * 48)
        print('{:^48s}'.format("Good bye!"))
        print('=' * 48)

if __name__ == '__main__':
   main()