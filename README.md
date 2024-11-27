Summative Assignment: System Deployment Summary

Objective
The assignment involves deploying a Machine Learning classification model for plant disease recognition. The deployment process includes creating a complete ML pipeline, implementing cloud scalability, monitoring, and retraining capabilities, and demonstrating a production-ready system.
________________________________________
Key Deliverables
1.	Model Creation and Evaluation
o	A Machine Learning classification model will be developed offline using a dataset of plant diseases.
o	The model will be saved in .pkl or .tf formats.
o	Evaluation metrics will be demonstrated in a Jupyter Notebook to showcase the model's performance.

2.	Pipeline Development
o	Create Python-based functions for preprocessing, model training, prediction, and retraining.
o	Build an end-to-end pipeline for the entire process, ensuring the system can handle retraining when triggered by new data.

3.	Deployment on Cloud
o	Host the pipeline on a cloud platform to allow public access.
o	Include scalability features to handle high traffic, leveraging tools like Docker and cloud services.
o	Simulate high loads with Locust and analyze response times and latencies under different container setups.

4.	Desktop App
o	Develop a user-friendly Desktop app for:
	Uploading images for predictions.
	Viewing visualizations of key dataset features.
	Uploading bulk data to trigger model retraining.

5.	Functional Requirements
o	Model Prediction: Predict plant diseases from single data points (e.g., images).
o	Visualizations: Generate meaningful insights from at least three dataset features, illustrating patterns or trends.
o	Data Upload: Enable bulk data uploads for retraining purposes.
o	Retraining Trigger: Include a feature to initiate retraining manually with uploaded data.

6.	Documentation
o	GitHub Repository:
	Include a clear project structure with code, models, and documentation.
	Provide a README.md with setup instructions, project description, and results.
o	Notebook: Include all preprocessing, training, and testing functions.
o	Video Demo: Upload a YouTube video demonstrating the project.
________________________________________
Dataset Overview
The dataset used for training the model consists of approximately 87,000 RGB images of healthy and diseased plant leaves, categorized into 38 classes:
•	Training Data: 70,295 images.
•	Validation Data: 17,572 images.
•	Test Data: 33 images created for prediction purposes.
The dataset was enhanced using offline augmentation techniques to increase diversity and improve model robustness. It helps ensure accurate and reliable predictions by covering a wide range of plant diseases.
________________________________________
Why This System is Important
This system aims to provide:
•	Accurate Disease Detection: Leveraging state-of-the-art ML techniques for efficient analysis.
•	Accessibility: A user-friendly platform for farmers and researchers.
•	Efficiency: Rapid processing and predictions to facilitate timely interventions.
________________________________________
This project demonstrates the complete lifecycle of ML model development, deployment, and retraining while emphasizing scalability and user accessibility. The result will be a robust and production-ready system to aid in plant health management.
