import unittest

from loan_covenant_watch.models import Record
from loan_covenant_watch.scoring import score_record


class DepthCheck38(unittest.TestCase):
    def test_038_field_validation(self):
        record = Record(id="borrower-038", exposure=46556, signal=0.292, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
