import modal
import sys

app = modal.App(name="aadeechat-backend")

# Add current directory to Python path so Modal can find main.py
sys.path.append(".")

# Build image with FastAPI and Uvicorn
image = modal.Image.debian_slim().pip_install("fastapi", "uvicorn")

@app.function(image=image, keep_warm=1)
@modal.asgi_app()
def fastapi_app():
    from main import app as fastapi_app
    return fastapi_app
