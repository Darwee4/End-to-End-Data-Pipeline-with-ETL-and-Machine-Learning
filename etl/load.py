import os
import psycopg2
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class DataLoader:
    def __init__(self):
        self.conn = None
        self.connect()

    def connect(self):
        """Connect to PostgreSQL database"""
        try:
            self.conn = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )
            return True
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return False

    def create_table(self, table_name, columns):
        """Create table in database"""
        try:
            with self.conn.cursor() as cursor:
                columns_with_types = ", ".join(
                    [f"{col} {dtype}" for col, dtype in columns.items()]
                )
                query = f"""
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        {columns_with_types}
                    )
                """
                cursor.execute(query)
                self.conn.commit()
                return True
        except Exception as e:
            print(f"Error creating table: {e}")
            return False

    def load_data(self, df, table_name):
        """Load data into PostgreSQL table"""
        try:
            with self.conn.cursor() as cursor:
                # Convert DataFrame to list of tuples
                data_tuples = [tuple(x) for x in df.to_numpy()]
                columns = ",".join(df.columns)
                
                # Create insert query
                insert_query = f"""
                    INSERT INTO {table_name} ({columns})
                    VALUES ({",".join(["%s"]*len(df.columns))})
                """
                
                cursor.executemany(insert_query, data_tuples)
                self.conn.commit()
                return True
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    loader = DataLoader()
    
    # Example usage:
    # df = pd.read_csv("data/processed_data.csv")
    # columns = {
    #     "column1": "VARCHAR(255)",
    #     "column2": "INTEGER",
    #     "column3": "DATE"
    # }
    # loader.create_table("example_table", columns)
    # loader.load_data(df, "example_table")
    # loader.close()
