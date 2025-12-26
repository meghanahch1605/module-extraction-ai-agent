# module-extraction-ai-agent
## 📌 Module Extraction AI Agent

### Overview

This project is an AI-powered Streamlit application that automatically extracts **modules**, **submodules**, and their **descriptions** from documentation-based help websites. The system crawls documentation pages, processes structured content, and outputs a clean JSON representation of product features.

This tool is designed to help product and engineering teams quickly understand the functional structure of complex documentation.

---

### 🚀 Features

* Accepts one or more documentation URLs
* Recursively crawls relevant documentation pages
* Extracts meaningful content (headings, paragraphs, lists)
* Infers:

  * **Modules** (top-level features)
  * **Submodules** (actions or functionalities)
* Generates structured JSON output
* Interactive Streamlit UI for easy usage
* Graceful handling of invalid URLs and broken links

---

### 🏗️ Architecture

```
User URL
  ↓
URL Validation
  ↓
Recursive Crawler
  ↓
HTML Content Parser
  ↓
Module & Submodule Inference Agent
  ↓
Structured JSON Output
  ↓
Streamlit UI
```

---

### 🛠️ Tech Stack

* Python 3
* Streamlit
* Requests
* BeautifulSoup
* lxml

---

### ▶️ How to Run

#### 1. Install dependencies

```bash
pip install -r requirements.txt
```

#### 2. Run the application

```bash
python -m streamlit run app.py
```

#### 3. Open browser

```
http://localhost:8501
```

---

### 🧪 Tested Documentation URLs

The application was tested on the following documentation websites:

1. [https://www.chargebee.com/docs/2.0/](https://www.chargebee.com/docs/2.0/)
2. [https://wordpress.org/documentation/](https://wordpress.org/documentation/)
3. [https://help.zluri.com/](https://help.zluri.com/)
4. [https://support.neo.space/hc/en-us](https://support.neo.space/hc/en-us)

---

### 📤 Output Format

```json
[
  {
    "module": "Module Name",
    "Description": "Detailed description of the module",
    "Submodules": {
      "Submodule Name": "Description of the submodule"
    }
  }
]
```

---

### ⚠️ Assumptions

* Documentation follows a logical HTML structure
* Headings represent feature hierarchy
* Descriptions are derived only from extracted content

---

### 🚧 Limitations

* Some websites may have deeply nested or inconsistent HTML
* Dynamic JavaScript-rendered content is not supported
* Module inference is structure-based, not semantic

---

### 🔮 Future Improvements

* Support for JavaScript-rendered docs
* Confidence scoring for extracted modules
* Caching repeated crawls
* Dockerized deployment
* REST API endpoint

---

### 👤 Author

**Chollangi Meghana Harini**
B.Tech - Raghu Institute of Technology
