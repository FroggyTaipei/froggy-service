from storages.backends.s3boto3 import S3Boto3Storage


class PrivateStorage(S3Boto3Storage):
    default_acl = 'private'
    file_overwrite = False
    querystring_auth = True
    auto_create_bucket = True


class CleanStorage():
    """
    使用Traversal將Storage清空
    """
    def __init__(self, storage=None, **kwargs):
        self.storage = storage
        self.clean_storage(self.storage)

    def clean_file(self, path, file_list):
        for i in file_list:
            self.storage.delete(f'{path}/{i}')

    def clean_dir(self, path, dir):
        storage_list = self.storage.listdir(f'{path}{dir}/')
        self.clean_file(f'{path}{dir}/', storage_list[1])
        for i in storage_list[0]:
            self.clean_dir(f'{path}{dir}/', i)

    def clean_storage(self, storage):
        path = ''
        storage_list = storage.listdir(path)
        self.clean_file(path, storage_list[1])
        for i in storage_list[0]:
            self.clean_dir(path, i)
