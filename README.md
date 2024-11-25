# Image Labels Generator

This project demonstrates how to use Flask and Amazon Rekognition to build an image labels generator. Users can upload images, which are stored in Amazon S3 and analyzed using Rekognition to generate descriptive labels with confidence scores.

---

## Features
- **Upload Images**: Upload images to Amazon S3 via a POST request.
- **Analyze Images**: Use Amazon Rekognition to identify objects, scenes, and other details in images.
- **Output Results**: Get a JSON response with labels and confidence scores.

---

## How to Run the Project

### Prerequisites
1. **AWS Account**:
   - Set up an S3 bucket and enable Amazon Rekognition.
   - Ensure the IAM role associated with your project has the following policies:
     - `AmazonS3FullAccess`
     - `AmazonRekognitionFullAccess`

2. **Python Environment**:
   - Install Python 3.9+.
   - Install `pip` (Python package manager).

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Harrygithubportfolio/Image-Labels-Generator.git
Navigate to the project directory:

bash
Copy code
cd Image-Labels-Generator
Set up a virtual environment:

bash
Copy code
python3 -m venv rekognition_env
source rekognition_env/bin/activate  # For macOS/Linux
rekognition_env\Scripts\activate     # For Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python3 app.py
Test the endpoints:

Upload an image:
bash
Copy code
curl -X POST -F "file=@/path/to/image.jpg" http://127.0.0.1:5000/upload
Analyze the uploaded image:
bash
Copy code
curl -X POST -H "Content-Type: application/json" \
-d '{"filename": "image.jpg"}' \
http://127.0.0.1:5000/analyze
AWS Services Used
Amazon S3: For image storage.
Amazon Rekognition: For analyzing images and generating descriptive labels.
Future Enhancements
Add a frontend with a simple file upload form and results display.
Deploy the application using AWS Elastic Beanstalk or EC2.
Implement user authentication to manage access to the service.
Sample Output
Here’s an example of the JSON response returned by the /analyze endpoint:

json
Copy code
{
  "labels": [
    {
      "Name": "Person",
      "Confidence": 99.99
    },
    {
      "Name": "Portrait",
      "Confidence": 98.75
    },
    {
      "Name": "Photography",
      "Confidence": 96.50
    }
  ]
}
Author
Harry Graham
This project was created to demonstrate cloud and Python development skills using AWS services.

