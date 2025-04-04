
# tests/test_controller.py

import torch
from torch.utils.data import DataLoader, TensorDataset
from appom.controller import train, evaluate
from appom.model import ARNFModel

def get_dummy_dataloader():
    input_ids = torch.randint(0, 1000, (4, 12))
    attention_mask = torch.ones_like(input_ids)
    labels = torch.randint(0, 3, (4, 12))

    dataset = TensorDataset(input_ids, attention_mask, labels)
    return DataLoader(dataset, batch_size=2)

def test_train_loop_runs():
    model = ARNFModel(base_model="bert-base-uncased", num_labels=3)
    dataloader = get_dummy_dataloader()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)

    loss = train(model, dataloader, optimizer, device="cpu")
    assert isinstance(loss, float)
    assert loss > 0

def test_evaluate_loop_runs():
    model = ARNFModel(base_model="bert-base-uncased", num_labels=3)
    dataloader = get_dummy_dataloader()

    preds, labels = evaluate(model, dataloader, device="cpu")
    assert len(preds) == len(labels)
    assert all(isinstance(p, list) for p in preds)
