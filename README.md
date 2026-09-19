# Full-Stack API Rate Limiter

A containerized Python microservice that implements custom IP-based rate limiting and features a real-time traffic monitoring dashboard. Built to demonstrate middleware development, API security, and environment virtualization.

## Features
- **Custom Security Middleware**: Intercepts inbound HTTP traffic to enforce a strict limit of 5 requests per 60-second window per IP address.
- **Live Traffic Dashboard**: A lightweight HTML/JS frontend that polls the backend API to display active connections and dynamically flag blocked targets.
- **Containerized Environment**: Fully packaged with Docker for isolated, environment-agnostic deployment.

## Tech Stack
- **Backend**: Python 3.10, FastAPI, Uvicorn
- **Frontend**: HTML, Vanilla CSS & JavaScript
- **Infrastructure**: Docker, Git

## Quick Start

### Run via Docker
Ensure Docker Desktop is running, then build and launch the container:
```bash
docker build -t rate-limiter-app .
docker run -p 8000:8000 rate-limiter-app
