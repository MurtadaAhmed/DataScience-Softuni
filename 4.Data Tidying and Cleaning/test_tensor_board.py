# in the terminal run: tensorboard --logdir=runs after running this code
# then open the browser and go to: http://localhost:6006/
# if running on docker , we need to run the docker contain with the port 6006 open
# docker run -it -p 6006:6006 <your-docker-image>
# then in the docker container
# run: tensorboard --logdir=demo_result_tensorboard --host 0.0.0.0 --port 6006
# or
# run: tensorboard --logdir /runs --host 0.0.0.0 --port 6006




import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter

# Dummy data and model
input_size = 10
output_size = 1
batch_size = 16
epochs = 10000000

# Create a simple linear model
model = nn.Linear(input_size, output_size)

# Loss and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dummy input and target data
inputs = torch.randn(batch_size, input_size)
targets = torch.randn(batch_size, output_size)

# TensorBoard writer
writer = SummaryWriter('runs/dummy_experiment')

# Training loop
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()

    # Forward pass
    outputs = model(inputs)
    loss = criterion(outputs, targets)

    # Backward pass and optimize
    loss.backward()
    optimizer.step()

    # Log the loss
    writer.add_scalar('training_loss', loss.item(), epoch)

    print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# Close the writer
writer.close()

print("Training complete. Check TensorBoard for logs.")
