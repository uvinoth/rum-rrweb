from __future__ import annotations

from datetime import datetime
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
    SmallInteger
)
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel


class ApplicantAddressDetails(SQLModel, table=True):

    __tablename__ = "applicant_address_details"


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

    current_address_line: Optional[str] = Field(default=None, sa_column=Column(Text))
    current_address_city: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    current_address_pin: Optional[str] = Field(default=None, sa_column=Column(String(10)))
    current_address_state: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    current_address_landmark: Optional[str] = Field(default=None, sa_column=Column(String(150)))
    current_address_ownership_status: Optional[str] = Field(
        default=None, sa_column=Column(String(50))
    )

    current_address_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    current_address_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    years_at_current_address: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))

    permanent_address_line: Optional[str] = Field(default=None, sa_column=Column(Text))
    permanent_address_city: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    permanent_address_pin: Optional[str] = Field(default=None, sa_column=Column(String(10)))
    permanent_address_state: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    permanent_address_landmark: Optional[str] = Field(default=None, sa_column=Column(String(150)))

    permanent_address_ownership_status: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    permanent_address_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    permanent_address_verified_via: Optional[str] = Field(default=None, sa_column=Column(String(50)))

    negative_area: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    negative_area_verified: bool = Field(
        default=False,
        sa_column=Column(Boolean, nullable=False, server_default="false")
    )

    mailing_address_line: Optional[str] = Field(default=None, sa_column=Column(Text))
    mailing_address_city: Optional[str] = Field(default=None, sa_column=Column(String(100)))
    mailing_address_pin: Optional[str] = Field(default=None, sa_column=Column(String(10)))
    mailing_address_state: Optional[str] = Field(default=None, sa_column=Column(String(50)))
    mailing_address_landmark: Optional[str] = Field(default=None, sa_column=Column(String(150)))

    istance_from_branch_km: Optional[int] = Field(default=None, sa_column=Column(SmallInteger))

    distance_from_branch_verified: bool = Field(
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
