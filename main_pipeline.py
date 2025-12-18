import os
import re
from config import FALLBACK_RESPONSE
from llm_extractor import ask_llm

DATA_FILE = r"C:\Users\DELL\Desktop\Sarfraz Khan(Code_File)\PW Data Science\PW Project DS\School LLM Chatbot\text_data\school_info.txt"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def clean(text):
    return re.sub(r"[^a-zA-Z0-9 ]", "", text.lower())

def rule_based_answer(question, data):
    q_words = set(clean(question).split())

    best_match = ""
    best_score = 0

    for line in data:
        l_words = set(clean(line).split())
        score = len(q_words & l_words)

        if score > best_score:
            best_score = score
            best_match = line

    if best_score >= 2:
        return best_match

    return None

def run_pipeline(question):
    data = load_data()

    if not data:
        return FALLBACK_RESPONSE

    rule_answer = rule_based_answer(question, data)
    if rule_answer:
        return rule_answer

    return ask_llm("\n".join(data), question)
