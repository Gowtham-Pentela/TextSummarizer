from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_training import ModelTrainer
from textSummarizer.logging import logger 

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
         # initialize the configuration manager class
        config = ConfigurationManager() 

        # get the data Transformation config from the class
        model_trainer_config = config.get_model_trainer_config()
        
        # call the data Transformation components
        model_trainer = ModelTrainer(config=model_trainer_config)

        # call the data transformation method
        logger.info("Starting Training Model")
        model_trainer.train()
        logger.info("Model Training completed successfully")
    
