from facemodel import model
from dataprocess import *
model.load_state_dict(torch.load('model_final'))

import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
	help="path to input image")

args = vars(ap.parse_args())
img=Image.open(args["input"])

img = img.resize((300,300))
x=transform(img)
x=torch.unsqueeze(x,0)
loader=torch.utils.data.DataLoader(dataset, batch_size=1, 
                                           sampler=indices)


def match(x,loader):
    
    output=model(x)
    _,prediction=torch.max(output,1)
    prediction
    
    for i,l in loader:
        
        if torch.equal(i,x):
            if prediction==l:
                return "Matched"
            else:
                return "Unmatched"
    else:
        return "unknown"

print(match(x,loader))



