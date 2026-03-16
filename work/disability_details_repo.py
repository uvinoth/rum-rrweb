from __future__ import annotations

"""
repositories/disability_details_repo.py
─────────────────────────────────────────
Raw DB queries for the applicant_disability_details table.
"""

from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import ApplicantDisabilityDetails


async def fetch_disability_details_by_party(
    session: AsyncSession,
    party_id: int,
) -> Optional[ApplicantDisabilityDetails]:
    """Return the disability-details row for a given party_id."""
    result = await session.execute(
        select(ApplicantDisabilityDetails)
        .where(ApplicantDisabilityDetails.party_id == party_id)
    )
    return result.scalars().first()
