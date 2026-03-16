from __future__ import annotations

"""
repositories/profile_check_repo.py
────────────────────────────────────
Raw DB queries for the applicant_profile_check table.
"""

from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import ApplicantProfileCheck


async def fetch_profile_check_by_party(
    session: AsyncSession,
    party_id: int,
) -> Optional[ApplicantProfileCheck]:
    """Return the profile-check row for a given party_id."""
    result = await session.execute(
        select(ApplicantProfileCheck)
        .where(ApplicantProfileCheck.party_id == party_id)
    )
    return result.scalars().first()
