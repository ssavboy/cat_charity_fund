from datetime import datetime
from typing import List

from app.models.base import CharityDonationBase


def investing(
    target: CharityDonationBase,
    sources: List[CharityDonationBase],
) -> List[CharityDonationBase]:
    results = []
    for source in sources:
        fund_selection = min(
            target.full_amount - (target.invested_amount or 0),
            source.full_amount - (source.invested_amount or 0),
        )
        for entity in source, target:
            entity.invested_amount = (
                entity.invested_amount or 0
            ) + fund_selection
            if entity.full_amount == entity.invested_amount:
                entity.fully_invested = True
                entity.close_date = datetime.now()
        results.append(source)
        if target.fully_invested:
            break
    return results
