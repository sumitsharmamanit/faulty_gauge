import unittest
from detector import detector


class test_detector(unittest.TestCase):

    def setUp(self):
        pass

    def testing_stable_gauge(self):
        val1 = detector('input/stable-needle2.mp4', 1, cropX1=340, cropY1=380, cropX2=530, cropY2=570).detect()
        val2 = detector('input/stable-needle.mp4', 1, cropX1=180, cropY1=350, cropX2=350, cropY2=550).detect()
        self.assertEqual(val1, 1)
        self.assertEqual(val2, 1)

    def testing_defected_gauge(self):
        val1 = detector('input/needle2.mp4', 1, cropX1=1, cropY1=42, cropX2=1180, cropY2=1290).detect()
        val2 = detector('input/needle.mp4', 1, cropX1=1, cropY1=100, cropX2=900, cropY2=1000).detect()
        self.assertEqual(val1, 0)
        self.assertEqual(val2, 0)


if __name__ == '__main__':
    unittest.main()
