HouseTypeCategories = (
    ('Apartment', 'Apartment'),
    ('Independent', 'Independent'),
    ('Villa', 'Villa'),
)

HouseFurnishTypeCategories = (
    ('Fully furnished', 'Fully furnished'),
    ('Semi furnished', 'Semi furnished'),
    ('Unfurnished', 'Unfurnished')
)

HouseAccomodationAllowedCategories = (
    ('Girls', 'Girls'),
    ('Boys', 'Boys'),
    ('Family', 'Family')
)

FLAT = 'flat'
PRIVATE_ROOM = 'private'
SHARED_ROOM = 'shared'

HouseAccomodationTypeCategories = (
    ('shared', 'Shared rooms'),
    ('private', 'Private rooms'),
    ('flat', 'Entire house'),
)

AmenityTypeCategories = (
    ('In-House', 'In-House'),
    ('Society', 'Society')
)


def get_house_picture_upload_path(instance, filename):
    return "House/{}/{}/{}".format(instance.house.id, instance.house.pictures.count(), filename.split('/')[-1])


def get_amenity_picture_upload_path(instance, filename):
    return "Amenity/{}.{}".format(instance.name, filename.split('.')[-1])


def get_sub_amenity_picture_upload_path(instance, filename):
    return "SubAmenity/{}.{}".format(instance.name, filename.split('.')[-1])

