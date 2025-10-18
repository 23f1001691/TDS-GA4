import base64
import requests
import math

# --- SETTINGS ---
JINA_API_KEY = "your_jina_api_key"  
IMAGE_PATH = "download.webp"   
TEXT_INPUT = "خوارزمية تحسين السرب الجزيئي"  

# --- Helper to get embedding from Jina API ---
def get_embedding(input_data):
    url = "https://api.jina.ai/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {JINA_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=input_data, headers=headers)
    response.raise_for_status()
    return response.json()["data"][0]["embedding"]

# --- Step 1: Encode image in base64 ---
with open(IMAGE_PATH, "rb") as img_file:
    image_base64 = base64.b64encode(img_file.read()).decode("utf-8")

# --- Step 2: Get embeddings ---
image_embedding = get_embedding({
    "model": "jina-clip-v2",
    "input": [{"image": image_base64}]
})

text_embedding = get_embedding({
    "model": "jina-clip-v2",
    "input": [TEXT_INPUT]
})

# --- Step 3: Compute cosine similarity (dot product since normalized) ---
def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = math.sqrt(sum(a * a for a in vec1))
    mag2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (mag1 * mag2)

similarity = cosine_similarity(image_embedding, text_embedding)
print(f"Cosine similarity (dot product): {similarity:.4f}")
