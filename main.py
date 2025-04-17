from transformers import BertTokenizer, BertForSequenceClassification
import torch
import joblib

# Load the model and tokenizer
tokenizer = BertTokenizer.from_pretrained("intent_model")
model = BertForSequenceClassification.from_pretrained("intent_model")

# Load the label encoder
le = joblib.load("label_encoder.pkl")

def get_intent(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    predicted = torch.argmax(outputs.logits, dim=1).item()
    return le.inverse_transform([predicted])[0]

def chatbot_response(user_input):
    intent = get_intent(user_input)

    # Basic response logic
    responses = {
        "greet": "Hello! How can I help you today?????",
        "goodbye": "Goodbye! Have a great day!",
        "thank_you": "You're welcome!",
        "joke": "Why don't scientists trust atoms? Because they make up everything!"
    }

    return responses.get(intent, "Sorry, I didn't understand that.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    print("Bot:", chatbot_response(user_input))
