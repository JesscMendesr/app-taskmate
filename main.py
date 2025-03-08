from fastapi import FastAPI
from controllers.usuario_controller import router as usuario_router
from controllers.tarefa_controller import router as tarefa_router
from controllers.cliente_controller import router as cliente_router

app = FastAPI()

# Registra os routers
app.include_router(usuario_router, prefix="/api")
app.include_router(tarefa_router, prefix="/api")
app.include_router(cliente_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Bem-vindo ao sistema de gestão de tarefas e clientes!"}