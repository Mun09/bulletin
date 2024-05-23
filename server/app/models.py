from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy 모델의 기본 클래스
Base = declarative_base()
 
class Post(BaseModel):
    id: Optional[int] = Field(default=None, description="게시물의 고유 식별자")
    title: str = Field(..., description="게시물의 제목")
    content: str = Field(..., description="게시물의 내용")
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc), description="게시물 생성 타임스탬프")
    updated_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc), description="게시물 마지막 수정 타임스탬프")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)