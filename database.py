from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine("postgresql://jazz07:capi2022@localhost/Proyectos",echo=True)

Base = declarative_base()

SessionLocal= sessionmaker(bind=engine)