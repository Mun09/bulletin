# main.py
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from .models import User

# PostgreSQL 데이터베이스 연결 설정
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/dbname"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 모델 정의
Base = declarative_base()

# FastAPI 애플리케이션 설정
app = FastAPI()

def setup_database():
    # 데이터베이스 테이블을 생성하거나 기존의 테이블을 업데이트합니다.
    Base.metadata.create_all(bind=engine)

# 데이터베이스 세션 의존성 추가
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 사용자 생성 엔드포인트
@app.post("/users/")
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    hashed_password = password  # 실제로는 비밀번호를 해싱하여 저장해야 함
    db_user = User(username=username, email=email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
