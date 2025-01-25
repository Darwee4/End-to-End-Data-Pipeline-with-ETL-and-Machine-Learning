import pandas as pd
from datetime import datetime

class DataTransformer:
    def __init__(self):
        self.processed_dir = "data/processed"
        os.makedirs(self.processed_dir, exist_ok=True)

    def clean_data(self, df):
        """Perform basic data cleaning"""
        try:
            # Drop duplicates
            df = df.drop_duplicates()
            
            # Handle missing values
            df = df.fillna(method='ffill').fillna(method='bfill')
            
            # Convert date columns to datetime
            for col in df.columns:
                if 'date' in col.lower():
                    df[col] = pd.to_datetime(df[col], errors='coerce')
            
            return df
        except Exception as e:
            print(f"Error cleaning data: {e}")
            return None

    def feature_engineering(self, df):
        """Create new features from existing data"""
        try:
            # Example feature engineering
            if 'date' in df.columns:
                df['year'] = df['date'].dt.year
                df['month'] = df['date'].dt.month
                df['day'] = df['date'].dt.day
            
            return df
        except Exception as e:
            print(f"Error in feature engineering: {e}")
            return None

    def save_processed_data(self, df, filename):
        """Save processed data to processed directory"""
        try:
            file_path = os.path.join(self.processed_dir, filename)
            df.to_csv(file_path, index=False)
            return file_path
        except Exception as e:
            print(f"Error saving processed data: {e}")
            return None

if __name__ == "__main__":
    transformer = DataTransformer()
    
    # Example usage:
    # df = pd.read_csv("data/raw_data.csv")
    # cleaned_df = transformer.clean_data(df)
    # transformed_df = transformer.feature_engineering(cleaned_df)
    # transformer.save_processed_data(transformed_df, "processed_data.csv")
