
# appom/data_loader.py

import json
import torch
from torch.utils.data import Dataset

class NERDataset(Dataset):
    def __init__(self, data_path, tokenizer, max_length=256):
        with open(data_path, 'r', encoding='utf-8') as f:
            self.samples = json.load(f)
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        item = self.samples[idx]
        encoding = self.tokenizer(
            item['text'],
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        labels = torch.tensor(item['labels'], dtype=torch.long)
        return {**{k: v.squeeze(0) for k, v in encoding.items()}, "labels": labels}
