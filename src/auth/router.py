from fastapi import APIRouter
from fastapi.responses import JSONResponse

auth_router = APIRouter()


@auth_router.post("/login")
def login(user: LoginPayload):

    # result, status_code = auth_service.login(email=user.email, password=user.password)
    return JSONResponse(content=result, status_code=status_code)


@auth_router.post("/refresh_access_token")
def refresh_access_token(refresh_token_payload: RefreshTokenPayload):

    # result, status_code = auth_service.refresh_access_token(
    #     refresh_token=refresh_token_payload.refresh_token
    # )
    return JSONResponse(content=result, status_code=status_code)
