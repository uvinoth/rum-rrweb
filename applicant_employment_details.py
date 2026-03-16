from __future__ import annotations

from datetime import datetime, date
from typing import Optional
from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Column,
    ForeignKey,
    Text,
    String,
    Identity,
    Boolean,
    Date,
    SmallInteger
)
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel


class ApplicantEmploymentDetails(SQLModel, table=True):

    __tablename__ = "applicant_employment_details"

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

    employment_type: Optional[str] = Field(
        default=None,
        sa_column=Column(String(50))
    )
    employment_industry: Optional[str] = Field(
        default=None,
        sa_column=Column(String(100))
    )

    employer_type: Optional[str] = Field(
        default=None,
        sa_column=Column(String(50))
    )

    employment_profession: Optional[str] = Field(
        default=None,
        sa_column=Column(String(100))
    )

    nature_of_business: Optional[str] = Field(
        default=None,
        sa_column=Column(String(100))
    )

    business_office_address: Optional[str] = Field(
        default=None,
        sa_column=Column(Text)
    )

    business_office_city: Optional[str] = Field(
        default=None,
        sa_column=Column(String(100))
    )

    business_office_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    negative_list: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    negative_list_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    years_at_job_or_business: Optional[int] = Field(
        default=None,
        sa_column=Column(SmallInteger)
    )

    years_at_job_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    gstin: Optional[str] = Field(
        default=None,
        sa_column=Column(String(20))
    )


    udyam_number: Optional[str] = Field(
        default=None,
        sa_column=Column(String(30))
    )

    udyam_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    date_of_incorporation: Optional[date] = Field(
        default=None,
        sa_column=Column(Date)
    )

    date_of_incorporation_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

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
