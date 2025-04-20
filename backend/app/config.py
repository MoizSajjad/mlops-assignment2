#Purpose: Environment configs (DB connection, secret key)
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "postgresql://postgres:postgres@database:5432/postgres")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "super-secret")
