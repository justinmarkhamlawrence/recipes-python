from sqlalchemy import Column, Integer, String, Sequence

from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    ingredients = Column(String, nullable=False)
    directions = Column(String, nullable=False)

    def as_dictionary(self):
        post = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "ingredients": self.ingredients,
            "directions": self.directions
        }
        return post
