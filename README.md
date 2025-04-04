# 🌾 Hybrid NER for AI-Driven Water & Agricultural Resource Management

This repository implements a hybrid Named Entity Recognition (NER) framework combining **ontology-guided attention mechanisms** with **deep learning models**, specifically optimized for agricultural and water resource domains.

🚀 Designed for real-world applications such as:
- Precision irrigation planning  
- Early detection of crop diseases  
- Efficient allocation of water in data-scarce regions  

---

## 🧠 Key Features

- **ARNF (Adaptive Representation Neural Framework)** for multi-scale semantic feature learning  
- **ATOS (Adaptive Task Optimization Strategy)** for dynamic multi-task priority balancing  
- Ontology-integrated attention using domain-specific knowledge  
- Efficient inference with up to **33% memory reduction** and **~30% latency improvement**  
- Modular, testable codebase with real and synthetic benchmarks  

---

## 📁 Project Structure

```bash
Hybrid-NER-AgriWater/
│
├── appom/                   # Core library
│   ├── __init__.py
│   ├── data_loader.py       # Dataset class & tokenizer integration
│   ├── model.py             # ARNF model implementation
│   ├── controller.py        # Training/evaluation logic (uses ATOS)
│   └── utils.py             # Metric calculations, helpers
│
├── config/                  # Model and training configurations
│   ├── default_config.yaml
│   └── agrinlp_config.yaml
│
├── data/                    # Input datasets
│   ├── raw/                 # Unprocessed source data
│   │   └── raw_readme.py
│   └── processed/           # Cleaned and label-aligned NER data
│       └── processed_readme.py
│
├── benchmarks/              # Profiling, ablation, latency & memory tests
│   ├── latency_tests.py
│   ├── memory_tests.py
│   └── ablation_study.ipynb
│
├── experiments/             # Shell scripts, result logs
│   ├── run_experiments.sh
│   ├── logs/
│   └── results/
│
├── ontology/                # Domain-specific ontology files
│   └── agri_ontology.owl
│
├── tests/                   # Unit tests for model & controller
│   ├── test_model.py
│   └── test_controller.py
│
├── requirements.txt         # Python dependencies
├── setup.py                 # Package metadata (to be added)
└── README.md                # You are here!
