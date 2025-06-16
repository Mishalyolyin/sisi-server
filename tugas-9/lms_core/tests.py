# lms_core/tests/test_utils.py
from django.test import TestCase
from lms_core.utils import calculator, validate_password
from django.contrib.auth.models import User
from lms_core.models import Course, CourseMember

class CalculatorFunctionTest(TestCase):
    def test_addition(self):
        self.assertEqual(calculator(1, 2, '+'), 3)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculator(10, 0, '/')

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculator(1, 2, '%')

class PasswordValidationTest(TestCase):
    def test_valid(self):
        self.assertTrue(validate_password("Abcd1234!"))

    def test_invalid(self):
        self.assertFalse(validate_password("short"))
        
class CourseModelTest(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher', password='pass')
        self.student = User.objects.create_user(username='student', password='pass')
        self.course = Course.objects.create(name="Django", description="Basic", price=100, teacher=self.teacher)

    def test_is_member(self):
        self.assertFalse(self.course.is_member(self.student))
        CourseMember.objects.create(course_id=self.course, user_id=self.student, roles='std')
        self.assertTrue(self.course.is_member(self.student))
