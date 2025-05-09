# updating components
import os
from textSummarizer.logging import logger
from textSummarizer.config.configuration import DataValidationConfig
class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    # checks if the three files are present or not. Can add other modules like checking datatype of all files.
    def validate_files(self)-> bool:
        try:
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e