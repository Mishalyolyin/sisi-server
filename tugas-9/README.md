# 🧪 Automated Testing - Django LMS Project

Proyek ini adalah implementasi automated testing untuk backend LMS (Learning Management System) menggunakan Django dan Django Ninja. Project ini menguji beberapa aspek utama aplikasi melalui:

- ✅ Unit Testing
- ✅ Integration Testing (API)
- ✅ Load Testing (Locust)

---

## 📦 Framework & Tools

- **Python 3.13**
- **Django 5.2**
- **Django Ninja**
- **Locust**

---

## 🚀 Struktur Testing

### ✅ 1. Unit Testing

Menggunakan `unittest` bawaan Django untuk menguji:

- Fungsi `calculator()`  
- Fungsi `validate_password()`

File: `lms_core/tests.py`

```python
def test_addition(self):
    self.assertEqual(calculator(1, 2, '+'), 3)

def test_valid_password(self):
    self.assertTrue(validate_password("Abcd1234!"))
