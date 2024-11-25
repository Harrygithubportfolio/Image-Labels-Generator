import boto3
from flask import Flask, request, jsonify

app = Flask(__name__)

# AWS Configuration
S3_BUCKET = "image-label-generator-1234"  # Replace with your bucket name
REGION = "eu-west-2"  # Replace with your AWS region

# AWS Clients
s3_client = boto3.client('s3', region_name=REGION)
rekognition_client = boto3.client('rekognition', region_name=REGION)

# Home Route
@app.route('/')
def home():
    return "Welcome to the Image Label Generator!"

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filename = file.filename

    try:
        # Upload file to S3
        s3_client.upload_fileobj(file, S3_BUCKET, filename)
        file_url = f"https://{S3_BUCKET}.s3.{REGION}.amazonaws.com/{filename}"
        return jsonify({"message": "File uploaded successfully", "url": file_url, "filename": filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'filename' not in request.json:
        return jsonify({"error": "No filename provided"}), 400

    filename = request.json['filename']

    try:
        # Call Rekognition
        response = rekognition_client.detect_labels(
            Image={'S3Object': {'Bucket': S3_BUCKET, 'Name': filename}},
            MaxLabels=10
        )
        labels = [{"Name": label['Name'], "Confidence": label['Confidence']} for label in response['Labels']]
        return jsonify({"labels": labels})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
# 