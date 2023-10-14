from fastapi import APIRouter, HTTPException

from .schemas import ResponseModel, PromptRequest
from .gpt_handler import generate_gpt_response

router = APIRouter(prefix='/gpt', tags=['GPT'])


@router.post("/ask", response_model=ResponseModel)
async def ask_gpt(prompt_request: PromptRequest):
    try:
        response = generate_gpt_response(prompt_request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
