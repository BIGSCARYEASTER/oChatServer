# Import the server
from cloudlink import server

# Import protocols
from cloudlink.server.protocols import clpv4, scratch

# Instantiate the server object
server = server()
server.enable_ssl(certfile="cert.pem", keyfile="privkey.pem")

# Set logging level
server.logging.basicConfig(
    level=server.logging.INFO # See python's logging library for details on logging levels.
)

bannedClients = []

# Load protocols
clpv4 = clpv4(server)
scratch = scratch(server)
clpv4.enable_motd = True
clpv4.motd_message = "INSECURE! Be careful what you say! - Bigscaryeaster"
@server.on_connect
async def on_connect(client):
    print(client, "Connected!")
@server.on_disconnect
async def on_disconnect(client):
    print(client, "Disconnected!")
# Start the server!
server.run(ip="10.0.1.197", port=3000)


# This is a template I used and you can use too! - bigscaryeaster
# This is also running forever!
