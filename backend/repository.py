from backend.connection import db

class Repository:

    model = None
    session = db.session

    @classmethod
    def get_all(cls) -> list:
        return cls.model.query.all()

    @classmethod
    def add(cls, instance: db.Model) -> None:
        return cls.session.add(instance)

    @classmethod
    def commit(cls):
        cls.session.commit()

    @classmethod
    def rollback(cls):
        cls.session.rollback()
