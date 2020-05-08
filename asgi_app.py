from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({"hello": "world"})

routes = [
    Route("/", endpoint=homepage)
]

app = Starlette(debug=True, routes=routes)
