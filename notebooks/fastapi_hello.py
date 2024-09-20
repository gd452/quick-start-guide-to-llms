from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# In-memory storage for names
stored_names = []

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "hello world"

@app.get("/hello", response_class=PlainTextResponse)
async def hello():
    try:
        return "hello world!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.get("/hello/{name}", response_class=PlainTextResponse)
async def hello_name(name: str):
    return f"hello {name}!"

@app.get("/form", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "name": None, "stored_names": stored_names})

@app.post("/form", response_class=HTMLResponse)
async def post_form(request: Request, name: str = Form(...)):
    stored_names.append(name)
    return templates.TemplateResponse("form.html", {"request": request, "name": name, "stored_names": stored_names})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

