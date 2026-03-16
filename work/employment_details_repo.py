from __future__ import annotations

"""
repositories/employment_details_repo.py
─────────────────────────────────────────
Raw DB queries for the applicant_employment_details table.
"""

from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import ApplicantEmploymentDetails


async def fetch_employment_details_by_party(
    session: AsyncSession,
    party_id: int,
) -> Optional[ApplicantEmploymentDetails]:
    """Return the employment-details row for a given party_id."""
    result = await session.execute(
        select(ApplicantEmploymentDetails)
        .where(ApplicantEmploymentDetails.party_id == party_id)
    )
    return result.scalars().first()
