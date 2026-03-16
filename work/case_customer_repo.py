from __future__ import annotations

"""
repositories/case_customer_repo.py
─────────────────────────────────
All raw DB queries for the case_customers table.
Each function receives a session + filter params and returns ORM rows.
No business logic here.
"""

from typing import Optional, Sequence  # Optional kept for fetch_case_customer_by_id return type

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.models import CaseCustomer


async def fetch_case_customers(
    session: AsyncSession,
    case_id: int,
    applicant_type: str,
) -> Sequence[CaseCustomer]:
    """
    Return all non-deleted case_customers for a given case_id
    filtered by customer_type (primary / co_applicant / guarantor).
    """
    stmt = (
        select(CaseCustomer)
        .where(
            CaseCustomer.case_id == case_id,
            CaseCustomer.deleted_at.is_(None),
            CaseCustomer.customer_type == applicant_type,
        )
    )

    result = await session.execute(stmt)
    return result.scalars().all()


async def fetch_case_customer_by_id(
    session: AsyncSession,
    party_id: int,
) -> Optional[CaseCustomer]:
    """Return a single case_customer row by primary key (party_id)."""
    result = await session.execute(
        select(CaseCustomer).where(CaseCustomer.id == party_id)
    )
    return result.scalars().first()
