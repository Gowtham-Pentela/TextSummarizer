# Text Summarizer

## Introduction
Text summarization is a crucial application of Natural Language Processing (NLP), particularly in scenarios where time is limited or vast amounts of text need to be condensed. This project implements a text summarization pipeline using state-of-the-art transformer models, providing an end-to-end solution for training, validating, and deploying a summarization model.

## Features
- **Data Pipeline**: Includes ingestion, validation, transformation, and training stages.
- **Model Training**: Fine-tunes a HuggingFace Transformer model on custom datasets.
- **Prediction API**: Provides a RESTful API for text summarization using FastAPI.
- **Deployment**: Dockerized application with CI/CD workflows for seamless deployment.
- **Logging**: Integrated logging for tracking pipeline execution.
- **Modular Design**: Clean and maintainable codebase with reusable components.

---
## Project Structure
```
.
├── app.py                 # FastAPI application for training and prediction
├── main.py                # Entry point for the training pipeline
├── config/
│   └── config.yaml        # Configuration file for pipeline stages
├── src/
│   ├── textSummarizer/
│   ├── pipeline/          # Pipeline stages for data processing and training
│   ├── components/        # Core components for each pipeline stage
│   ├── utils/             # Utility functions
│   ├── logging/           # Logging setup
│   ├── config/            # Configuration manager
│   ├── entity/            # Data classes for configuration
│   └── constants/         # Constants used across the project
├── research/              # Jupyter notebooks for experimentation
├── artifacts/             # Directory for storing intermediate and final outputs
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── .github/
│   └── workflows/         # CI/CD pipeline configuration
└── README.md              # Project documentation
```
---

## Installation

### Prerequisites
- Python 3.8 or higher
- Docker (optional, for deployment)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Gowtham-Pentela/TextSummarizer.git
   cd TextSummarizer
   ```
2. Create a virtual environment:
    ``` bash
    python -m venv textS
    source textS/bin/activate  # On Windows: textS\Scripts\activate
    ```
3. Install Dependencies
    ```bash 
    pip install -r requirements.txt
    ```
4. Set up the project structure:
    ```bash
    python template.py
    ```
---
## Usage
Training the Model
Run the following command to execute the training pipeline:
```bash
python main.py
```
---
## Running the API
Start the FastAPI server:
```bash
python app.py
```
The API will be available at `http://localhost:8080.`

#### Endpoints:
1. GET `/`: Redirects to API documentation.
2. GET `/train`: Triggers the training pipeline.
3. POST `/predict`: Accepts a text input and returns the summarized text.
---
## Deployment
Docker
1. Build the Docker image:
    ```bash
    docker build -t text-summarizer .
    ```
2. Run the container:
    ``` bash 
    docker run -p 8080:8080 text-summarizer
    ```
#### CI/CD
The project includes a GitHub Actions workflow for building and deploying the application. Update your Docker Hub credentials in the repository secrets to enable the pipeline.

---
#### Configuration

The `config/config.yaml` file contains all the configurable parameters for the pipeline stages. Update this file to modify the behavior of the pipeline.

---
#### Logging
Logs are stored in the `logs/` directory. You can monitor the pipeline execution by checking the running_logs.log file.

---
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
HuggingFace Transformers
FastAPI
Docker
GitHub Actions