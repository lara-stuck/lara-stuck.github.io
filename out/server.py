from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

# Define the allowed pages
pages = [
    "profile",
    "blog",
    "services",
    "projects",
    "contact",
    "assets"
]

# Initialize the FastAPI application
app = FastAPI()

# Mount the static files directory (e.g., for assets)
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
async def serve_path(request: Request):
    return FileResponse("index.html")


@app.get("/{path:path}")
async def serve_path(path: str, request: Request):
    """
    Handles GET requests and serves index.html for legal paths if the requested file does not exist.
    """
    # Check if the path matches any of the legal pages
    is_legal_path = any(path.startswith(page) for page in pages)

    # If the path is not an actual file or directory, redirect to index.html
    if is_legal_path and not os.path.exists(path):
        print(f"Path '{path}' does not exist. Redirecting to index.html")
        return FileResponse("index.html")
    
    # If the path exists or is not part of legal paths, return 404 or serve the file
    if os.path.exists(path):
        return FileResponse(path)
    else:
        return RedirectResponse("index.html")

# To run the server, use uvicorn:
# uvicorn filename:app --host 0.0.0.0 --port 8000
