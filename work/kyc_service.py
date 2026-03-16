from __future__ import annotations

"""
services/kyc_service.py
────────────────────────
Business logic layer.

Every function:
  1. Calls one or more repository functions to fetch raw ORM rows.
  2. Validates / assembles them into the response schema.
  3. Raises domain exceptions on failure.

No SQLAlchemy query syntax here — that lives in repositories/.
"""

from typing import Optional  # still needed for ORM row return types

from sqlalchemy.ext.asyncio import AsyncSession

from core.exceptions import KYCNotFoundException
from repositories.address_details_repo import fetch_address_details_by_party
from repositories.basic_details_repo import fetch_basic_details_by_party
from repositories.case_customer_repo import fetch_case_customers
from repositories.disability_details_repo import fetch_disability_details_by_party
from repositories.employment_details_repo import fetch_employment_details_by_party
from repositories.profile_check_repo import fetch_profile_check_by_party
from schemas.kyc_schemas import (
    AddressDetailsOut,
    ApplicantKYCOut,
    BasicDetailsOut,
    CaseCustomerOut,
    DisabilityDetailsOut,
    EmploymentDetailsOut,
    KYCModule,
    KYCResponse,
    ProfileCheckOut,
)


# ─────────────────────────────────────────────
# Internal helper
# ─────────────────────────────────────────────

def _should_load(module: KYCModule, target: KYCModule) -> bool:
    """Return True when the requested module matches target or ALL is requested."""
    return module in (target, KYCModule.ALL)


# ─────────────────────────────────────────────
# Core service function
# ─────────────────────────────────────────────

async def get_kyc_data(
    session: AsyncSession,
    case_id: int,
    applicant_type: str,
    module: KYCModule,
) -> KYCResponse:
    """
    Fetch KYC data for all applicants in a case.

    Steps:
      1. Fetch all case_customer rows (optionally filtered by applicant_type).
      2. For each applicant, fetch only the requested module(s).
      3. Assemble and return KYCResponse.
    """
    customers = await fetch_case_customers(session, case_id, applicant_type)

    if not customers:
        raise KYCNotFoundException(
            f"No applicants found for case_id={case_id} with applicant_type='{applicant_type}'"
        )

    applicants: list[ApplicantKYCOut] = []

    for customer in customers:
        party_id: int = customer.id  # type: ignore[assignment]

        basic = (
            BasicDetailsOut.model_validate(
                await fetch_basic_details_by_party(session, party_id)
            )
            if _should_load(module, KYCModule.BASIC)
            and await fetch_basic_details_by_party(session, party_id)
            else None
        )

        address = (
            AddressDetailsOut.model_validate(
                await fetch_address_details_by_party(session, party_id)
            )
            if _should_load(module, KYCModule.ADDRESS)
            and await fetch_address_details_by_party(session, party_id)
            else None
        )

        disability = (
            DisabilityDetailsOut.model_validate(
                await fetch_disability_details_by_party(session, party_id)
            )
            if _should_load(module, KYCModule.DISABILITY)
            and await fetch_disability_details_by_party(session, party_id)
            else None
        )

        employment = (
            EmploymentDetailsOut.model_validate(
                await fetch_employment_details_by_party(session, party_id)
            )
            if _should_load(module, KYCModule.EMPLOYMENT)
            and await fetch_employment_details_by_party(session, party_id)
            else None
        )

        profile_check = (
            ProfileCheckOut.model_validate(
                await fetch_profile_check_by_party(session, party_id)
            )
            if _should_load(module, KYCModule.PROFILE_CHECK)
            and await fetch_profile_check_by_party(session, party_id)
            else None
        )

        applicants.append(
            ApplicantKYCOut(
                applicant=CaseCustomerOut.model_validate(customer),
                basic=basic,
                address=address,
                disability=disability,
                employment=employment,
                profile_check=profile_check,
            )
        )

    return KYCResponse(
        case_id=case_id,
        applicant_type=applicant_type,
        module=module.value,
        applicants=applicants,
    )


# ─────────────────────────────────────────────
# Module-specific service functions
# ─────────────────────────────────────────────

async def get_basic_kyc(
    session: AsyncSession,
    case_id: int,
    applicant_type: str,
) -> KYCResponse:
    return await get_kyc_data(session, case_id, applicant_type, KYCModule.BASIC)


async def get_address_kyc(
    session: AsyncSession,
    case_id: int,
    applicant_type: str,
) -> KYCResponse:
    return await get_kyc_data(session, case_id, applicant_type, KYCModule.ADDRESS)


async def get_disability_kyc(
    session: AsyncSession,
    case_id: int,
    applicant_type: str,
) -> KYCResponse:
    return await get_kyc_data(session, case_id, applicant_type, KYCModule.DISABILITY)


async def get_employment_kyc(
    session: AsyncSession,
    case_id: int,
    applicant_type: str,
) -> KYCResponse:
    return await get_kyc_data(session, case_id, applicant_type, KYCModule.EMPLOYMENT)


async def get_profile_check_kyc(
    session: AsyncSession,
    case_id: int,
    applicant_type: str,
) -> KYCResponse:
    return await get_kyc_data(session, case_id, applicant_type, KYCModule.PROFILE_CHECK)
