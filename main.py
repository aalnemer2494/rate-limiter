from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
import time

app = FastAPI()

traffic_data = {}
MAX_REQUESTS = 5
TIME_WINDOW = 60

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    # Do not rate-limit the dashboard or stats endpoints
    if request.url.path in ["/dashboard", "/stats"]:
        return await call_next(request)

    client_ip = request.client.host
    current_time = time.time()
    
    if client_ip not in traffic_data:
        traffic_data[client_ip] = []
        
    traffic_data[client_ip] = [t for t in traffic_data[client_ip] if current_time - t < TIME_WINDOW]
    
    if len(traffic_data[client_ip]) >= MAX_REQUESTS:
        return JSONResponse(
            status_code=429, 
            content={"error": "Too Many Requests", "message": "Rate limit exceeded."}
        )
        
    traffic_data[client_ip].append(current_time)
    return await call_next(request)

@app.get("/")
def home():
    return {"status": "200 OK", "message": "Ping successful."}

@app.get("/dashboard", response_class=HTMLResponse)
def get_dashboard():
    with open("templates/index.html", "r") as f:
        return f.read()

@app.get("/stats")
def get_stats():
    return traffic_data
