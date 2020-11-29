import torch
from torchvision.models import resnet18

class Resnet(nn.Module):
    def __init__(self):
        super(Resnet, self).__init__()
        self.net = resnet18(pretrained=False, num_classes=1024)

    def forward(self, x):
        features = self.net(x)
        out = F.relu(features, inplace=True)
        return out

def resnet_18(cfg):
    model = Resnet()
    return model