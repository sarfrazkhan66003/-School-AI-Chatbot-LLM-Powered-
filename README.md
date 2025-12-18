# 🏫 School AI Chatbot (LLM Powered)

An intelligent **LLM-based School Information Chatbot** built using **Python, Streamlit, and Groq (OpenAI-compatible API)**.
This project demonstrates how to build a **real-time, context-grounded AI chatbot** that answers queries strictly from provided data without hallucination.

Developed by **Sarfraz Khan** 👨‍💻

---

## 🚀 Project Overview

This chatbot answers user questions related to a school using a **text-based knowledge source (`school.txt`)**.
It connects to a **Large Language Model (LLM)** in real-time and generates accurate responses based only on the given school information.

If the requested information is not available, the chatbot politely responds with a fallback message and contact details.

---

## 🎯 Key Features

* 🤖 Real-time LLM responses using Groq API
* 📄 Context-based answering from school.txt
* ❌ No hallucination (strict grounding)
* 📊 Confidence indicator (High / Low)
* 🧾 Source attribution (school.txt)
* 💬 Session-based chat history
* 📈 Query logging for analytics
* 🎨 Clean & user-friendly Streamlit UI

---

## 🧠 What This Project Demonstrates

* How LLMs can be safely used with **domain-specific data**
* How to avoid hallucinations using **prompt engineering**
* How to design a **production-style AI pipeline**
* How to build **resume-ready GenAI projects**

---

## 🗂️ Project Structure

```
School-LLM-Chatbot/
│
├── app.py                 # Streamlit UI (Frontend)
├── main_pipeline.py       # Core logic pipeline
├── llm_extractor.py       # LLM API interaction
├── config.py              # API & environment configuration
├── .env                   # API key (ignored by git)
├── query_log.txt          # Query analytics log
│
├── text_data/
│   └── school.txt         # School information source
│
├── requirements.txt
└── README.md
```

---

## 📥 Input

User can ask questions such as:

* What is the name of the school?
* What are the school timings?
* What is the admission process?
* What are the fees for primary classes?
* Does the school provide transport facility?

---

## 📤 Output

The chatbot responds with:

* ✅ Accurate answer from school.txt
* 📊 Confidence score
* 📄 Source information

### Example Output:

```
The school timing is from 8:00 AM to 2:00 PM.

Confidence: High
Source: school.txt
```

If information is missing:

```
Is sawal ki jankari hamare paas uplabdh nahi hai.
Zyada jankari ke liye school se sampark kare.

Contact: +91-9876543210
Email: info@greenvalleyschool.edu

Confidence: Low
Source: school.txt
```

---

## ⚙️ How the System Works (Step-by-Step)

1️⃣ User enters a question in the UI
2️⃣ `main_pipeline.py` loads school.txt
3️⃣ Context + question is sent to LLM
4️⃣ LLM generates grounded response
5️⃣ Confidence & source are appended
6️⃣ Query is logged for analytics
7️⃣ Final answer is shown to the user

---

## 🔑 Environment Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create `.env` File

```env
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ `.env` is ignored using `.gitignore`

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📦 Technologies Used

* Python 🐍
* Streamlit 🎨
* Groq API (OpenAI-compatible) ⚡
* Prompt Engineering 🧠
* Environment Variables (.env) 🔐

---

## 📈 Learning Outcomes

Through this project, I learned:

* How to integrate LLM APIs in real-time applications
* How to design hallucination-safe AI systems
* How to structure AI pipelines for production
* How to build user-friendly AI interfaces
* How to log and analyze user queries
* How to write clean, modular, and scalable code

---

## 🧑‍💻 Author

**Sarfraz Khan**
Aspiring Data Scientist | AI & LLM Enthusiast

---

## ⭐ Future Enhancements

* 🔍 Vector search using FAISS
* 🎤 Voice-based chatbot
* 🌐 Multi-school support
* ☁️ Cloud deployment
* 📊 Admin analytics dashboard

---

⭐ If you like this project, feel free to **star the repository**!
