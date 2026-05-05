from sse_starlette.sse import EventSourceResponse

async def sse_response(generator):
    return EventSourceResponse(generator)