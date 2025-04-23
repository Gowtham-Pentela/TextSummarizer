## Text Summarizer

## Introduction
Text summarization is a crucial application of Natural Language Processing (NLP), particularly in scenarios where time is limited or vast amounts of text need to be condensed. This repository documents the development and deployment process of a text summarization model, focusing on fine-tuning a HuggingFace Transformer model on custom data.

## Project Overview
This repository presents a detailed review of the end-to-end process, covering concepts such as fine-tuning Large Language Models (LLMs), data set description, project timeline, setup, development phases. It provides insights into modular coding practices, Dockerized deployments, and CI/CD workflows.

## Features
- Fine-tuning a HuggingFace Transformer model on custom data.
- Deployment of the model using AWS services such as EC2, ECR, and GitHub actions.
- Modular coding practices for better code organization and maintainability.
- Integration with FastAPI for creating a user interface.
- Continuous Integration and Continuous Deployment (CI/CD) workflows using GitHub actions.

### WorkFlows
1. Update config.yaml
2. Update params.yaml
3. Update entity 
4. Update configuration manager in src config
5. Update components
6. Update Pipeline
7. Update main.py
8. Update app.py

## Installation
To install the required dependencies, run:

``` pip install -r requirements.txt ```
