import requests
import json
import enum
import urllib.parse
import canvas_api.objects.enrollment

class enrollment_service:
    class enrollment_type(enum.StrEnum):
        StudentEnrollment = "StudentEnrollment"
        TeacherEnrollment = "TeacherEnrollment"
        TaEnrollment = "TaEnrollment"
        ObserverEnrollment = "ObserverEnrollment"
        DesignerEnrollment = "DesignerEnrollment"

    class enrollment_state(enum.StrEnum):
        Active = "active"
        Invited = "invited"
        Inactive = "inactive"
    

    def __init__(self, domain_address: str, access_token: str):
        self.address = domain_address + "/courses/"
        self.access_token = access_token
    
    def enroll(self, course_id: int, user_id: str, start_at=None, end_at=None, type=None, role=None, role_id=None, enrollment_state=None,
               course_section_id=None, limit_privileges_to_course_section=None, notify=None, self_enrollment_code=None, self_enrolled=None,
               associated_user_id=None, sis_user_id=None, integration_id=None, root_account=None):
        
        address = self.address + str(course_id) + "/enrollments"

        enroll_dict = {
            "enrollment[user_id]": user_id,
            "enrollment[start_at]": start_at,
            "enrollment[end_at]": end_at,
            "enrollment[type]": type,
            "enrollment[role]": role,
            "enrollment[role_id]": role_id,
            "enrollment[enrollment_state]": enrollment_state,
            "enrollment[course_section_id]": course_section_id,
            "enrollment[limit_privileges_to_course_section]": limit_privileges_to_course_section,
            "enrollment[notify]": notify,
            "enrollment[self_enrollment_code]": self_enrollment_code,
            "enrollment[self_enrolled]": self_enrolled,
            "enrollment[associated_user_id]": associated_user_id,
            "enrollment[sis_user_id]": sis_user_id,
            "enrollment[integration_id]": integration_id,
            "enrollment[root_account]": root_account
        }

        data_string = ""
        for key, value in enroll_dict.items():
            if value:
                data_string += f"{key}={value}&"
        #data_string = urllib.parse.quote(data_string.strip().rstrip("&"))
        data_string = data_string.strip().rstrip('&')
        print(address)
        print(data_string)
        result = requests.post(address, headers=dict(Authorization=f"Bearer {self.access_token}"), data=data_string)
        if result.status_code != 200:
            print("Error enrolling user.")
            return result.status_code, result.content
        enrollment = canvas_api.objects.enrollment.enrollment(**json.loads(result.content))
        return result.status_code, enrollment