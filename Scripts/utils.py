
# appom/utils.py

import numpy as np
from sklearn.metrics import f1_score, classification_report

def compute_metrics(preds, labels):
    preds_flat = np.concatenate(preds)
    labels_flat = np.concatenate(labels)

    mask = labels_flat != -100  # assuming -100 is used for ignored tokens
    preds_clean = preds_flat[mask]
    labels_clean = labels_flat[mask]

    f1 = f1_score(labels_clean, preds_clean, average="weighted")
    report = classification_report(labels_clean, preds_clean)

    return {"f1": f1, "report": report}
