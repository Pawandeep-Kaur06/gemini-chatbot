import google.generativeai as genai
import gradio as gr

API_KEY = "YOUR_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def chatbot(message, history):
    try:
        response = model.generate_content(message)
        return response.text
    except Exception as e:
        return f"Error: {e}"

demo = gr.ChatInterface(
    fn=chatbot,
    title="Gemini AI Chatbot",
    description="Simple chatbot using Gemini API"
)

demo.launch()