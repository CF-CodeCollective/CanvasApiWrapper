class user():
    # Internal Canvas ID
    id = None
    # Full Name
    name = None
    # Name for Sorting
    sortable_name = None
    # Last Name
    last_name = None
    # First Name
    first_name = None
    # SIS ID associated with the user. Only appears if imported via SIS and getter has SIS permissions.
    sis_user_id = None
    # ID of the SIS import. Same restrictions as the sis_user_id
    sis_import_id = None
    # Associated integration ID. Also an SIS field, and has the same restrictions as sis_user_id
    integration_id = None
    # Unique Login ID for the user. Used to log in.
    login_id = None
    # If Avatars are enabled, this field will be included and contain a link to the user's avatar.
    avatar_url = None
    # If Avatars are enabled and the getter is an admin, contains the current state of the user's avatar.
    avatar_state = None
    # A list of the user's active enrollments.
    enrollments = []
    # Can be requested by certain api calls. Returns the user's primary email address.
    email = None
    # Can be requested by certain api calls. Returns the user's locale in RFC 5646 format.
    locale = None
    # Only returned in certain api calls. Returns the timestamp of the user's last login.
    last_login = None
    # Only returned in certain api calls. Returns the IANA time zone of the user.
    time_zone = None
    # The user's bio.
    bio = None
    # Returned if pronouns are enabled. Contains the user's pronouns.
    pronouns = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__.update({ key : value })
