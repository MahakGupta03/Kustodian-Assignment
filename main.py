from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import firebase_admin
from firebase_admin import credentials, db

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
templates = Jinja2Templates(directory="templates")

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://kustodian-assessment-default-rtdb.firebaseio.com/'
})


@app.get("/", response_class=Jinja2Templates.TemplateResponse)
async def get_clients(request: Request):
    # try:
    #     ref = db.reference('clients')
    #     clients = ref.get()
    #     client_list = [client for client in clients.values()]
    #     return templates.TemplateResponse("index.html", {"request": request, "clients": client_list})
    # except Exception as e:
    #     return "Failed to fetch data from Firebase: " + str(e)
    try:
        ref = db.reference('clients')
        clients = ref.get()
        if not clients:
            raise HTTPException(status_code=404, detail="No clients found")
        client_list = [client for client in clients.values()]
        return templates.TemplateResponse("index.html", {"request": request, "clients": client_list})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data from Firebase: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)