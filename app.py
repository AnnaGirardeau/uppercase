from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.api_route("/", methods=["GET", "POST"])
async def transform_text(request: Request, text: str = None):
    """
    Transforms the provided text input to uppercase.
    Supports both GET (using query parameter) and POST (using a JSON payload).
    
    GET example:
      /?text=hello
    POST example (JSON body):
      { "text": "hello" }
    """
    # Determine the request method
    if request.method == "POST":
        # Try to parse JSON body for POST requests.
        try:
            payload = await request.json()
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid JSON input")
        # Override text from JSON payload if present
        text = payload.get("text", text)

    # Validate that text input was provided.
    if not text:
        raise HTTPException(status_code=400, detail="No text provided. Please provide text via query parameter (GET) or JSON payload (POST).")
    
    # Transform the text to uppercase.
    upper_text = text.upper()
    return JSONResponse(content={"result": upper_text})
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
