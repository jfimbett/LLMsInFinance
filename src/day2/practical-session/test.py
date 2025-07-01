#%%
from transformers import pipeline

clf = pipeline("text-classification")            # default model

#%%
print(clf("This restaurant is awesome"))

clf_roberta = pipeline(model="FacebookAI/roberta-large-mnli")  # task inferred
print(clf_roberta("This restaurant is awesome"))

batch_out = clf(["Great food", "Terrible service"])            # list → batch

