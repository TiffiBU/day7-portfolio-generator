import openai, os
from dotenv import load_dotenv
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
PROJECTS = [
    {"day": 1, "title": "AI Text Summariser", "description": "Summarises text using GPT-4o-mini into 3 bullet points."},
    {"day": 2, "title": "AI Sentiment Analyser", "description": "Classifies customer feedback as positive, negative or neutral."},
    {"day": 3, "title": "AI Customer Support Bot", "description": "Context-aware chatbot with conversation memory."},
    {"day": 4, "title": "RAG Document Assistant", "description": "Ask questions about your own uploaded documents."},
    {"day": 5, "title": "AI Batch Processor", "description": "Processes hundreds of items automatically with GPT."},
    {"day": 6, "title": "AI Research Agent", "description": "Searches the web and writes structured research briefings."},
    {"day": 7, "title": "AI Portfolio Generator", "description": "Generates a complete HTML portfolio site with GPT."},
]
def generate_portfolio():
    print("Generating your AI portfolio site...")
    projects_text = "\n".join(["Day "+str(p["day"])+": "+p["title"]+" - "+p["description"] for p in PROJECTS])
    prompt = "Create a stunning dark-themed single-page portfolio website. Hero: TiffiBU, AI Engineer 7 Projects in 7 Days. Projects:\n"+projects_text+"\nSkills: Python, OpenAI API, RAG, Agents, Prompt Engineering. Footer GitHub: https://github.com/TiffiBU. Return ONLY complete HTML."
    response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role":"system","content":"You are an expert web developer. Generate beautiful modern HTML with inline CSS, dark theme, purple/blue gradients."},{"role":"user","content":prompt}], max_tokens=4000)
    html = response.choices[0].message.content
    for tag in ["```html","```"]:
        if html.startswith(tag): html = html[len(tag):]
    if html.endswith("```"): html = html[:-3]
    with open("portfolio.html","w") as f:
        f.write(html.strip())
    print("Done! Open portfolio.html in your browser.")
if __name__ == "__main__":
    generate_portfolio()
