
# tests/test_model.py

import torch
from appom.model import ARNFModel

def test_arnf_model_forward_pass():
    model = ARNFModel(base_model="bert-base-uncased", num_labels=5)
    model.eval()

    input_ids = torch.randint(0, 1000, (2, 10))          # batch_size=2, seq_len=10
    attention_mask = torch.ones_like(input_ids)
    labels = torch.randint(0, 5, (2, 10))                # 5 label classes

    with torch.no_grad():
        output = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)

    assert "logits" in output
    assert output["logits"].shape == (2, 10, 5)
    assert output["loss"] is not None
