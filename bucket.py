from google.cloud import storage

my_bucket = "sake-test"


def upload_object(bucket, local_file_path, bucket_file_path):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(bucket_file_path)
    blob.upload_from_filename(local_file_path)


def list_objects(bucket):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blobs = client.list_blobs(bucket)
    objects = []
    for blob in blobs:
        objects.append(blob.name)
    return objects


def download_object(bucket, bucket_file_path, local_file_path):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(bucket_file_path)
    blob.download_to_filename(local_file_path)


def list_objects_with_prefix(bucket, prefix):
    client = storage.Client()
    blobs = client.list_blobs(bucket, prefix = prefix)
    objects = []
    for blob in blobs:
        objects.append(blob.name)
    return objects


def delete_object(bucket, bucket_file_path):
    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(bucket_file_path)
    blob.delete()


#%%
upload_object(my_bucket, "essai.txt", "chemin/monessai.txt")
upload_object(my_bucket, "essai.txt", "chemin/monessai0.txt")
upload_object(my_bucket, "essai.txt", "chemin/monessai1.txt")
upload_object(my_bucket, "essai.txt", "chemin/monessai2.txt")
upload_object(my_bucket, "essai.txt", "chemin/monessai3.txt")
upload_object(my_bucket, "essai.txt", "chemin/monessai4.txt")
upload_object(my_bucket, "essai.txt", "chemin/monessai5.txt")
upload_object(my_bucket, "essai.txt", "autrechemin/souschemin/monessai4.txt")
#%%
list_objects(my_bucket)
#%%
download_object(my_bucket, "chemin/monessai.txt", "monfichier.txt")
#%%
list_objects_with_prefix(my_bucket, "chemin/")
#%%
delete_object(my_bucket, "chemin/monessai.txt")