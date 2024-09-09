class enrollment():
    # The ID of the enrollment.
    id = None
    # The unique id of the course.
    course_id = None
    # The SIS Course ID in which the enrollment is associated. Only displayed if
    # present. This field is only included if the user has permission to view SIS
    # information.
    sis_course_id = None
    # The Course Integration ID in which the enrollment is associated. This field
    # is only included if the user has permission to view SIS information.
    course_integration_id = None
    # The unique id of the user's section.
    course_section_id = None
    # The Section Integration ID in which the enrollment is associated. This field
    # is only included if the user has permission to view SIS information.
    section_integration_id = None
    # The SIS Account ID in which the enrollment is associated. Only displayed if
    # present. This field is only included if the user has permission to view SIS
    # information.
    sis_account_id = None
    # The SIS Section ID in which the enrollment is associated. Only displayed if
    # present. This field is only included if the user has permission to view SIS
    # information.
    sis_section_id = None
    # The SIS User ID in which the enrollment is associated. Only displayed if
    # present. This field is only included if the user has permission to view SIS
    # information.
    sis_user_id = None
    # The state of the user's enrollment in the course.
    enrollment_state = None
    # User can only access his or her own course section.
    limit_privileges_to_course_section = None
    # The unique identifier for the SIS import. This field is only included if the
    # user has permission to manage SIS information.
    sis_import_id = None
    # The unique id of the user's account.
    root_account_id = None
    # The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment',
    # 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'.
    type = None
    # The unique id of the user.
    user_id = None
    # The unique id of the associated user. Will be null unless type is
    # ObserverEnrollment.
    associated_user_id = None
    # The enrollment role, for course-level permissions. This field will match
    # `type` if the enrollment role has not been customized.
    role = None
    # The id of the enrollment role.
    role_id = None
    # The created time of the enrollment, in ISO8601 format.
    created_at = None
    # The updated time of the enrollment, in ISO8601 format.
    updated_at = None
    # The start time of the enrollment, in ISO8601 format.
    start_at = None
    # The end time of the enrollment, in ISO8601 format.
    end_at = None
    # The last activity time of the user for the enrollment, in ISO8601 format.
    last_activity_at = None
    # The last attended date of the user for the enrollment in a course, in ISO8601
    # format.
    last_attended_at = None
    # The total activity time of the user for the enrollment, in seconds.
    total_activity_time = None
    # The URL to the Canvas web UI page for this course enrollment.
    html_url = None
    # The URL to the Canvas web UI page containing the grades associated with this
    # enrollment.
    grades = None
    # A description of the user.
    user = None
    # The user's override grade for the course.
    override_grade = None
    # The user's override score for the course.
    override_score = None
    # The user's current grade in the class including muted/unposted assignments.
    # Only included if user has permissions to view this grade, typically teachers,
    # TAs, and admins.
    unposted_current_grade = None
    # The user's final grade for the class including muted/unposted assignments.
    # Only included if user has permissions to view this grade, typically teachers,
    # TAs, and admins..
    unposted_final_grade = None
    # The user's current score in the class including muted/unposted assignments.
    # Only included if user has permissions to view this score, typically teachers,
    # TAs, and admins..
    unposted_current_score = None
    # The user's final score for the class including muted/unposted assignments.
    # Only included if user has permissions to view this score, typically teachers,
    # TAs, and admins..
    unposted_final_score = None
    # optional: Indicates whether the course the enrollment belongs to has grading
    # periods set up. (applies only to student enrollments, and only available in
    # course endpoints)
    has_grading_periods = None
    # optional: Indicates whether the course the enrollment belongs to has the
    # Display Totals for 'All Grading Periods' feature enabled. (applies only to
    # student enrollments, and only available in course endpoints)
    totals_for_all_grading_periods_option = None
    # optional: The name of the currently active grading period, if one exists. If
    # the course the enrollment belongs to does not have grading periods, or if no
    # currently active grading period exists, the value will be null. (applies only
    # to student enrollments, and only available in course endpoints)
    current_grading_period_title = None
    # optional: The id of the currently active grading period, if one exists. If
    # the course the enrollment belongs to does not have grading periods, or if no
    # currently active grading period exists, the value will be null. (applies only
    # to student enrollments, and only available in course endpoints)
    current_grading_period_id = None
    # The user's override grade for the current grading period.
    current_period_override_grade = None
    # The user's override score for the current grading period.
    current_period_override_score = None
    # optional: The student's score in the course for the current grading period,
    # including muted/unposted assignments. Only included if user has permission to
    # view this score, typically teachers, TAs, and admins. If the course the
    # enrollment belongs to does not have grading periods, or if no currently
    # active grading period exists, the value will be null. (applies only to
    # student enrollments, and only available in course endpoints)
    current_period_unposted_current_score = None
    # optional: The student's score in the course for the current grading period,
    # including muted/unposted assignments and including ungraded assignments with
    # a score of 0. Only included if user has permission to view this score,
    # typically teachers, TAs, and admins. If the course the enrollment belongs to
    # does not have grading periods, or if no currently active grading period
    # exists, the value will be null. (applies only to student enrollments, and
    # only available in course endpoints)
    current_period_unposted_final_score = None
    # optional: The letter grade equivalent of
    # current_period_unposted_current_score, if available. Only included if user
    # has permission to view this grade, typically teachers, TAs, and admins. If
    # the course the enrollment belongs to does not have grading periods, or if no
    # currently active grading period exists, the value will be null. (applies only
    # to student enrollments, and only available in course endpoints)
    current_period_unposted_current_grade = None
    # optional: The letter grade equivalent of current_period_unposted_final_score,
    # if available. Only included if user has permission to view this grade,
    # typically teachers, TAs, and admins. If the course the enrollment belongs to
    # does not have grading periods, or if no currently active grading period
    # exists, the value will be null. (applies only to student enrollments, and
    # only available in course endpoints)
    current_period_unposted_final_grade = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if enrollment.__dict__.__contains__(key):
                self.__dict__.update({ key : value })
            else:
                print(f"No matching field '{key}'")