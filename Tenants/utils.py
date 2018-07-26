def get_tenant_document_upload_path(instance, filename):
    return "Tenants/{}/documents/{}/{}".format(instance.tenant.user.id, instance.type, filename.split('/')[-1])
