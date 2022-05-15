#!/usr/bin/python3
""" State Module for HBNB project """

import os
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    name = ""
