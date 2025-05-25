from typing import Annotated
from fastapi import APIRouter, Depends
from app.services.bank_service import OnlineBankService
from app.api.dependencies import get_online_bank_service

router = APIRouter()

@router.post("/bank/transfer")
def transfer_money_online(from_account_id: int, to_account_id: int, amount: int,
                         online_bank_service: Annotated[OnlineBankService, Depends(get_online_bank_service)]):
    """
    Transfer money online between two accounts
    """
    online_bank_service.make_transfer_online(from_account_id, to_account_id, amount)
    return {"message": "Transfer successful"}
