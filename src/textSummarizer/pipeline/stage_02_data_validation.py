from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger 

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
         # initialize the configuration manager class
        config = ConfigurationManager() 

        # get the data validation config from the class
        data_validation_config = config.get_data_validation_config()
        
        # call the data validation components
        data_validation = DataValidation(config=data_validation_config)

        # call the data validation method
        logger.info("Starting data validation")
        data_validation.validate_files()
        logger.info("Data validation completed successfully")
    
