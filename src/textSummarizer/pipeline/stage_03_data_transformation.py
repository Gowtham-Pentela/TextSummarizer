from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger 

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
         # initialize the configuration manager class
        config = ConfigurationManager() 

        # get the data Transformation config from the class
        data_transformation_config = config.get_data_transformation_config()
        
        # call the data Transformation components
        data_transformation = DataTransformation(config=data_transformation_config)

        # call the data transformation method
        logger.info("Starting data Transformation")
        data_transformation.convert()
        logger.info("Data Transformation completed successfully")
    
