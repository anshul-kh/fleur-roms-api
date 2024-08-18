from prisma import Client, register

db  = Client()
register(db)