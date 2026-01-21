# from app.prompts import build_prompt
from prompts import build_prompt
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#Generating the output for the CSR Summary
def generate_summary(payload):
    prompt = build_prompt(payload)

    #Adding the model using for this summary
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        max_tokens=300,#Cost effecient,
        temperature=0.2 # To control hallucination
    )

    return response.choices[0].message.content.strip()