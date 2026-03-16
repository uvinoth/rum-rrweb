from __future__ import annotations

from datetime import datetime, date
from typing import Optional

from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Column,
    ForeignKey,
    Text,
    Integer,
    String,
    Identity,
    Boolean,
    Date,
    SmallInteger
)
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel



class ApplicantBasicDetails(SQLModel, table=True):

    __tablename__ = "applicant_basic_details"


    id: int | None = Field(
        default=None,
        sa_column=Column(
            BigInteger,
            Identity(always=True),
            primary_key=True,
        ),
    )


    party_id: int = Field(
        sa_column=Column(
            BigInteger,
            ForeignKey("case_customers.id", ondelete="CASCADE"),
            nullable=False,
        )
    )


    full_name: str = Field(sa_column=Column(String(150), nullable=False))

    name_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    name_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    gender: Optional[str] = Field(default=None, sa_column=Column(String(20)))

    gender_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    gender_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    date_of_birth: Optional[date] = Field(default=None, sa_column=Column(Date))

    dob_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    dob_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    age_years: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))
    father_spouse_name: Optional[str] = Field(default=None, sa_column=Column(String(150)))

    father_spouse_name_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    application_category: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    marital_status: Optional[str] = Field(default=None, sa_column=Column(String(20)))

    profile_risk: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    preferred_language: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    mobile_number: Optional[str] = Field(default=None, sa_column=Column(String(15)))

    mobile_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    alternate_mobile_number: Optional[str] = Field(default=None, sa_column=Column(String(15)))

    email_id: Optional[str] = Field(default=None, sa_column=Column(String(150)))

    driving_license_number: Optional[str] = Field(default=None, sa_column=Column(String(30)))

    driving_license_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    driving_license_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    driving_license_expiry: Optional[date] = Field(default=None, sa_column=Column(Date))

    voter_id_number: Optional[str] = Field(default=None, sa_column=Column(String(30)))

    voter_id_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    voter_id_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    passport_number: Optional[str] = Field(default=None, sa_column=Column(String(30)))

    passport_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    passport_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    passport_expiry: Optional[date] = Field(default=None, sa_column=Column(Date))

    face_liveliness_image_url: Optional[str] = Field(default=None, sa_column=Column(Text))

    face_liveliness_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    face_liveliness_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    created_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    )

    updated_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False
        )
    )
