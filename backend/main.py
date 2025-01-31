from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Создание приложения FastAPI
app = FastAPI()

# Настройка CORS (чтобы веб-клиент мог обращаться к API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешить все источники (для тестирования)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Определение модели запроса
class Message(BaseModel):
    text: str

# Маршрут для проверки работы API
@app.get("/")
def read_root():
    return {"message": "API работает! Отправьте POST-запрос на /chat"}

# Основной маршрут чата
@app.post("/chat")
def chat(message: Message):
    # Здесь можно добавить логику обработки сообщений (например, через GPT)
    response_text = f"Вы сказали: {message.text}"
    return {"response": response_text}

# Заглушка для favicon.ico (чтобы не было 404)
@app.get("/favicon.ico")
async def favicon():
    return {"detail": "No favicon"}
