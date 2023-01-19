import sqlite3


def find_rating(rait):
    """Получает рейтинг фильма возвращает список словарей в виде название, райтинг, описание"""
    result = []
    for i in range(len(rait)):
        with sqlite3.connect('././netflix.db') as connect:
            cursor = connect.cursor()
            sqlite_query = f"""
                            SELECT DISTINCT title, rating, description
                            FROM netflix
                            WHERE rating = '{rait[i]}'
                            AND type = 'Movie'
                            ORDER BY release_year ASC 
                            LIMIT 200                                             
                            """
            cursor.execute(sqlite_query)
            for row in cursor.fetchall():
                dict_db = {}
                dict_db['title'] = row[0]
                dict_db['rating'] = row[1]
                dict_db['description'] = row[2]
                result.append(dict_db)
    return result
