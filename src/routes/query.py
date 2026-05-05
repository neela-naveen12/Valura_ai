from fastapi import APIRouter
from src.core.safety import check_safety
from src.core.classifier import classify
from src.core.router import route
from src.core.memory import get_history, add_message
from sse_starlette.sse import EventSourceResponse
import asyncio

router = APIRouter()

@router.post("/query")
async def query_endpoint(request: dict):

    query = request.get("query")
    session_id = request.get("session_id", "default")
    portfolio = request.get("portfolio", [])

    async def event_stream():

        # Step 1: Safety
        safety = check_safety(query)
        if safety.get("blocked"):
            yield {"event": "error", "data": safety}
            return

        yield {"event": "start", "data": "Processing..."}

        history = get_history(session_id)

        # Step 2: Classification
        classification = classify(query, history)

        yield {"event": "chunk", "data": "Classified intent"}

        context = {
            "query": query,
            "portfolio": portfolio,
            "intent": classification["intent"],
            "entities": classification["entities"]
        }

        # Step 3: Routing
        response = route(classification["agent"], context)

        add_message(session_id, {"query": query, "response": response})

        await asyncio.sleep(0.2)

        yield {"event": "done", "data": response}

    return EventSourceResponse(event_stream())