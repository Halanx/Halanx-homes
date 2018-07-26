def get_owner_profile_pic_upload_path(instance, filename):
    return "Owners/{}/{}".format(instance.user.id, filename.split('/')[-1])


def get_owner_document_upload_path(instance, filename):
    return "Owners/{}/documents/{}/{}".format(instance.owner.user.id, instance.type, filename.split('/')[-1])
