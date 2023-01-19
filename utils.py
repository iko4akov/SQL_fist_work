import sqlite3
import json

def find_in_db(film_name):
    """Получает строку возвращает все совпадения с полученной строкой и названиями фильмов"""
    with sqlite3.connect('netflix.db') as connect:
        cursor = connect.cursor()
        sqlite_query = f"""
                        SELECT title, country, release_year, listed_in, description
                        FROM netflix 
                        WHERE title LIKE "%{film_name}%"
                        AND type = 'Movie'          
                        ORDER BY release_year DESC                        
                        LIMIT 10            
                        
                        """
        cursor.execute(sqlite_query)
        #Создаю пустой словарь для который дальше чкерез цикл заполняю
        result = []
        for row in cursor.fetchall():
            dict_db = {}
            dict_db['description'] = row[4]
            dict_db["genre"] = row[3]
            dict_db['release_year'] = row[2]
            dict_db['country'] = row[1]
            dict_db['title'] = row[0]
            result.append(dict_db)
        return result

    
def find_genre(genre):
    """Получает жанр и возвращает 10 фильмов самых свежих"""
    result = []
    with sqlite3.connect('netflix.db') as connect:
        cursor = connect.cursor()
        sqlite_query = f"""
                        SELECT title, description
                        FROM netflix 
                        WHERE listed_in = "{genre}"
                        AND type = 'Movie'          
                        ORDER BY release_year ASC                        
                        LIMIT 10           

                        """
        cursor.execute(sqlite_query)
        # Создаю пустой словарь для который дальше чкерез цикл заполняю
        for row in cursor.fetchall():
            print(row)
            dict_db = {}
            dict_db['title'] = row[0]
            dict_db['description'] = row[1]
            result.append(dict_db)
        return result

    
def serch_actors(name_one, name_two):
    """Получает два имени, возвращает список тех кто пересекается с этими двумя именами более 2х раз"""
    result = []
    with sqlite3.connect('netflix.db') as connect:
        cursor = connect.cursor()
        sqlite_query =(f"""
                       SELECT "cast"
                       FROM netflix 
                       WHERE "cast" LIKE "%{name_one}%"
                       AND "cast" LIKE '%{name_two}%'    
                       """)
        cursor.execute(sqlite_query)
        for row in cursor.fetchall():
            result.extend(row[0].split(", "))
        colleagues = []
        for name in result:
            if result.count(name) > 2 and name_two != name != name_one:
                colleagues.append(name)
        return set(colleagues)

    
def search_3_elems(type_r, year, genre):
    """Получает 3 значения
    возвращает список словарей в виде название фильма и описания"""
    with sqlite3.connect('netflix.db') as connect:
        cursor = connect.cursor()
        sqlite_query = (f"""
                       SELECT title, description
                       FROM netflix 
                       WHERE "type" = '{type_r}'
                       AND "release_year" = '{year}'
                       AND "listed_in" LIKE '%{genre}%'                        
                        """)
        cursor.execute(sqlite_query)
        result = []
        for row in cursor.fetchall():
            data_dict = {}
            data_dict['title'] = row[0]
            data_dict['description'] = row[1]
            result.append(data_dict)
        result_json = json.dumps(result, ensure_ascii=False)
        return result_json
