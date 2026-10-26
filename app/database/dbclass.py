from datetime import datetime, timedelta
import sqlite3
from app.schemas import *


class AssetDB:
    def __init__(self):
        # Make a connection 
        self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self, name: str):
        '''
        Create the table if it doesn't exist yet
        '''
        self.cur.execute(f"""
            CREATE TABLE IF NOT EXISTS {name} (
                id INTEGER PRIMARY KEY,
                date TEXT, 
                name TEXT,
                value FLOAT
            )"""
        )
        self.conn.commit()

    def drop_table(self, name: str):
        self.cur.execute(f""" DROP TABLE {name}""")
        self.conn.commit()

    def TS_get(self, body: AssetRequest) -> AssetResponse | None:
        query = f"""
            SELECT date, value
            FROM {body.db_name}
            WHERE date >= :init_date
            AND date <= :end_date
            AND name = :name
        """

        self.cur.execute(
            query,
            {
                "init_date": body.init_date,
                "end_date": body.end_date,
                "name": body.name
            }
        )

        results = self.cur.fetchall()

        if not results:
            return None

        values = {
        date: value
        for date, value in results
    }

        return AssetResponse(
            request="Time Series Getter",
            initial_date=body.init_date,
            end_date=body.end_date,
            name=body.name,
            values=values
        )

    def insert(self, body: AssetCreate) -> int:
        query = f"""
            INSERT INTO {body.db_name}
            (date, name, value)
            VALUES (:date, :name, :value)
        """

        self.cur.execute(
            query,
            {
                "date": body.date,
                "name": body.name,
                "value": body.value
            }
        )

        self.conn.commit()
        return self.cur.lastrowid

    def update(self, body: AssetUpdate) -> dict[str, str]:
        '''
        Fix it to get error handling. 
        '''
        query = f"""
            UPDATE {body.db_name} SET {body.field_to_set} = ? WHERE {body.condition}
        """
        self.cur.execute(query,(body.value))
        self.conn.commit()
        if self.cur.rowcount == 0:
            return {
                "status": "failed",
                "message": "No rows matched the condition."
            }
        else:
            return {
                "status": "success",
                "message": f"{self.cur.rowcount} row(s) updated."
            }
