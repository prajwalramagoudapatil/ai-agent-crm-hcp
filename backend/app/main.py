from fastapi import FastAPI
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware


from app.core.config import settings
from app.db.database import Base, engine
from app.api.hcp_routes import router as hcp_router
from app.api.interaction_routes import router as interactions_router
from app.api.agent_routes import router as agent_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Backend for AI-powered HCP Interaction Logging"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(hcp_router)
app.include_router(interactions_router)
app.include_router(agent_router)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "debug": settings.DEBUG
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
    
@app.get("/db-test")
def db_test():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
        return {"db_test_result": "success"}
    except Exception as e:
        return {
            "database": "Test Failed",
            "error": str(e)
        }
        


