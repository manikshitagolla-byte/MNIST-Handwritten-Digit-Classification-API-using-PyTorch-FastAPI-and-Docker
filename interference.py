import torch
import torch.nn as nn

model = nn.Sequential(
    nn.Flatten(), nn.Linear(28 * 28, 128), nn.ReLU(), nn.Linear(128, 10)
)

model.load_state_dict(torch.load("mnist_model.pth"))

model.eval()

print("Model loaded successfully!")
