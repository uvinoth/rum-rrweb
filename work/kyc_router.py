from __future__ import annotations

"""
routers/kyc_router.py
──────────────────────
FastAPI route definitions for the KYC module.

Each route handler:
  1. Declares its path, query params, and response_model.
  2. Calls the appropriate service function.
  3. Wraps the result in the APIResponse envelope and returns.

No business logic or DB queries here.
"""

from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db.session import get_db
from schemas.kyc_schemas import APIResponse, KYCModule, KYCResponse
from services.kyc_service import (
    get_address_kyc,
    get_basic_kyc,
    get_disability_kyc,
    get_employment_kyc,
    get_kyc_data,
    get_profile_check_kyc,
)

router = APIRouter(prefix="/kyc", tags=["KYC"])

# ── Reusable query param aliases ───────────────────────────────────────────

# applicantType is REQUIRED — no default, no Optional
ApplicantTypeQuery = Annotated[
    str,
    Query(
        alias="applicantType",
        description="Applicant role (required): primary | co_applicant | guarantor",
        examples=["primary", "co_applicant", "guarantor"],
    ),
]

ModuleQuery = Annotated[
    KYCModule,
    Query(
        description="KYC section to retrieve. Defaults to 'all'.",
        examples=["basic", "address", "disability", "employment", "profile_check", "all"],
    ),
]

DBSession = Annotated[AsyncSession, Depends(get_db)]


# ─────────────────────────────────────────────────────────────────────────────
# GET /kyc/{case_id}/
#   Combined endpoint: returns all modules or a specific one.
#   ?applicantType=primary|co_applicant|guarantor   (REQUIRED)
#   &module=basic|address|disability|employment|profile_check|all  (default: all)
# ─────────────────────────────────────────────────────────────────────────────

@router.get(
    "/{case_id}/",
    response_model=APIResponse[KYCResponse],
    summary="Get KYC data for a case",
    description=(
        "Returns KYC data for applicants in a case filtered by **applicantType** (required). "
        "Use **module** to fetch only one section."
    ),
    responses={
        200: {"description": "KYC data fetched successfully"},
        404: {"description": "No applicants found"},
        422: {"description": "applicantType query param missing"},
    },
)
async def get_kyc(
    case_id: int,
    session: DBSession,
    applicant_type: ApplicantTypeQuery,
    module: ModuleQuery = KYCModule.ALL,
) -> APIResponse[KYCResponse]:
    data = await get_kyc_data(session, case_id, applicant_type, module)
    return APIResponse(data=data, message="KYC data fetched successfully")


# ─────────────────────────────────────────────────────────────────────────────
# Module-specific GET endpoints
# ─────────────────────────────────────────────────────────────────────────────

@router.get(
    "/{case_id}/basic/",
    response_model=APIResponse[KYCResponse],
    summary="Get basic / identity details",
)
async def get_basic_details(
    case_id: int,
    session: DBSession,
    applicant_type: ApplicantTypeQuery,
) -> APIResponse[KYCResponse]:
    data = await get_basic_kyc(session, case_id, applicant_type)
    return APIResponse(data=data, message="Basic details fetched successfully")


@router.get(
    "/{case_id}/address/",
    response_model=APIResponse[KYCResponse],
    summary="Get address details",
)
async def get_address_details(
    case_id: int,
    session: DBSession,
    applicant_type: ApplicantTypeQuery,
) -> APIResponse[KYCResponse]:
    data = await get_address_kyc(session, case_id, applicant_type)
    return APIResponse(data=data, message="Address details fetched successfully")


@router.get(
    "/{case_id}/disability/",
    response_model=APIResponse[KYCResponse],
    summary="Get disability / impairment details",
)
async def get_disability_details(
    case_id: int,
    session: DBSession,
    applicant_type: ApplicantTypeQuery,
) -> APIResponse[KYCResponse]:
    data = await get_disability_kyc(session, case_id, applicant_type)
    return APIResponse(data=data, message="Disability details fetched successfully")


@router.get(
    "/{case_id}/employment/",
    response_model=APIResponse[KYCResponse],
    summary="Get employment / business details",
)
async def get_employment_details(
    case_id: int,
    session: DBSession,
    applicant_type: ApplicantTypeQuery,
) -> APIResponse[KYCResponse]:
    data = await get_employment_kyc(session, case_id, applicant_type)
    return APIResponse(data=data, message="Employment details fetched successfully")


@router.get(
    "/{case_id}/profile-check/",
    response_model=APIResponse[KYCResponse],
    summary="Get profile check details (FCU / NPA / employee flags)",
)
async def get_profile_check(
    case_id: int,
    session: DBSession,
    applicant_type: ApplicantTypeQuery,
) -> APIResponse[KYCResponse]:
    data = await get_profile_check_kyc(session, case_id, applicant_type)
    return APIResponse(data=data, message="Profile check details fetched successfully")
