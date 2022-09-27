
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext


def get_sharepoint_context_using_user():
 
    # Get sharepoint credentials
    sharepoint_url = 'https://{your-tenant-prefix}.sharepoint.com'

    # Initialize the client credentials
    user_credentials = UserCredential(<your username>, <your password>)

    # create client context object
    ctx = ClientContext(sharepoint_url).with_credentials(user_credentials)

    return ctx
