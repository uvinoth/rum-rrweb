from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, ConfigDict

DataT = TypeVar("DataT")


# ─────────────────────────────────────────────
# Enums
# ─────────────────────────────────────────────

class KYCModule(str, Enum):
    BASIC          = "basic"
    ADDRESS        = "address"
    DISABILITY     = "disability"
    EMPLOYMENT     = "employment"
    PROFILE_CHECK  = "profile_check"
    ALL            = "all"


# ─────────────────────────────────────────────
# Generic API envelope
# ─────────────────────────────────────────────

class APIResponse(BaseModel, Generic[DataT]):
    success: bool = True
    message: Optional[str] = None
    data: DataT


# ─────────────────────────────────────────────
# CaseCustomer
# ─────────────────────────────────────────────

class CaseCustomerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    case_id: int
    customer_id: int
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    dob: Optional[date]
    email: Optional[str]
    mobile_number: str
    alternate_mobile_number: Optional[str]
    language: Optional[str]
    impairment_status: Optional[bool]
    impairment_type: Optional[str]
    impairment_percentage: Optional[Decimal]
    udid_number: Optional[str]
    pincode: Optional[str]
    customer_type: Optional[str]
    cibil_score: Optional[str]
    ucic_id: Optional[int]
    status: Optional[str]
    gender: Optional[str]
    is_default: Optional[bool]
    is_funding: Optional[bool]
    remarks: Optional[str]
    ckyc_id: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


# ─────────────────────────────────────────────
# Module schemas
# ─────────────────────────────────────────────

class BasicDetailsOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    party_id: int
    full_name: str
    name_verified: bool
    name_verified_via: Optional[str]
    gender: Optional[str]
    gender_verified: bool
    gender_verified_via: Optional[str]
    date_of_birth: Optional[date]
    dob_verified: bool
    dob_verified_via: Optional[str]
    age_years: Optional[int]
    father_spouse_name: Optional[str]
    father_spouse_name_verified: bool
    application_category: Optional[str]
    marital_status: Optional[str]
    profile_risk: Optional[str]
    preferred_language: Optional[str]
    mobile_number: Optional[str]
    mobile_verified: bool
    alternate_mobile_number: Optional[str]
    email_id: Optional[str]
    driving_license_number: Optional[str]
    driving_license_verified: bool
    driving_license_verified_via: Optional[str]
    driving_license_expiry: Optional[date]
    voter_id_number: Optional[str]
    voter_id_verified: bool
    voter_id_verified_via: Optional[str]
    passport_number: Optional[str]
    passport_verified: bool
    passport_verified_via: Optional[str]
    passport_expiry: Optional[date]
    face_liveliness_image_url: Optional[str]
    face_liveliness_verified: bool
    face_liveliness_verified_via: Optional[str]
    created_at: datetime
    updated_at: datetime


class AddressDetailsOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    party_id: int
    current_address_line: Optional[str]
    current_address_city: Optional[str]
    current_address_pin: Optional[str]
    current_address_state: Optional[str]
    current_address_landmark: Optional[str]
    current_address_ownership_status: Optional[str]
    current_address_verified: bool
    current_address_verified_via: Optional[str]
    years_at_current_address: Optional[int]
    permanent_address_line: Optional[str]
    permanent_address_city: Optional[str]
    permanent_address_pin: Optional[str]
    permanent_address_state: Optional[str]
    permanent_address_landmark: Optional[str]
    permanent_address_ownership_status: Optional[str]
    permanent_address_verified: bool
    permanent_address_verified_via: Optional[str]
    negative_area: bool
    negative_area_verified: bool
    mailing_address_line: Optional[str]
    mailing_address_city: Optional[str]
    mailing_address_pin: Optional[str]
    mailing_address_state: Optional[str]
    mailing_address_landmark: Optional[str]
    istance_from_branch_km: Optional[int]
    distance_from_branch_verified: bool
    created_at: datetime
    updated_at: datetime


class DisabilityDetailsOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    party_id: int
    impairment_status: bool
    type_of_impairment: Optional[str]
    percentage_of_impairment: Optional[Decimal]
    udid_number: Optional[str]
    created_at: datetime
    updated_at: datetime


class EmploymentDetailsOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    party_id: int
    employment_type: Optional[str]
    employment_industry: Optional[str]
    employer_type: Optional[str]
    employment_profession: Optional[str]
    nature_of_business: Optional[str]
    business_office_address: Optional[str]
    business_office_city: Optional[str]
    business_office_verified: bool
    negative_list: bool
    negative_list_verified: bool
    years_at_job_or_business: Optional[int]
    years_at_job_verified: bool
    gstin: Optional[str]
    udyam_number: Optional[str]
    udyam_verified: bool
    date_of_incorporation: Optional[date]
    date_of_incorporation_verified: bool
    created_at: datetime
    updated_at: datetime


class ProfileCheckOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    party_id: int
    is_director_or_senior_officer: bool
    director_senior_verified: bool
    is_existing_employee: bool
    existing_employee_verified: bool
    is_resigned_employee: bool
    fcu_market_information: bool
    fcu_market_verified: bool
    fcu_risk_customer: bool
    fcu_risk_verified: bool
    npa_status: bool
    pos_waiver_status: bool
    pos_waiver_verified: bool
    created_at: datetime
    updated_at: datetime


# ─────────────────────────────────────────────
# Composite response
# ─────────────────────────────────────────────

class ApplicantKYCOut(BaseModel):
    applicant:     CaseCustomerOut
    basic:         Optional[BasicDetailsOut]      = None
    address:       Optional[AddressDetailsOut]    = None
    disability:    Optional[DisabilityDetailsOut] = None
    employment:    Optional[EmploymentDetailsOut] = None
    profile_check: Optional[ProfileCheckOut]      = None


class KYCResponse(BaseModel):
    case_id:        int
    applicant_type: Optional[str]
    module:         str
    applicants:     list[ApplicantKYCOut]
