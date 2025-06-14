import modal

app = modal.App(name="aadeechat-backend")

image = modal.Image.debian_slim().pip_install("fastapi", "uvicorn")

@app.function(image=image, keep_warm=1)
@modal.asgi_app()
def fastapi_app():
    from main import app as fastapi_app
    return fastapi_app

