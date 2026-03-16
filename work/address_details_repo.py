from __future__ import annotations

"""
repositories/address_details_repo.py
──────────────────────────────────────
Raw DB queries for the applicant_address_details table.
"""

from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import ApplicantAddressDetails


async def fetch_address_details_by_party(
    session: AsyncSession,
    party_id: int,
) -> Optional[ApplicantAddressDetails]:
    """Return the address-details row for a given party_id."""
    result = await session.execute(
        select(ApplicantAddressDetails)
        .where(ApplicantAddressDetails.party_id == party_id)
    )
    return result.scalars().first()
