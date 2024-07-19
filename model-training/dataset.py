import json
import torch
from torch.utils.data import Dataset
from transformers import GPT2Tokenizer

class CustomDataset(Dataset):
    def __init__(self, file_path):
        # Load dataset from JSON file
        with open(file_path, 'r') as file:
            self.data = json.load(file)
        # Initialize tokenizer
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        # Set maximum length for tokenization
        self.max_length = 512

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # Get item at index
        item = self.data[idx]
        text = item['text']
        # Tokenize the text
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=self.max_length)
        input_ids = inputs['input_ids'].squeeze()
        attention_mask = inputs['attention_mask'].squeeze()
        return {'input_ids': input_ids, 'attention_mask': attention_mask}
