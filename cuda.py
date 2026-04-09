import os
import torch

print(f"CUDA available: {torch.cuda.is_available()}")

print(torch.__version__)
print(torch.version.cuda)
print(torch.randn(1).cuda())