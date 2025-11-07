import torch
from torch import nn, Tensor


x = nn.Parameter(torch.randn([2, 2], dtype=torch.float32))
print(x)
b = nn.Parameter(torch.randn([2, ], dtype=torch.float))
print(b)

class MyLayer(nn.Module):
    def __init__(self, input: int, output: int) -> None:
        super().__init__()
        self.weight = nn.Parameter(torch.randn(\
            input, output, dtype=torch.float32))
        self.bias = nn.Parameter(torch.randn(\
            output, dtype=torch.float32))
        
    def forward(self, x: Tensor) -> Tensor:
        return x @ self.weight + self.bias
    
layer_1 = MyLayer(2, 1)
for str, param in layer_1.named_parameters():
    print(f"name: {str}, parameter: {param}")