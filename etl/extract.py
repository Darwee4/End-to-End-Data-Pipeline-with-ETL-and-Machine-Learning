import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

class DataExtractor:
    def __init__(self):
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)

    def extract_csv(self, file_path):
        """Extract data from CSV file"""
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None

    def extract_api(self, url, params=None):
        """Extract data from API"""
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching data from API: {e}")
            return None

    def save_raw_data(self, data, filename):
        """Save raw data to data directory"""
        try:
            file_path = os.path.join(self.data_dir, filename)
            if isinstance(data, pd.DataFrame):
                data.to_csv(file_path, index=False)
            else:
                pd.DataFrame(data).to_csv(file_path, index=False)
            return file_path
        except Exception as e:
            print(f"Error saving raw data: {e}")
            return None

if __name__ == "__main__":
    extractor = DataExtractor()
    
    # Example usage:
    # csv_data = extractor.extract_csv("data/sample.csv")
    # api_data = extractor.extract_api("https://api.example.com/data")
    # extractor.save_raw_data(api_data, "api_data.csv")
