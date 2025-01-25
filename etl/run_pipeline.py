from extract import extract_data
from transform import transform_data
from load import load_data
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def run_pipeline():
    """Run the complete ETL pipeline"""
    try:
        logger.info("Starting ETL pipeline")
        
        # Load environment variables
        load_dotenv()
        
        # Extract phase
        logger.info("Extracting data")
        raw_data = extract_data()
        
        # Transform phase
        logger.info("Transforming data")
        processed_data = transform_data(raw_data)
        
        # Load phase
        logger.info("Loading data")
        load_data(processed_data)
        
        logger.info("ETL pipeline completed successfully")
        
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        raise

if __name__ == "__main__":
    run_pipeline()
