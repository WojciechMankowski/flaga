from app import db, User

# db.create_all()
user = User(name="Wojciech Mankowski", password="Wojtek92!", e_mail="wojtekm510@gmail.com")
db.session.add(user)
db.session.commit()