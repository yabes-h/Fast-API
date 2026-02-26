from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
```
- Klik **"Commit changes"**

---

**File 2: `requirements.txt`**
- Klik **"Add file" → "Create new file"**
- Nama file: `requirements.txt`
- Isi dengan:
```
fastapi
uvicorn[standard]
