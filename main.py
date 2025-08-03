from fastapi import FastAPI, HTTPException
from tasks import add

app = FastAPI(title="Async Task Queue Sample")


@app.get("/add")
def enqueue_add(x: int, y: int):
    try:
        res = add.delay(x, y)
        return {"task_id": res.id, "status": "queued"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))