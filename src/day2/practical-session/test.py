#%%
from transformers import pipeline

clf = pipeline("text-classification")            # default model

print(clf("This restaurant is awesome"))

