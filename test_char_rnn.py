"""
Test script for the character-level language model training
This tests just the basics without the full training loop
"""
import torch
import torch.nn as nn
import numpy as np
import string
import random

# Set random seeds for reproducibility
torch.manual_seed(42)
np.random.seed(42)
random.seed(42)

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Create a small vocabulary and character mappings
all_characters = string.ascii_lowercase + ' '  # lowercase letters and space
n_characters = len(all_characters)
print(f"Characters in vocabulary: {all_characters}")
print(f"Vocabulary size: {n_characters}")

# Create dictionaries to convert between characters and indices
char_to_idx = {char: i for i, char in enumerate(all_characters)}
idx_to_char = {i: char for i, char in enumerate(all_characters)}

# Define the model
class CharRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers=1):
        super(CharRNN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers
        
        # GRU layer
        self.gru = nn.GRU(input_size, hidden_size, n_layers)
        
        # Output layer
        self.decoder = nn.Linear(hidden_size, output_size)
        
        # Softmax layer
        self.softmax = nn.LogSoftmax(dim=1)
    
    def forward(self, input_tensor, hidden_state):
        output, hidden = self.gru(input_tensor, hidden_state)
        output = self.decoder(output[-1])
        output = self.softmax(output)
        return output, hidden
    
    def init_hidden(self, batch_size=1):
        return torch.zeros(self.n_layers, batch_size, self.hidden_size, device=device)

# Test string to tensor conversion
def string_to_tensor(string):
    tensor = torch.zeros(len(string), 1, n_characters)
    for i, char in enumerate(string):
        index = char_to_idx.get(char, char_to_idx[' '])  # Default to space if char not found
        tensor[i][0][index] = 1
    return tensor

# Initialize a small model
n_hidden = 32
n_layers = 1
model = CharRNN(n_characters, n_hidden, n_characters, n_layers).to(device)

print(f"Model parameters: {sum(p.numel() for p in model.parameters())}")

# Test a forward pass
test_string = "hello"
input_tensor = string_to_tensor(test_string).to(device)
hidden = model.init_hidden()
output, hidden = model(input_tensor, hidden)

print(f"Input shape: {input_tensor.shape}")
print(f"Output shape: {output.shape}")
print(f"Hidden shape: {hidden.shape}")

# Get prediction
_, top_index = output.topk(1)
predicted_char = idx_to_char[top_index.item()]
print(f"Predicted next character after '{test_string}': '{predicted_char}'")

print("Basic model test completed successfully!")
