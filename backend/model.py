import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_test_cases(code):
    inputs = tokenizer.encode(code, return_tensors='pt')
    outputs = model.generate(inputs, max_length=500, num_return_sequences=1)
    test_cases = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return test_cases
