import pulumi
import pulumi_civo as civo

region = "LON1"

obj_store_cred = civo.ObjectStoreCredential("my-obj-store-cred", region=region)

obj_store = civo.ObjectStore("pulumi-state",
                         	access_key_id=obj_store_cred.access_key_id,
                         	max_size_gb=500,
                         	region=region)

pulumi.export('obj_store_cred_access_key', obj_store_cred.access_key_id)
pulumi.export('obj_store_url', obj_store.bucket_url)
pulumi.export('obj_store_name', obj_store.name)

web_server = civo.Instance("web-server", region="LON1", disk_image="ubuntu-jammy")

pulumi.export('server_id', web_server.id)
