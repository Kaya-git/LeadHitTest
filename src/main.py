from fastapi import FastAPI
from form_verif.routers import from_verif_router
import uvicorn

app = FastAPI(
    title="LeadHit"
)

@app.get("/")
async def root():
    ...

app.include_router(from_verif_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
