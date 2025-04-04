# 🌾 HydroAgri-NER: Hybrid NER for AI-Driven Water & Agricultural Resource Management

AgroNERX is a hybrid Named Entity Recognition (NER) system that integrates **ontology-guided attention mechanisms** with **deep neural models** to extract structured information from domain-specific, unstructured agricultural and water resource texts. The system is optimized for challenging conditions such as **data scarcity**, **semantic ambiguity**, and **heterogeneous real-world inputs**.

This repository contains the full implementation of the proposed method, including model code, configurations, datasets (samples), benchmarks, and unit tests.

---

## 📌 Motivation

Named Entity Recognition (NER) is a foundational task in NLP that enables structured understanding of text. In agriculture and water resource domains, however, NER systems must contend with:

- Complex and evolving domain terminologies (e.g., crop names, irrigation methods)
- Time-sensitive text (e.g., weather reports, sensor data)
- Sparse labeled data in specialized subfields
- The need for lightweight deployment in low-resource regions

AgroNERX addresses these challenges by combining **pre-trained language models** with **domain-specific knowledge bases** and a dynamic optimization strategy.

---

## 🧠 Key Components

### 🔹 Adaptive Representation Neural Framework (ARNF)
- Learns hierarchical semantic representations across token, phrase, and entity levels.
- Uses context-aware embeddings from pre-trained models (e.g., BERT).

### 🔹 Ontology-Guided Attention
- Integrates external agricultural ontologies (e.g., FAO, Agrovoc) to guide entity linking.
- Boosts performance on unseen or rare domain terms.

### 🔹 Adaptive Task Optimization Strategy (ATOS)
- Dynamically balances loss terms from multiple objectives.
- Increases robustness in multitask setups and heterogeneous input formats.

---

## 📊 Performance Summary

| Dataset     | F1 Score ↑ | Inference Latency ↓ | Memory Usage ↓ |
|-------------|------------|----------------------|----------------|
| AgriNLP     | 95.54%     | -29.8%               | -33.4%         |
| FAO-AIMS    | 96.75%     | -27.2%               | -31.1%         |

The model outperforms several state-of-the-art baselines and scales effectively for real-time decision support systems.

---

## 🔮 Future Development

We plan to further improve and extend AgroNERX in the following directions:

- **Real-time NER on streaming data** (e.g., IoT-based sensor reports, live climate feeds)
- **Multi-lingual support**, including datasets in Spanish, French, and regional languages commonly used in agricultural reporting
- **Low-resource transfer learning**, with meta-learning techniques for domains with extremely sparse labeled data
- **Integration with geospatial data**, for enhanced entity grounding in location-aware scenarios
- **Deployment toolkit** for on-edge inference in mobile or remote devices
- **Graph-based reasoning** using domain ontologies to enhance post-NER inference tasks

---


## 📝 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software for research or commercial purposes, provided that proper attribution is given.

See the full license in [LICENSE](./LICENSE).


---


## 🙏 Acknowledgments

This project would not have been possible without the following:

- **FAO-AIMS** and **AgroPortal** for providing access to open ontologies and domain data.
- The **HuggingFace Transformers** and **Datasets** teams for their powerful open-source libraries.
- Colleagues at **Legend Co., Ltd.** for their support, infrastructure, and early feedback on model deployments.
- The broader NLP and data-for-good community for inspiring the use of AI in sustainable development goals (SDGs).

Special thanks to the researchers and domain experts contributing to open agriculture and water-related NLP benchmarks.
