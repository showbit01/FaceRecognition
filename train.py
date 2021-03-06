# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bhvox891RgsrtG308LeaMhhbaM8GLiGo
"""


#import torch

#import torchvision
from facemodel import *
from dataprocess import *

import time
import copy

import torch.optim as optim
from torch.optim import lr_scheduler  

criterion   = nn.CrossEntropyLoss()
optimizer   = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

def train_model(model, criterion, optimizer, num_epochs):
  losses = []
  runloss=0
  corrects=0
  best_acc=0
  total=0

  best_model_parameters = copy.deepcopy(model.state_dict())
  best_acc = 0.0
  initial_time= time.time()

  model=model.to(device)
  for epoch in range(num_epochs):

    #print('Epoch {}/{}'.format(epoch+1,num_epochs))
    #print('-' * 10)

    for input,label in train_loader:
      input=input.to(device)
      label=label.to(device)

      optimizer.zero_grad()
      
      output=model(input)
      _,prediction=torch.max(output,1)
      #print(output)

      loss=criterion(output,label)
      # print(loss)

      loss.backward()
      optimizer.step()
      #losses.append(loss.item())
      losses.append(loss.item())

      runloss+=loss.item() * input.size(0)
      corrects+= torch.sum(prediction == label)
      total+=input.size(0)
         

    epoch_loss=runloss/dataset_sizes['train']
    epoch_accurate=corrects.double()/total
    
    #print('Training loss : {:.4f} Training Accuracy: {:.2f}'.format(epoch_loss,epoch_accurate*100))

    if epoch_accurate>best_acc:

      best_acc=epoch_accurate
      best_model_parameters=copy.deepcopy(model.state_dict())

  final_time=time.time()

  train_time=final_time-initial_time

  print('Traning completed in {:.0f}m {:.0f}s'.format(train_time//60,train_time%60))

  model.load_state_dict(best_model_parameters)

  return model,losses

           
model,losses=train_model(model, criterion, optimizer, num_epochs=50)



torch.save(model.state_dict(),'./model_final')
model.load_state_dict(torch.load('model_final'))


'''
fig=plt.figure(figsize=(10,10))
plt.title("Train Loss")
plt.plot(losses,label="Train")
plt.xlabel('num_epochs', fontsize=12)
plt.ylabel('loss', fontsize=12)
plt.legend(loc='best')
'''
