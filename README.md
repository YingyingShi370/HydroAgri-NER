# HydroAgri-NER 🌾
A Hybrid NER Approach for AI-Driven Water and Agricultural Resource Management

> AgroNERX is a domain-adapted Named Entity Recognition (NER) framework that integrates ontology-guided attention mechanisms with deep learning. It is designed to extract critical entities from unstructured text in agriculture and water management, enabling more intelligent, scalable, and real-time decision-making for resource-constrained environments.

---

## 🔍 Highlights

- ✅ **Hybrid Model**: Combines pre-trained transformers with domain ontologies for robust semantic understanding.
- 🧠 **ARNF**: Multi-scale feature encoder capturing contextual semantics across tokens.
- 🎯 **ATOS**: Task balancing strategy optimized for heterogeneous and low-resource domains.
- 🚀 **Fast & Lightweight**: Achieves up to **29.8% latency reduction** and **33.4% memory savings**.
- 📊 **High Accuracy**: Achieved **95.54% F1** on AgriNLP and **96.75% F1** on FAO-AIMS datasets.

---

## 📌 Method Overview

<p align="center">
  <img src="https://your-domain.com/path/to/method_diagram.png" alt="AgroNERX Framework Overview" width="600"/>
</p>

AgroNERX consists of:

- **ARNF**: Adaptive Representation Neural Framework – semantic feature encoder across multiple linguistic and domain levels.
- **Ontology-guided Attention**: Leverages agricultural and water-resource ontologies to guide token interactions.
- **ATOS**: Adaptive Task Optimization Strategy – dynamically adjusts learning focus across subtasks.

---

## 📁 Datasets and Ontologies

We evaluate on two real-world, domain-specific NER datasets:

| Dataset   | Description                                | Format      |
|-----------|--------------------------------------------|-------------|
| **AgriNLP**   | Agronomic reports with annotated entities | JSON         |
| **FAO-AIMS**  | Policy texts in agriculture and irrigation | JSON/XML     |

Ontologies such as [AgroPortal](http://agroportal.lirmm.fr/) are integrated to support knowledge-enhanced tagging.

---

## 🚀 Quick Start

### 🔧 Setup

```bash
git clone https://github.com/your-username/AgroNERX.git
cd AgroNERX
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
