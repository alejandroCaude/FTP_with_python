from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
# Crear un autorizador
authorizer = DummyAuthorizer()
# Añadir usuarios
authorizer.add_user("user", "password", ".", perm="elradfmw")
authorizer.add_anonymous("./public", perm="elradfmw")
# Crear el manejador FTP
handler = FTPHandler
handler.authorizer = authorizer
# Crear el servidor FTP, que utiliza el manejador
server = FTPServer(("192.168.1.35", 12400), handler)
# Iniciar el servidor para escuchar
server.serve_forever()
