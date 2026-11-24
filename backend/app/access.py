def can_read(user_c: str, resource_c: str) -> bool:
    access = ['public', 'internal', 'confidential', 'secret']
    if user_c not in access or resource_c not in access:
        return False

    return access.index(user_c) >= access.index(resource_c)
