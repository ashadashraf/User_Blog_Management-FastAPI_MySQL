from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication, chat

# OPENAI_API_KEY="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"

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)

app.include_router(user.router)

app.include_router(chat.router)

app.include_router(blog.router)
