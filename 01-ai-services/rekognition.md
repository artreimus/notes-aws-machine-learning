---
title: "Amazon Rekognition"
exam: "MLA-C01"
status: "draft"
domain:
  - "2.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
  - "01_ai_services"
aliases:
  - "Amazon Rekognition"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Amazon Rekognition

## 1. Overview

Amazon Rekognition is a cloud-based service that automates image and video analysis using machine learning. It provides pre-trained and customizable computer vision (CV) capabilities to extract information and insights from your visual data without requiring any machine learning expertise. Rekognition is designed to be highly scalable and is integrated with other AWS services like Amazon S3 and AWS Lambda, making it a powerful tool for building applications that need to understand visual content.

Its relevance in the AWS Machine Learning landscape stems from its position as one of the core AI Services. It abstracts the complexity of building, training, and deploying ML models for common computer vision tasks, allowing developers to add sophisticated AI-powered features to their applications quickly.

## 2. AWS Services & Features

Amazon Rekognition offers a wide range of features for both image and video analysis.

### Rekognition Image

- **Labels (Object and Scene Detection)**: Identifies thousands of objects (e.g., "car," "tree," "table") and scenes (e.g., "beach," "city," "sunset"). It also supports hierarchical labels.
- **Facial Analysis**: Detects faces in images and extracts attributes such as gender, age range, emotions (happy, sad, etc.), glasses, facial hair, and more.
- **Face Comparison and Search**: Compares a face in one image with faces in another, returning a similarity score. It can also search for a specific face against a "face collection," which is a searchable index of faces you have stored.
- **Celebrity Recognition**: Recognizes tens of thousands of celebrities in various categories.
- **Text in Image**: Detects and extracts text from images, which is useful for applications like reading road signs, license plates, or text in documents.
- **Unsafe Content Detection**: Identifies explicit and suggestive adult content, as well as violent content, enabling content moderation workflows.
- **Custom Labels**: Allows you to train your own custom model to detect objects and scenes specific to your business needs (e.g., identifying your company logo, specific machine parts on an assembly line).

### Rekognition Video

Rekognition Video analysis can be performed on both videos stored in Amazon S3 and on real-time streaming video.

- **Label, Object, and Activity Detection**: Tracks the detection of objects and their movement throughout a video. It can also identify activities like "playing football" or "delivering a package."
- **Person Tracking**: Tracks the path of multiple people in a video frame.
- **Content Moderation**: Detects unsafe content in videos, providing timestamps for when such content appears.
  -. **Face Liveness Detection**: Helps verify that a user is physically present in front of a camera and not a spoofed image or video. This is crucial for preventing fraud in identity verification systems.
- **Celebrity Recognition**: Identifies when and where celebrities appear in a video.
- **Face Search**: Searches for faces from a collection within a stored video, providing timestamps for each match.
- **Text in Video**: Extracts text from videos, along with timestamps.

## 3. Practical Application

### Sample Architecture: Automated Image Tagging and Content Moderation

A common use case is to automatically analyze and tag images uploaded to an S3 bucket.

1.  **Upload**: A user uploads an image to a designated Amazon S3 bucket.
2.  **Trigger**: The S3 `PutObject` event triggers an AWS Lambda function.
3.  **Analyze**: The Lambda function calls the Amazon Rekognition `DetectLabels` and `DetectModerationLabels` APIs, passing the S3 object information.
4.  **Store & Act**:
    - The Lambda function stores the labels and moderation results in an Amazon DynamoDB table, indexed by the image key.
    - If moderation labels are found, the function can automatically move the image to a restricted S3 folder for manual review and flag the content in the database.
5.  **Search/Serve**: A web application can then query the DynamoDB table to allow users to search for images by their content labels or to display moderated content differently.

### Other Real-World Scenarios

- **Media and Entertainment**: Automatically generating metadata for large media archives, enabling searchable video content. Broadcasters use it for content moderation and to place contextual ads.
- **Public Safety**: Law enforcement agencies can use face search to find missing persons or identify persons of interest from video footage (use of this technology is subject to legal and ethical guidelines).
- **Retail**: Analyzing in-store camera footage to understand customer demographics, dwell time in certain aisles, and foot traffic patterns to optimize store layout.
- **Identity Verification**: Onboarding new customers by comparing a selfie with a photo from an ID card using the `CompareFaces` API and verifying liveness.

## 4. Challenges & Best Practices

### Challenges

- **Accuracy & Bias**: The accuracy of detections can be affected by image quality (resolution, lighting, angle). Facial analysis models can exhibit bias across different demographic groups, leading to fairness and ethical concerns.
- **Confidence Thresholds**: The API returns a confidence score for every label or face match. Choosing an appropriate threshold is critical; too low can lead to false positives, and too high can lead to false negatives.
- **Cost Management**: Analyzing large volumes of video can be expensive. Processing every frame of a long, high-resolution video might not be cost-effective.
- **Managing Face Collections**: For large-scale face search applications, managing the lifecycle of face collections (adding, deleting, and organizing faces) requires careful application design.

### Best Practices

- **Use Confidence Scores**: Don't treat all results as equal. Use the confidence score to filter out low-confidence predictions. For high-accuracy use cases like identity verification, AWS recommends a face match similarity threshold of 99% or higher.
- **Follow Responsible AI Practices**: Be aware of the ethical implications of using facial recognition. Always follow AWS's guidance on responsible AI. For public safety use cases, it should be used to assist human reviewers, not for fully autonomous decisions.
- **Optimize for Cost**: For stored video analysis, process videos at a lower frame rate if real-time precision is not required. Use notification handlers (`AmazonSQS` and `AmazonSNS`) to track the completion of asynchronous video analysis jobs instead of polling.
- **Leverage Custom Labels**: When built-in labels are insufficient, use Rekognition Custom Labels to train a model on your specific data. Start with a small, high-quality dataset (as few as 10 images per label) and iterate.
- **Pre-process Images**: For best results, provide images where the subject is clear, well-lit, and in-focus.

## Sources

- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/mla-01-in-scope-services.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
