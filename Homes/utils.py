APARTMENT = 'apartment'
INDEPENDENT = 'independent'
VILLA = 'villa'

HouseTypeCategories = (
    (APARTMENT, 'Apartment'),
    (INDEPENDENT, 'Independent'),
    (VILLA, 'Villa'),
)

FULLY_FURNISHED = 'full'
SEMI_FURNISHED = 'semi'
UNFURNISHED = 'nil'

HouseFurnishTypeCategories = (
    (FULLY_FURNISHED, 'Fully furnished'),
    (SEMI_FURNISHED, 'Semi furnished'),
    (UNFURNISHED, 'Unfurnished')
)

GIRLS = 'girls'
BOYS = 'boys'
FAMILY = 'family'

HouseAccomodationAllowedCategories = (
    (GIRLS, 'Girls'),
    (BOYS, 'Boys'),
    (FAMILY, 'Family')
)

FLAT = 'flat'
PRIVATE_ROOM = 'private'
SHARED_ROOM = 'shared'

HouseAccomodationTypeCategories = (
    (SHARED_ROOM, 'Shared rooms'),
    (PRIVATE_ROOM, 'Private rooms'),
    (FLAT, 'Entire house'),
)

AmenityTypeCategories = (
    ('In-House', 'In-House'),
    ('Society', 'Society')
)

default_profile_pic_url = "https://d28fujbigzf56k.cloudfront.net/static/img/nopic.jpg"


def get_house_picture_upload_path(instance, filename):
    return "House/{}/{}/{}".format(instance.house.id, instance.house.pictures.count(), filename.split('/')[-1])


def get_amenity_picture_upload_path(instance, filename):
    return "Amenity/{}.{}".format(instance.name, filename.split('.')[-1])


def get_sub_amenity_picture_upload_path(instance, filename):
    return "SubAmenity/{}.{}".format(instance.name, filename.split('.')[-1])


def get_house_owner_profile_pic_upload_path(instance, filename):
    return "HouseOwner/{}/{}".format(instance.user.id, filename.split('/')[-1])

