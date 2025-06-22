import torch
import sys

print(f"Python version: {sys.version}")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU device: {torch.cuda.get_device_name(0)}")
else:
    print("Running on CPU only")

# Test creating a simple model
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(10, 1)
    
    def forward(self, x):
        return self.linear(x)

# Create model and move to available device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleModel().to(device)
print(f"Model created and moved to {device}")
print(f"Model parameters: {sum(p.numel() for p in model.parameters())}")

# Test NLTK availability
try:
    import nltk
    from nltk.corpus import words
    print("NLTK installed")
    
    try:
        nltk.data.find('corpora/words')
        print("NLTK words corpus already downloaded")
    except LookupError:
        print("NLTK words corpus needs to be downloaded")
except ImportError:
    print("NLTK not installed")
