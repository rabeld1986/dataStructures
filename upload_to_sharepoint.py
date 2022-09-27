from office365.sharepoint.client_context import ClientContext

def upload_to_sharepoint(dir_name: str, file_name: str):

    sp_relative_url = create_sharepoint_directory(dir_name)
    ctx = get_sharepoint_context()

    target_folder = ctx.web.get_folder_by_server_relative_url(sp_relative_url)

    with open(file_name, 'rb') as content_file:
        file_content = content_file.read()
        target_folder.upload_file(file_name, file_content).execute_query()
