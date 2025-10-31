import unittest
from password_generator import generate_password


class TestGeneratePassword(unittest.TestCase):
    def test_length(self):
        """Test that generated password has the correct length"""
        pwd = generate_password(12, True, True)
        self.assertEqual(len(pwd), 12)

    def test_with_digits_and_specials(self):
        """Test that password includes digits and specials when enabled"""
        pwd = generate_password(20, True, True)
        has_digit = any(ch.isdigit() for ch in pwd)
        has_special = any(ch in "!@#$%^&*()_+" for ch in pwd)
        self.assertTrue(has_digit)
        self.assertTrue(has_special)

    def test_with_digits_only(self):
        """Test password with digits but no specials"""
        pwd = generate_password(15, True, False)
        has_digit = any(ch.isdigit() for ch in pwd)
        has_special = any(ch in "!@#$%^&*()_+" for ch in pwd)
        self.assertTrue(has_digit)
        self.assertFalse(has_special)

    def test_with_special_only(self):
        """Test password with specials but no digits"""
        pwd = generate_password(15, False, True)
        has_digit = any(ch.isdigit() for ch in pwd)
        has_special = any(ch in "!@#$%^&*()_+" for ch in pwd)
        self.assertFalse(has_digit)
        self.assertTrue(has_special)

    def test_letters_only(self):
        """Test password with only letters"""
        pwd = generate_password(10, False, False)
        self.assertTrue(all(ch.isalpha() for ch in pwd))

    def test_randomness(self):
        """Test that multiple calls produce different passwords"""
        pwd1 = generate_password(12, True, True)
        pwd2 = generate_password(12, True, True)
        self.assertNotEqual(pwd1, pwd2)


if __name__ == "__main__":
    unittest.main()
