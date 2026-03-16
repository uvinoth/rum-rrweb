from __future__ import annotations

from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Column,
    ForeignKey,
    Identity,
    Boolean
)
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel

class ApplicantProfileCheck(SQLModel, table=True):

    __tablename__ = "applicant_profile_check"

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


    is_director_or_senior_officer: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    director_senior_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )


    is_existing_employee: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    existing_employee_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    is_resigned_employee: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    fcu_market_information: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    fcu_market_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    fcu_risk_customer: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    fcu_risk_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    npa_status: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    pos_waiver_status: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    pos_waiver_verified: bool = Field(
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
