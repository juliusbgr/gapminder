# Gapminder Bubble Chart Dashboard

An interactive Streamlit dashboard visualizing Life Expectancy, Population, and GNI per Capita (PPP) over time using Gapminder data. Features an animated bubble chart with multi-country selection and year slider.

---

## Project Structure

```bash
app/
├── merged.csv # Merged & cleaned dataset used by the app
└── app.py # Streamlit dashboard application

Dockerfile # Docker container setup
README.md # This file
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- Docker

### Running Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run streamlit app

```bash
streamlit run app/app.py
```

3. Open your browser at http://localhost:8501

### Running with Docker

Build the image
```bash
docker build -t gapminder .
```
Run the container
```bash
docker run -p 8501:8501 -v /full/path/to/app:/app gapminder
```
Open http://localhost:8501 in your browser.

### Notes
- The app reads data from app/merged.csv.
- Data is filtered and visualized interactively with controls for selecting countries and year.
- The GNI axis uses a log scale for better visualization.
