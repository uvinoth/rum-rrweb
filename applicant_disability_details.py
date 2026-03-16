from __future__ import annotations

from uuid import UUID, uuid4
from typing import Optional
from decimal import Decimal
from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Column,
    ForeignKey,
    String,
    Identity,
    Boolean,
    Numeric
)

from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel

class ApplicantDisabilityDetails(SQLModel, table=True):

    __tablename__ = "applicant_disability_details"


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

    impairment_status: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    type_of_impairment: Optional[str] = Field(
        default=None,
        sa_column=Column(String(100))
    )

    percentage_of_impairment: Optional[Decimal] = Field(
        default=None,
        sa_column=Column(Numeric(5, 2))
    )

    udid_number: Optional[str] = Field(
        default=None,
        sa_column=Column(String(30))
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
