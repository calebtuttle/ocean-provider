#
# Copyright 2021 Ocean Protocol Foundation
# SPDX-License-Identifier: Apache-2.0
#
from sqlalchemy import Column, String

from .database import Base


class UserNonce(Base):
    """
    Table for storing the nonce values for the Eth account addresses.
    """

    __tablename__ = "user_nonce"

    address = Column(String(255), nullable=False, primary_key=True, autoincrement=False)
    nonce = Column(String(255), nullable=False)
