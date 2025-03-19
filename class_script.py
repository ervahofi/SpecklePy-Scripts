from specklepy.api.credentials import get_default_account

from specklepy.transports.server import ServerTransport

from specklepy.api.client import SpeckleClient

from specklepy.api import operations

from specklepy.objects.base import Base

from specklepy.core.api.inputs.version_inputs import CreateVersionInput


# Identify the Project and Model

project_id = "28a211b286"

model_id = "f5c0c919fa"

# Set up authentication and connection to server

client = SpeckleClient(host ="macad.speckle.xyz")

account = get_default_account()

client.authenticate_with_account(account)

transport = ServerTransport(project_id, client)


# Get a list of active projects

projects = client.active_user.get_projects(limit=3)

for project in projects.items:

    print(project.name)



# Get a specific Model by ID

my_model = client.model.get(model_id, project_id)

print(my_model.name)

# Get the Referenced Object ID of the latest Versio


versions = client.version.get_versions(model_id, project_id)
referenced_obj_id = versions.items[0].referencedObject


# Receive the referenced object (speckle object!


print("Fetching data from the server...")
objData = operations.receive(referenced_obj_id, transport)
print("Got the data!")


speckle_object = objData["@Data"]

child_obj = speckle_object["@{0;0}"][0]

child_obj["MyProp"] = "JustATest"

all_properties = child_obj.get_member_names()
typed_properties = child_obj.get_typed_member_names()
dynamic_properties = child_obj.get_dynamic_member_names()  
