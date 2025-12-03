from fastapi import FastAPI
from app.schemas.chat import ChatRequest, ChatResponse
from app.agent.agent import agent_instance

app = FastAPI()

SYSTEM_PROMPT = (
    "Você é um agente inteligente. "
    "Se a mensagem contiver um cálculo matemático, use a tool calculator. "
    "Caso contrário, responda normalmente."
)

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    prompt = f"{SYSTEM_PROMPT}\nUsuário: {req.message}"
    result = agent_instance(prompt)
    return ChatResponse(response=str(result))
