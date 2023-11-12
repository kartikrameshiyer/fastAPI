import enum
from sqlalchemy import Column,Boolean,ForeignKey, Integer,String, Enum,Text
from sqlalchemy.orm import relationship
from ..db_setup import Base
from datetime import datetime
from .mixins import Timestamp

class PostStatus(enum.Enum):
    DRAFT = 1
class Role(enum.Enum):
    teacher = 1
    student = 2
class User(Timestamp,Base):
    """User table"""
    __tablename__ = 'users'

    id =Column(Integer,primary_key= True, index=True)
    email =Column(String(100),unique = True, index=True, nullable = False)
    role =Column(Enum(Role))
    
    profile = relationship("Profile",back_populates="owner")
class Profile(Timestamp,Base):
    """Profile table"""
    __tablename__ = "profiles"

    id =Column(Integer,primary_key= True, index=True)
    first_name =Column(String(50),nullable = False)
    last_name =Column(String(50),nullable=False)
    middle_name =Column(String(50), nullable=True)
    bio =Column(Text,nullable = True)
    is_active =Column(Boolean, default=False)
    user_id =Column(Integer, ForeignKey('users.id'),index=True, nullable=False)

    owner = relationship("User",back_populates="profile")

