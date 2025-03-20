from enum import Enum
from .extensions import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Enum as SQLAlchemyEnum, func
from sqlalchemy.orm import relationship

class Categories(Enum):
    CREATIVE = "Creative"
    HEALTH = "Health"
    FITNESS = "Fitness"
    PRODUCTIVITY = "Productivity"
    FINANCIAL = "Financial"

    def __str__(self):
        return self.value 

class HabitUser(db.Model, UserMixin):  
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)

    habits = relationship("Habit", back_populates="user", cascade="all, delete-orphan")

class Habit(db.Model):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(SQLAlchemyEnum(Categories), nullable=False) 
    created = Column(Date, default=func.current_date())
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user = relationship("HabitUser", back_populates="habits") 

    def __repr__(self):
        return f"<Habit {self.name}, Category: {self.category.value}>"
    
class HabitLog(db.Model):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    habit_id = Column(Integer, ForeignKey("habits.id", ondelete="CASCADE"), nullable=False)
    date = Column(Date, nullable=False)
    comment = Column(Text, nullable=True)
    image_url = Column(String(300), nullable=True)

    habit = relationship("Habit", back_populates="logs")

