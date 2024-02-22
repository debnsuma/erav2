import torch
import torch.optim as optim
import torch.nn.functional as F

from torchvision import datasets, transforms

# Train data transformations
train_transforms = transforms.Compose([
                                        transforms.RandomApply([transforms.CenterCrop(22), ], p=0.1),
                                        transforms.Resize((28, 28)),
                                        transforms.RandomRotation((-15., 15.), fill=0),
                                        transforms.ToTensor(),
                                        transforms.Normalize((0.1307,), (0.3081,)),
                                    ])

# Test data transformations
test_transforms = transforms.Compose([
                                        transforms.ToTensor(),
                                        transforms.Normalize((0.1307,), (0.3081,))
                                    ])

use_cuda = torch.cuda.is_available()
device = torch.device("cuda" if use_cuda else "cpu")
criterion = F.nll_loss

def optimizer_fn(model, lr, momentum):
    return optim.SGD(model.parameters(), lr=lr, momentum=momentum)
    
def scheduler_fn(optimizer, step_size, gamma):
    return optim.lr_scheduler.StepLR(optimizer, step_size=step_size, gamma=gamma, verbose=True)
