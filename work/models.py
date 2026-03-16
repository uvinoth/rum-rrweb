from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Boolean,
    Column,
    Date,
    ForeignKey,
    Identity,
    Integer,
    Numeric,
    SmallInteger,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel


class CaseCustomer(SQLModel, table=True):
    __tablename__ = "case_customers"

    id: int = Field(
        default=None,
        sa_column=Column(BigInteger, Identity(always=True), primary_key=True, autoincrement=True),
    )
    case_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("cases.id", ondelete="CASCADE"), nullable=False)
    )
    customer_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    )
    first_name: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    middle_name: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    last_name: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    dob: Optional[date] = Field(default=None, sa_column=Column(Date))
    email: Optional[str] = Field(default=None, sa_column=Column(CITEXT()))
    mobile_number: str = Field(sa_column=Column(String(15), nullable=False))
    alternate_mobile_number: Optional[str] = Field(default=None, sa_column=Column(String(15)))
    language: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    impairment_status: Optional[bool] = Field(default=None, sa_column=Column(Boolean))
    impairment_type: Optional[str] = Field(default=None, sa_column=Column(String))
    impairment_percentage: Optional[Decimal] = Field(default=None, sa_column=Column(Numeric(5, 2)))
    udid_number: Optional[str] = Field(default=None, sa_column=Column(String))
    pincode: Optional[str] = Field(default=None, sa_column=Column(String(10)))
    customer_type: Optional[str] = Field(default=None, sa_column=Column(String(25)))
    cibil_score: Optional[str] = Field(default=None, sa_column=Column(String(20)))
    ucic_id: Optional[int] = Field(default=None, sa_column=Column(Integer))
    status: Optional[str] = Field(default=None, sa_column=Column(String(40)))
    gender: Optional[str] = Field(default=None, sa_column=Column(String(25)))
    is_default: Optional[bool] = Field(default=False, sa_column=Column(Boolean))
    is_funding: Optional[bool] = Field(default=False, sa_column=Column(Boolean))
    remarks: Optional[str] = Field(default=None, sa_column=Column(String(255)))
    ckyc_id: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    created_at: Optional[datetime] = Field(
        sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(TIMESTAMP(timezone=True), onupdate=func.now())
    )
    deleted_at: Optional[datetime] = Field(
        sa_column=Column(TIMESTAMP(timezone=True))
    )


