pip install e2b== 0.1.4
from e2b import Session
id = "Nodejs"
session = await Session.create(id)
await session.close()

session = await Session.create(id)
await session.filesystem.write
