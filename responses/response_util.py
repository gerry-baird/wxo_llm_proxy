from model.models import LLM_Request, LLM_Response, LLM_Cache_Entry
from responses.response_examples import llm_response_1


def build_data():
    data = []

    request_1 = LLM_Request(
        prompt="You are an insurance salesman and you have a client named John Collins. Write a marketing email to the client. The customer has a child that recently turned 25. In the USA, every young adult is required to purchase independent health by the age of 26. Recommend the silver plan as it is very cost effective. We will give a 15% discount as a loyalty bonus if the child takes out a policy with us.",
        model_id="meta-llama/llama-2-70b-chat",
        max_new_tokens=500,
        min_new_tokens=400,
        decoding_method="greedy"
    )

    response_1 = LLM_Response(
        message=llm_response_1
    )

    cache_1 = LLM_Cache_Entry(request=request_1, response=response_1)

    data.append(cache_1)
    return data
