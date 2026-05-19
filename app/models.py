from app.database import Base , engine

from sqlalchemy import Column , Integer , String , Boolean

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer,  primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)
    


