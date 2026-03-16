from __future__ import annotations

"""
repositories/basic_details_repo.py
────────────────────────────────────
Raw DB queries for the applicant_basic_details table.
"""

from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import ApplicantBasicDetails


async def fetch_basic_details_by_party(
    session: AsyncSession,
    party_id: int,
) -> Optional[ApplicantBasicDetails]:
    """Return the basic-details row for a given party_id."""
    result = await session.execute(
        select(ApplicantBasicDetails)
        .where(ApplicantBasicDetails.party_id == party_id)
    )
    return result.scalars().first()
