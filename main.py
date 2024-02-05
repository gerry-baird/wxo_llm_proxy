from fastapi import FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.routing import APIRoute
from model.models import LLM_Request, LLM_Response
from responses.response_util import build_data
from deep_compare import CompareVariables

app = FastAPI()
security = HTTPBasic()


# this is our datastore
preset_responses = build_data()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/v1/generate")
async def generate(llm_request: LLM_Request) -> LLM_Response:

    for llm_cache_entry in preset_responses:
        cached_request = llm_cache_entry.request
        if CompareVariables.deep_compare(cached_request, llm_request):
            return llm_cache_entry.response

    default_response = preset_responses[0].response
    return default_response


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name  # in this case, operation ID will be 'greeting'


use_route_names_as_operation_ids(app)