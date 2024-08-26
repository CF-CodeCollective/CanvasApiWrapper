import requests

class EnrollmentService:
    def __init__(self, domain_address: str, access_token: str, course_id: int):
        self.address = domain_address + "/api/v1/courses/" + str(course_id) + "/enrollments"
        self.access_token = access_token

    def GenerateStudentEnrollment(self, studentID: int):
        return f"enrollment[user_id]=sis_user_id%3A{str(studentID)}&enrollment[type]=StudentEnrollment&enrollment[enrollment_state]=active&enrollment[notify]=true&enrollment[self_enrolled]=true"

    def EnrollStudent(self, studentID: int):
        result = requests.post(self.address, data=self.GenerateStudentEnrollment(studentID), headers=dict(Authorization=f"Bearer {self.access_token}"))
        return result.status_code, result.content