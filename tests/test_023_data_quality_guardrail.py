import unittest

from loan_covenant_watch.models import Record
from loan_covenant_watch.scoring import score_record


class DepthCheck23(unittest.TestCase):
    def test_023_data_quality_guardrail(self):
        record = Record(id="borrower-023", exposure=58764, signal=0.736, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
