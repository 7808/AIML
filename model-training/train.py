import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from dataset import CustomDataset
import json
import os

def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

def main():
    # Load configuration
    config = load_config('model/config.json')
    model_name = config.get('model_name', 'gpt2')
    output_dir = config.get('output_dir', 'model')

    # Load dataset
    dataset = CustomDataset('data/dataset.json')

    # Load pre-trained model and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
        logging_dir='logs',
        logging_steps=200,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
    )

    # Train the model
    trainer.train()

    # Save the model
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)

if __name__ == '__main__':
    main()
