import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from dotenv import load_dotenv
import psycopg2

load_dotenv()

class ModelTrainer:
    def __init__(self):
        self.model_dir = "models"
        os.makedirs(self.model_dir, exist_ok=True)

    def load_data_from_db(self, table_name):
        """Load data from PostgreSQL database"""
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST'),
                port=os.getenv('DB_PORT'),
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD')
            )
            
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, conn)
            conn.close()
            return df
        except Exception as e:
            print(f"Error loading data from database: {e}")
            return None

    def preprocess_data(self, df, target_column):
        """Prepare data for training"""
        try:
            # Separate features and target
            X = df.drop(columns=[target_column])
            y = df[target_column]
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            return X_train, X_test, y_train, y_test
        except Exception as e:
            print(f"Error in data preprocessing: {e}")
            return None

    def train_model(self, X_train, y_train):
        """Train machine learning model"""
        try:
            model = RandomForestRegressor(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)
            return model
        except Exception as e:
            print(f"Error training model: {e}")
            return None

    def evaluate_model(self, model, X_test, y_test):
        """Evaluate model performance"""
        try:
            predictions = model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            print(f"Model MSE: {mse}")
            return mse
        except Exception as e:
            print(f"Error evaluating model: {e}")
            return None

    def save_model(self, model, filename):
        """Save trained model to file"""
        try:
            file_path = os.path.join(self.model_dir, filename)
            with open(file_path, 'wb') as f:
                pickle.dump(model, f)
            return file_path
        except Exception as e:
            print(f"Error saving model: {e}")
            return None

if __name__ == "__main__":
    trainer = ModelTrainer()
    
    # Example usage:
    # df = trainer.load_data_from_db("processed_data")
    # X_train, X_test, y_train, y_test = trainer.preprocess_data(df, "target_column")
    # model = trainer.train_model(X_train, y_train)
    # mse = trainer.evaluate_model(model, X_test, y_test)
    # trainer.save_model(model, "model.pkl")
