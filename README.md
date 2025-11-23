<div align="center">

<img src="static/assets/images/logo/cryptosniff-logo.svg" alt="CryptoSniff Logo" width="200"/>

### _Advanced Machine Learning-Based Cryptojacking Detection System_

<br/>

[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/Pleiades-M45/CryptoSniff/actions)
[![Docker](https://img.shields.io/badge/Docker-GHCR-2496ED?logo=docker&logoColor=white)](https://ghcr.io/pleiades-m45/cryptosniff)
[![Flask](https://img.shields.io/badge/Flask-2.2+-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7.1-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)

<br/>

**[✨Live Demo✨](https://cryptosniff.onrender.com)** 
<br/>

_Protect your systems from unauthorized cryptocurrency mining with AI-powered detection_

</div>

## Overview

**CryptoSniff** is an advanced web-based cryptojacking detection system that leverages **machine learning algorithms** to identify malicious cryptocurrency mining activities on systems. The application analyzes system metrics and behavioral patterns to detect cryptojacking attempts with high accuracy.

### What is Cryptojacking?

Cryptojacking is a growing cybersecurity threat where attackers secretly use victims' computing resources to mine cryptocurrency. This can lead to:

- Increased CPU usage and system slowdowns
- Higher electricity costs
- Accelerated hardware degradation
- Potential security vulnerabilities

### Our Solution

CryptoSniff helps protect systems by providing **real-time detection capabilities** through:

- **CSV Batch Analysis** - Process multiple system logs at once
- **Manual Detection** - Test individual system metrics
- **AI-Powered Predictions** - Advanced ML models with confidence scoring
- **Visual Analytics** - Interactive charts and detailed reports

## Tech Stack

<div align="center">

### Backend Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

### Frontend Stack

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)

### DevOps & Deployment

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

</div>

<br/>

## Installation

### Prerequisites

```bash
# Required
✓ Python 3.11+
✓ pip (Python package manager)
✓ Git

# Optional
○ Docker (for containerized deployment)
○ Virtual environment tool (venv/conda)
```

---

### Quick Start (Local Setup)

**Step 1: Clone Repository**

```bash
git clone https://github.com/Pleiades-M45/CryptoSniff.git
cd CryptoSniff
```

**Step 2: Create Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

**Step 3: Install Dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run Application**

```bash
python app.py
```

**Step 5: Access Application**

```
Open browser: http://localhost:5000
```

</td>
</tr>
</table>

---

### Docker Setup

<table>
<tr>
<td width="50%">

**Option 1: Pull from GHCR**

```bash
# Pull latest image
docker pull ghcr.io/pleiades-m45/cryptosniff:latest

# Run container
docker run -p 5000:5000 \
  ghcr.io/pleiades-m45/cryptosniff:latest
```

</td>
<td width="50%">

**Option 2: Build Locally**

```bash
# Build image
docker build -t cryptosniff .

# Run container
docker run -p 5000:5000 cryptosniff
```

</td>
</tr>
</table>

```
Application running at: http://localhost:5000
```

---

### CSV Detection (Batch Analysis)

**CSV Format**

```csv
I/O Data Operations,I/O Data Bytes,...
1234.56,987654.32,...
2345.67,876543.21,...
```

_Column order must match training schema_

### Required System Metrics

<details>
<summary><b>Click to view all 14 required features</b></summary>

| #   | Metric Name              | Description                  | Example Value | Unit     |
| --- | ------------------------ | ---------------------------- | ------------- | -------- |
| 1   | I/O Data Operations      | Input/output operation count | 1234.56       | ops      |
| 2   | I/O Data Bytes           | Bytes transferred in I/O     | 987654.32     | bytes    |
| 3   | Number of Subprocesses   | Active child processes       | 5             | count    |
| 4   | Time on Processor        | CPU time consumed            | 12.34         | seconds  |
| 5   | Disk Reading/sec         | Disk read operations rate    | 456.78        | KB/s     |
| 6   | Disk Writing/sec         | Disk write operations rate   | 234.56        | KB/s     |
| 7   | Bytes Sent               | Network bytes transmitted    | 123456.78     | bytes    |
| 8   | Received Bytes (HTTP)    | HTTP bytes received          | 234567.89     | bytes    |
| 9   | Network Packets Sent     | Outbound packet count        | 1500          | packets  |
| 10  | Network Packets Received | Inbound packet count         | 2000          | packets  |
| 11  | Pages Read/sec           | Memory page reads            | 45.67         | pages/s  |
| 12  | Pages Input/sec          | Page file input rate         | 34.56         | pages/s  |
| 13  | Page Errors/sec          | Page fault rate              | 1.23          | errors/s |
| 14  | Confirmed Byte Radius    | Byte transmission radius     | 789.01        | bytes    |

</details>

---

## Project Structure

```
CryptoSniff/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions CI/CD pipeline
├── dataset/
│   ├── Train.csv               # Training dataset
│   ├── Test.csv                # Testing dataset
│   └── Variable_Definitions.csv
├── models/
│   ├── random_forest_model.pkl # Trained Random Forest model
│   ├── decision_tree_model.pkl # Trained Decision Tree model
│   ├── logistic_model.pkl      # Trained Logistic Regression model
│   ├── scaler.pkl              # Data scaler
│   └── feature_selector.pkl    # Feature selector
├── notebooks/
│   └── final.ipynb             # Model training notebook
├── static/
│   └── assets/
│       ├── css/                # Stylesheets
│       ├── js/                 # JavaScript files
│       ├── images/             # Images and logos
│       └── fonts/              # Custom fonts
├── templates/
│   ├── index.html              # Homepage
│   ├── detection.html          # CSV detection page
│   └── form_detection.html     # Manual detection page
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── .dockerignore               # Docker ignore rules
└── README.md                   # This file
```

## Author

<div align="center">

<img src="https://github.com/Pleiades-M45.png" width="100" style="border-radius: 50%"/>

### ✨**Pleiades-M45**✨

[![GitHub](https://img.shields.io/badge/GitHub-Pleiades--M45-00ff41?style=for-the-badge&logo=github)](https://github.com/Pleiades-M45)
[![Project](https://img.shields.io/badge/Project-CryptoSniff-00ff41?style=for-the-badge&logo=github)](https://github.com/Pleiades-M45/CryptoSniff)

</div>