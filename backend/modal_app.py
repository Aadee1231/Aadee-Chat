import modal

stub = modal.Stub("aadee-backend")

image = modal.Image.debian_slim().pip_install("fastapi", "uvicorn")

@stub.function(image=image, keep_warm=1)
@modal.asgi_app()
def app():
    from main import app as fastapi_app
    return fastapi_app
