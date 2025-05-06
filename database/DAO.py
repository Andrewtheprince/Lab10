from database.DB_connect import DBConnect
from model.stato import Stato


class DAO:

    @staticmethod
    def getStati(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary = True)
        result = []
        query = """ SELECT co.StateNme as nomeStato1, co2.StateNme as nomeStato2
                    FROM contiguity c, country co, country co2
                    WHERE c.state1no = co.CCode and c.state2no = co2.CCode and c.year <= %s and c.conttype = 1
                    order by co.StateNme """
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStati():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """SELECT * FROM country c order by c.StateNme """
        cursor.execute(query)
        for row in cursor:
            result.append(Stato(**row))
        cursor.close()
        conn.close()
        return result

