# app/models/case_customer.py
from __future__ import annotations

from datetime import datetime, date
from decimal import Decimal

from sqlalchemy import (
    TIMESTAMP,
    BigInteger,
    Column,
    Identity,
    Numeric,
    String,
    Integer,
    Date,
    ForeignKey,
    Boolean,
)
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.sql import func
from sqlmodel import Field, SQLModel
from typing import Optional


# ---------------------------------------
# Case Customer Model
# ---------------------------------------
class CaseCustomer(SQLModel, table=True):
    __tablename__ = "case_customers"

    # Primary key (auto-increment)
    id: int = Field(
        default=None,
        sa_column=Column(
            BigInteger,
            Identity(always=True),
            primary_key=True,
            autoincrement=True,
        ),
    )

    # FK: cases.id
    case_id: int = Field(
        sa_column=Column(
            BigInteger,
            ForeignKey("cases.id", ondelete="CASCADE"),
            nullable=False,
        )
    )

    # FK: customers.id
    customer_id: int = Field(
        sa_column=Column(
            BigInteger,
            ForeignKey("customers.id", ondelete="CASCADE"),
            nullable=False,
        )
    )

    # User info
    first_name: str | None = Field(
        default=None, sa_column=Column(String(100), nullable=True)
    )

    middle_name: str | None = Field(
        default=None, sa_column=Column(String(100), nullable=True)
    )

    last_name: str | None = Field(
        default=None, sa_column=Column(String(100), nullable=True)
    )

    dob: Optional[date] = Field(default=None, sa_column=Column(Date, nullable=True))

    email: str | None = Field(
        default=None,
        sa_column=Column(CITEXT(), nullable=True),
    )

    mobile_number: str = Field(
        sa_column=Column(String(15), nullable=False),
    )

    alternate_mobile_number: str | None = Field(
        default=None, sa_column=Column(String(15), nullable=True)
    )

    language: str | None = Field(
        default=None, sa_column=Column(String(50), nullable=True)
    )

    impairment_status: bool | None = Field(
        default=None, sa_column=Column(Boolean, nullable=True)
    )

    impairment_type: str | None = Field(
        default=None, sa_column=Column(String, nullable=True)
    )

    impairment_percentage: Decimal | None = Field(
        default=None,
        sa_column=Column(
            Numeric(5, 2),
            nullable=True,
        ),
    )

    udid_number: str | None = Field(
        default=None, sa_column=Column(String, nullable=True)
    )

    pincode: str | None = Field(
        default=None, sa_column=Column(String(10), nullable=True)
    )

    customer_type: str | None = Field(
        default=None, sa_column=Column(String(25), nullable=True)
    )

    cibil_score: str | None = Field(
        default=None, sa_column=Column(String(20), nullable=True)
    )

    ucic_id: int | None = Field(default=None, sa_column=Column(Integer, nullable=True))

    status: str | None = Field(
        default=None, sa_column=Column(String(40), nullable=True)
    )

    gender: str | None = Field(
        default=None, sa_column=Column(String(25), nullable=True)
    )

    is_default: bool | None = Field(
        default=False, sa_column=Column(Boolean, nullable=True)
    )

    is_funding: bool | None = Field(
        default=False, sa_column=Column(Boolean, nullable=True)
    )

    remarks: str | None = Field(
        default=None, sa_column=Column(String(255), nullable=True)
    )

    ckyc_id: str | None = Field(
        default=None, sa_column=Column(String(100), nullable=True)
    )

    # --- Timestamp fields (declared last to preserve order) ---
    created_at: datetime | None = Field(
        sa_column=Column(
            "created_at",
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        )
    )

    updated_at: datetime | None = Field(
        sa_column=Column(
            "updated_at",
            TIMESTAMP(timezone=True),
            nullable=True,
            onupdate=func.now(),
        )
    )

    deleted_at: datetime | None = Field(
        sa_column=Column(
            "deleted_at",
            TIMESTAMP(timezone=True),
            nullable=True,
        )
    )