class ApplicantBasicDetails(SQLModel, table=True):
    __tablename__ = "applicant_basic_details"

    id: Optional[int] = Field(
        default=None,
        sa_column=Column(BigInteger, Identity(always=True), primary_key=True),
    )
    party_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("case_customers.id", ondelete="CASCADE"), nullable=False)
    )
    full_name: str = Field(sa_column=Column(String(150), nullable=False))
    name_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    name_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    gender: Optional[str] = Field(default=None, sa_column=Column(String(20)))
    gender_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    gender_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    date_of_birth: Optional[date] = Field(default=None, sa_column=Column(Date))
    dob_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    dob_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    age_years: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))
    father_spouse_name: Optional[str] = Field(default=None, sa_column=Column(String(150)))
    father_spouse_name_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    application_category: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    marital_status: Optional[str] = Field(default=None, sa_column=Column(String(20)))
    profile_risk: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    preferred_language: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    mobile_number: Optional[str] = Field(default=None, sa_column=Column(String(15)))
    mobile_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    alternate_mobile_number: Optional[str] = Field(default=None, sa_column=Column(String(15)))
    email_id: Optional[str] = Field(default=None, sa_column=Column(String(150)))
    driving_license_number: Optional[str] = Field(default=None, sa_column=Column(String(30)))
    driving_license_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    driving_license_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    driving_license_expiry: Optional[date] = Field(default=None, sa_column=Column(Date))
    voter_id_number: Optional[str] = Field(default=None, sa_column=Column(String(30)))
    voter_id_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    voter_id_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    passport_number: Optional[str] = Field(default=None, sa_column=Column(String(30)))
    passport_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    passport_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    passport_expiry: Optional[date] = Field(default=None, sa_column=Column(Date))
    face_liveliness_image_url: Optional[str] = Field(default=None, sa_column=Column(Text))
    face_liveliness_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    face_liveliness_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class ApplicantAddressDetails(SQLModel, table=True):
    __tablename__ = "applicant_address_details"

    id: Optional[int] = Field(
        default=None,
        sa_column=Column(BigInteger, Identity(always=True), primary_key=True),
    )
    party_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("case_customers.id", ondelete="CASCADE"), nullable=False)
    )
    current_address_line: Optional[str] = Field(default=None, sa_column=Column(Text))
    current_address_city: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    current_address_pin: Optional[str] = Field(default=None, sa_column=Column(String(10)))
    current_address_state: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    current_address_landmark: Optional[str] = Field(default=None, sa_column=Column(String(150)))
    current_address_ownership_status: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    current_address_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    current_address_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    years_at_current_address: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))
    permanent_address_line: Optional[str] = Field(default=None, sa_column=Column(Text))
    permanent_address_city: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    permanent_address_pin: Optional[str] = Field(default=None, sa_column=Column(String(10)))
    permanent_address_state: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    permanent_address_landmark: Optional[str] = Field(default=None, sa_column=Column(String(150)))
    permanent_address_ownership_status: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    permanent_address_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    permanent_address_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    negative_area: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    negative_area_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    mailing_address_line: Optional[str] = Field(default=None, sa_column=Column(Text))
    mailing_address_city: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    mailing_address_pin: Optional[str] = Field(default=None, sa_column=Column(String(10)))
    mailing_address_state: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    mailing_address_landmark: Optional[str] = Field(default=None, sa_column=Column(String(150)))
    istance_from_branch_km: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))
    distance_from_branch_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class ApplicantDisabilityDetails(SQLModel, table=True):
    __tablename__ = "applicant_disability_details"

    id: Optional[int] = Field(
        default=None,
        sa_column=Column(BigInteger, Identity(always=True), primary_key=True),
    )
    party_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("case_customers.id", ondelete="CASCADE"), nullable=False)
    )
    impairment_status: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    type_of_impairment: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    percentage_of_impairment: Optional[Decimal] = Field(default=None, sa_column=Column(Numeric(5, 2)))
    udid_number: Optional[str] = Field(default=None, sa_column=Column(String(30)))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class ApplicantEmploymentDetails(SQLModel, table=True):
    __tablename__ = "applicant_employment_details"

    id: Optional[int] = Field(
        default=None,
        sa_column=Column(BigInteger, Identity(always=True), primary_key=True),
    )
    party_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("case_customers.id", ondelete="CASCADE"), nullable=False)
    )
    employment_type: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    employment_industry: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    employer_type: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    employment_profession: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    nature_of_business: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    business_office_address: Optional[str] = Field(default=None, sa_column=Column(Text))
    business_office_city: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    business_office_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    negative_list: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    negative_list_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    years_at_job_or_business: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))
    years_at_job_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    gstin: Optional[str] = Field(default=None, sa_column=Column(String(20)))
    udyam_number: Optional[str] = Field(default=None, sa_column=Column(String(30)))
    udyam_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    date_of_incorporation: Optional[date] = Field(default=None, sa_column=Column(Date))
    date_of_incorporation_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))


class ApplicantProfileCheck(SQLModel, table=True):
    __tablename__ = "applicant_profile_check"

    id: Optional[int] = Field(
        default=None,
        sa_column=Column(BigInteger, Identity(always=True), primary_key=True),
    )
    party_id: int = Field(
        sa_column=Column(BigInteger, ForeignKey("case_customers.id", ondelete="CASCADE"), nullable=False)
    )
    is_director_or_senior_officer: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    director_senior_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    is_existing_employee: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    existing_employee_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    is_resigned_employee: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    fcu_market_information: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    fcu_market_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    fcu_risk_customer: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    fcu_risk_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    npa_status: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    pos_waiver_status: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    pos_waiver_verified: bool = Field(default=False, sa_column=Column(Boolean, nullable=False, server_default="false"))
    created_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False))
