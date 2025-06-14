import modal

app = modal.App(name="aadeechat-backend")

image = modal.Image.debian_slim().pip_install("fastapi", "uvicorn")

@app.function(image=image, min_containers=1)  # Use min_containers instead of deprecated keep_warm
@modal.asgi_app()
def app_entry():
    from main import app
    return app

