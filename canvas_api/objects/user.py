class user():
    # Internal Canvas ID
    id = -1
    # Full Name
    name = "John Doe"
    # Name for Sorting
    sortable_name = "Doe, John"
    # Last Name
    last_name = "Doe"
    # First Name
    first_name = "John"
    # SIS ID associated with the user. Only appears if imported via SIS and getter has SIS permissions.
    sis_user_id = None
    # ID of the SIS import. Same restrictions as the sis_user_id
    sis_import_id = None
    # Associated integration ID. Also an SIS field, and has the same restrictions as sis_user_id
    integration_id = None
    # Unique Login ID for the user. Used to log in.
    login_id = "johndoe@example.com"
    # If Avatars are enabled, this field will be included and contain a link to the user's avatar.
    avatar_url = "https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
    # If Avatars are enabled and the getter is an admin, contains the current state of the user's avatar.
    avatar_state = "approved"
    # A list of the user's active enrollments.
    enrollments = []
    # Can be requested by certain api calls. Returns the user's primary email address.
    email = "johndoe@example.com"
    # Can be requested by certain api calls. Returns the user's locale in RFC 5646 format.
    locale = "en"
    # Only returned in certain api calls. Returns the timestamp of the user's last login.
    last_login = "2012-05-30T17:45:25Z"
    # Only returned in certain api calls. Returns the IANA time zone of the user.
    time_zone = "America/New_York"
    # The user's bio.
    bio = "I am a Canvas user."
    # Returned if pronouns are enabled. Contains the user's pronouns.
    pronouns = "he/him"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if user.__dict__.__contains__(key):
                self.__dict__.update({ key : value })
            else:
                print(f"No matching field '{key}'")
