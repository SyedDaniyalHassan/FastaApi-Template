from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> str:
    """
    Sends echo back to user.

    :returns: message same as the incoming.
    """
    return "OK"
