def create_sharepoint_directory(dir_name: str):
    """
    Creates a folder in the sharepoint directory.
    """
    if dir_name:

        ctx = get_sharepoint_context_using_app()

        result = ctx.web.folders.add(f'Shared Documents/{dir_name}').execute_query()

        if result:
            # documents is titled as Shared Documents for relative URL in SP
            relative_url = f'Shared Documents/{dir_name}'
            return relative_url

create_sharepoint_directory('test directory')
