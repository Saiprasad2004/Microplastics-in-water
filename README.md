# Microplastics-in-water
# 🌊 Microplastic Detection and Water Quality Analysis using YOLOv8

An AI-powered computer vision project that detects and classifies microplastic particles in water sample images using YOLOv8. The system automatically identifies different types of microplastics, estimates contamination levels, evaluates water usability, and provides treatment recommendations.

---

## 📌 Project Overview

Microplastic pollution has become a major environmental concern affecting drinking water, aquatic ecosystems, and human health. This project leverages Deep Learning and Object Detection to automatically detect microplastic particles from microscopic water sample images.

The model is trained using the YOLOv8 object detection framework and can classify microplastics into multiple categories such as:

- Fiber
- Fragment
- Film
- Pellet

After detection, the system generates a contamination report containing:

- Number of particles detected
- Pollution severity level
- Estimated contamination risk
- Water usability assessment
- Recommended treatment methods

---

## 🚀 Features

✅ Automatic microplastic detection from images

✅ Classification of different microplastic types

✅ YOLOv8-based real-time object detection

✅ Water contamination assessment

✅ Pollution severity estimation

✅ Risk percentage calculation

✅ Water usability analysis

✅ Treatment recommendations

✅ Visualization of detected particles

---

## 🏗️ Project Workflow

```text
Water Sample Image
        │
        ▼
YOLOv8 Detection Model
        │
        ▼
Microplastic Classification
(Fiber, Film, Fragment, Pellet)
        │
        ▼
Particle Counting
        │
        ▼
Risk & Pollution Analysis
        │
        ▼
Water Quality Report
```

---

## 📂 Dataset

The project uses a microplastic image dataset downloaded from Kaggle and Roboflow.

### Classes

| Class | Description |
|---------|-------------|
| Fiber | Thread-like plastic particles |
| Fragment | Broken plastic pieces |
| Film | Thin plastic sheet particles |
| Pellet | Small spherical plastic particles |

Dataset structure:

```text
MicroPlastic-7/
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── data.yaml
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Google Colab | Development Environment |
| YOLOv8 | Object Detection |
| Ultralytics | YOLO Framework |
| OpenCV | Image Processing |
| Matplotlib | Data Visualization |
| Kaggle API | Dataset Download |
| Roboflow | Dataset Management |

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/your-username/microplastic-detection.git

cd microplastic-detection
```

### Install Dependencies

```bash
pip install ultralytics
pip install opencv-python
pip install matplotlib
pip install roboflow
```

---

## 🎯 Model Training

The model is trained using YOLOv8 Nano.

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)
```

### Training Parameters

| Parameter | Value |
|------------|--------|
| Model | YOLOv8n |
| Epochs | 50 |
| Image Size | 640 × 640 |
| Batch Size | 16 |
| Task | Object Detection |

---

## 🔍 Performing Detection

Load the trained model:

```python
from ultralytics import YOLO

model = YOLO("best.pt")
```

Predict on an image:

```python
results = model.predict(
    source="sample.jpg",
    conf=0.25
)
```

---

## 📊 Water Quality Analysis

The project analyzes detected particles and generates a contamination report.

### Metrics Generated

- Fiber Count
- Fragment Count
- Film Count
- Pellet Count
- Total Particles
- Contamination Risk (%)
- Water Safety Level
- Recommended Treatment

### Pollution Classification

| Total Particles | Pollution Level |
|----------------|----------------|
| 0 – 4 | Low Pollution |
| 5 – 14 | Moderate Pollution |
| 15+ | High Pollution |

---

## 💧 Water Usability Assessment

The system estimates water usability based on detected contamination.

| Contamination Level | Water Status |
|--------------------|---------------|
| Low | Safe after basic filtration |
| Moderate | Additional treatment required |
| High | Not suitable for direct consumption |

---

## 🧪 Treatment Recommendations

### Low Pollution

- Basic filtration
- Sedimentation

### Moderate Pollution

- Activated carbon filtration
- Membrane filtration

### High Pollution

- Ultrafiltration
- Reverse Osmosis (RO)
- Advanced water treatment systems

---

## 📈 Example Output

```text
====== MICROPLASTIC ANALYSIS REPORT ======

Fiber: 2
Fragment: 1
Film: 2
Pellet: 3

Total Particles: 8

Contamination Level:
Moderate Pollution

Risk Percentage:
64%

Water Status:
Treatment Required

Recommended Treatment:
Activated Carbon Filtration
Membrane Filtration
```

---

## 📁 Project Structure

```text
microplastic-detection/
│
├── dataset/
│   ├── train/
│   ├── valid/
│   └── test/
│
├── runs/
│   └── detect/
│       └── train/
│           └── weights/
│               ├── best.pt
│               └── last.pt
│
├── notebooks/
│   └── microplastic.ipynb
│
├── images/
│
├── results/
│
├── requirements.txt
│
└── README.md
```

---

## 🔮 Future Improvements

- Real-time video-based microplastic detection
- Mobile application integration
- Water quality dashboard
- Cloud deployment
- Support for additional microplastic categories
- IoT-enabled monitoring system
- Automated environmental reporting

---

## 🌍 Applications

- Water Quality Monitoring
- Environmental Research
- Wastewater Treatment Plants
- Aquatic Ecosystem Assessment
- Pollution Control Authorities
- Academic Research
- Smart Environmental Monitoring Systems

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📜 License

This project is intended for educational and research purposes.

---

## 👨‍💻 Author

**Itachi Uchiha**

AI-Based Microplastic Detection and Water Quality Analysis using YOLOv8

---
⭐ If you found this project useful, consider giving the repository a star.
