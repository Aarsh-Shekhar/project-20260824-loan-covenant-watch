import unittest

from loan_covenant_watch.models import Record
from loan_covenant_watch.scoring import score_record


class DepthCheck20(unittest.TestCase):
    def test_020_threshold_calibration(self):
        record = Record(id="borrower-020", exposure=34227, signal=0.508, urgency=8)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
