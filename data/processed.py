
"""
processed_readme.py

This module documents the structure of preprocessed data files stored in `data/processed/`.

These files are cleaned and aligned for model training and evaluation.
Each entry typically includes:

    {
        "text": "Drip irrigation is effective for maize.",
        "labels": [0, 1, 0, 0, 2, 0]
    }

Label formats can follow BIO, BILOU, or other schemes depending on configuration.

Expected files:
- train.json
- val.json
- test.json

Ensure that data is tokenized using the same tokenizer as the model expects.

Generated automatically via preprocessing scripts (e.g., in `appom/data_loader.py`).
"""


