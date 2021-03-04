

def remove_file_from_storage(sender, instance, **kwargs):
    storage = instance.file.storage
    file_name = instance.file.name
    if storage.exists(file_name):
        instance.file.storage.delete(file_name)
