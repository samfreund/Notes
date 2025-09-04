import unittest
import freunds_lab1 as l1

class MyTestCase(unittest.TestCase):
    def test_nest_egg(self):
        self.assertEqual(l1.nest_egg(1000,2), 1166.4)
        self.assertAlmostEqual(l1.nest_egg(5555, 10), 11992.83,1)

    def test_nest_egg_2(self):
        self.assertEqual(l1.nest_egg_2(1000,2000), 10)
        self.assertEqual(l1.nest_egg_2(1234, 100000), 58)
        self.assertEqual(l1.nest_egg_2(6500, 100000), 36)

    def test_draw_triangle(self):
        self.assertEqual(l1.draw_triangle(1).rstrip(), "*")
        self.assertEqual(l1.draw_triangle(2).rstrip(), "**\n *")
        self.assertEqual(l1.draw_triangle(3).rstrip(), "***\n **\n  *")
        self.assertEqual(l1.draw_triangle(4).rstrip(), "****\n ***\n  **\n   *")

    def test_is_prime(self):
        self.assertEqual(l1.is_prime(4), False)
        self.assertEqual(l1.is_prime(15), False)
        self.assertEqual(l1.is_prime(17), True)
        self.assertEqual(l1.is_prime(29), True)

    def test_is_palindrome(self):
        self.assertTrue(l1.is_palindrome('racecar'))
        self.assertTrue(l1.is_palindrome('Racecar'), "Capitalization not correct")
        self.assertTrue(l1.is_palindrome('race car'), "Spacing not correct")
        self.assertTrue(l1.is_palindrome('r.a.c.e,c,a,r'), "Punctuation not correct")
        self.assertTrue(l1.is_palindrome('Sit on a potato pan, Otis.'), "Punctuation/Capitalization/Spacing not correct")
        self.assertFalse(l1.is_palindrome('abcdefg'))
        self.assertFalse(l1.is_palindrome("Hello there! Welcome to the test suite!"))
        self.assertFalse(l1.is_palindrome("racecarrr"))

    def test_cc_check(self):
        self.assertTrue(l1.cc_check(2020202020000000))
        self.assertFalse(l1.cc_check(1111111111111111))
        self.assertTrue(l1.cc_check(4916832471406208))
        self.assertFalse(l1.cc_check(3416832471406208))
        self.assertTrue(l1.cc_check(5408608073972181))
        self.assertFalse(l1.cc_check(5408608073972161))


if __name__ == '__main__':
    unittest.main()
