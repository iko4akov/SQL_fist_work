import sqlite3

def find_in_db(user_input):
    """Поиск по словам в названии"""
    with sqlite3.connect('netflix.db') as connect:
        cursor = connect.cursor()
        sqlite_query = f"""
                        SELECT title, country, release_year, listed_in, description
                        FROM netflix 
                        WHERE title LIKE "%{user_input}%"
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
