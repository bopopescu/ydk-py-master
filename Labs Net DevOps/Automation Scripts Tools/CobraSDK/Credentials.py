from credentials import *
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol

# connect to the apic
auth = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
session = cobra.mit.access.MoDirectory(auth)
session.login()

# Create a Variable for your Tenant Name
# Use your initials in the name
# Example: "tenant_name = "js_Toolkit_Tenant""
tenant_name = "INITIALS_Cobra_Tenant"
# create a new tenant
root = cobra.model.pol.Uni('')
new_tenant = cobra.model.fv.Tenant(root, tenant_name)

# commit the new configuration
 config_request = cobra.mit.request.ConfigRequest()
 config_request.addMo(new_tenant)
session.commit(config_request)
