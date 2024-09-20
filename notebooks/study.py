import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_embedding(text):
    try:
        response = openai.Embedding.create(
            input=text,
            engine='text-embedding-ada-002'
        )
        return response['data'][0]['embedding']
    except openai.error.RateLimitError as e:
        print(f"RateLimitError: {e}")
        check_quota()
        return None

embedded_text = get_embedding("I love to be vectorized")

if embedded_text is not None:
    is_correct_length = len(embedded_text) == 1536
    print(is_correct_length)
else:
    print("Embedding not retrieved due to rate limit error.")