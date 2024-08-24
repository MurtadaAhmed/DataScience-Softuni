from transformers import AutoTokenizer, AutoModel
# Load the tokenizer and model
# tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/bert-base-bg-cs-pl-ru-cased")
tokenizer = AutoTokenizer.from_pretrained("DeepPavlov/xlm-roberta-large-en-ru")
# tokenizer = AutoTokenizer.from_pretrained("ai-forever/mGPT-1.3B-bulgarian")
# tokenizer = AutoTokenizer.from_pretrained("naver-clova-ix/donut-base")
model = AutoModel.from_pretrained("DeepPavlov/bert-base-bg-cs-pl-ru-cased")
# model = AutoModel.from_pretrained("DeepPavlov/xlm-roberta-large-en-ru")

# Example English text
text = "Евелена Бизова"

# Tokenize the text
tokens = tokenizer(text, return_tensors='pt')
token_ids = tokens['input_ids'].squeeze().tolist()
decoded_text = tokenizer.decode(token_ids, skip_special_tokens=True)
print(decoded_text)
exit()
# Pass tokens to the model
outputs = model(**tokens)

print(outputs)