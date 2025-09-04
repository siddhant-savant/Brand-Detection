# **Machine Learning based Brand Detection & Market Analytics**

## **Overview**

This project was developed as part of my MSc Data Science dissertation. It leverages web scraping, machine learning, and data analytics to help brands monitor and optimize their presence in the e-commerce marketplace. It integrates automated data collection, object detection, and KPI analysis to provide actionable insights on stock availability, pricing, and brand visibility.

### **Features**

  - Automated Web Scraping: Collects daily product, price, and availability data from major from e-commerce retailers.

  - Object Detection: TensorFlow 2 with ResNet50 and EfficientDet D2 architectures to detect and classify products from images.

### **KPI Analysis:**

  - Stock Monitoring

  - Price Tracking

  - Share of Shelf

  - Brand Exposure

### **Insights:**

  - Identify trends, compare competitor performance, and monitor brand exposure over time with the use of machine learning models.

### **Installation**

Clone the repository:

    git clone https://github.com/siddhant-savant/Brand-Detection.git
    cd Brand-Detection


Create and activate a Python environment (Anaconda recommended):

    conda create -n brand_detection python=3.8
    conda activate brand_detection

### **Usage**

  - Web Scraping: Run scripts in the Scripts/ folder to collect daily product data.

  - Model Training: Label images using LabelImg

  - Train object detection models in TensorFlow 2 using the provided scripts

  - Analysis: Generate business intelligence (BI) analytics using KPIs such as stock availability, pricing trends, and share of shelf metrics to derive actionable insights.

### **Folder Structure**

        Brand-Detection/
        │
        ├── models/           # Object detection model files
        └── Scripts/          # Python scripts for scraping data and sample output files

### **Future Work**

  - Predictive modeling for pricing trends

  - Expansion to additional retailers and brands

  - Improved object detection using more advanced architectures

  - Automating alerts for stock and price changes
