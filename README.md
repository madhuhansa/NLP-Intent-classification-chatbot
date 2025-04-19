# 🤖 Chatbot Intent Classification

## 📚 About

This project is a chatbot built using **BERT** (Bidirectional Encoder Representations from Transformers) for intent classification. The chatbot uses a pretrained BERT model to classify user inputs into intents (such as greetings, goodbyes, jokes, etc.) and responds accordingly. The project leverages **Hugging Face's Transformers** and **PyTorch** for the model, and **scikit-learn** for encoding labels.

---

## 📂 File Structure

- `intents.json`: Dataset containing intents and example patterns  
- `main.py`: Loads model and label encoder, and runs the chatbot  
- `notebook/BERT Intent Classifier.ipynb`: Notebook for training the model  
- `notebook/intent_model/`: Folder that stores the trained BERT model  
- `notebook/label_encoder.pkl`: Serialized label encoder used for decoding predictions

---

## 🧑‍💻 Learnings

- Fine tune a BERT model for intent classification  
- Use Transformers and PyTorch for NLP tasks  
- Serialize models and encoders using `joblib`  
- Build a simple rule-based chatbot responding based on intent

---

## 🧰 Requirements

- Python 3.x  
- Jupyter Notebook  
- PyTorch  
- Hugging Face Transformers  
- scikit-learn

---

## 🛠️ Steps to Run

1. Clone the repository  
2. Install dependencies  
3. Run the notebook to train and save the model  
4. Run `main.py` to launch the chatbot  
5. Interact and test different inputs

---

## 💬 Chatbot Responses

- **Greet**: "Hello! How can I help you today?????"  
- **Goodbye**: "Goodbye! Have a great day!"  
- **Thank you**: "You're welcome!"  
- **Joke**: "Why don't scientists trust atoms? Because they make up everything!"  
- **Others**: "Sorry, I didn't understand that."
  
---
## 📜 Author

**Yahan Mahuhansa**
