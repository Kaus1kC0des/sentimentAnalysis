import transformers
import torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification,pipeline

model_path = "cardiffnlp/twitter-roberta-base-sentiment"
sentiment = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

print(sentiment("This  is fucking awesome!"))