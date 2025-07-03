# human_review.py

import random
import hashlib

def get_human_consensus(prompt, response):
    key = hashlib.sha256((prompt + response).encode()).hexdigest()
    random.seed(int(key[:8], 16))
    return round(random.uniform(0.0, 1.0), 2)

def estimate_validation_time(response):
    word_count = len(response.split())
    base_time = 0.5 + (word_count / 50.0)
    return round(base_time, 1)
