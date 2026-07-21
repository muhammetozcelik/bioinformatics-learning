import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

VALIDATOR = PROJECT_ROOT / "week01/day04/validate_metadata.py"

VALID_METADATA = (
    PROJECT_ROOT / "week01/day03/data/experiment_metadata.csv"
)
DUPLICATE_METADATA = (
    PROJECT_ROOT / "week01/day04/data/duplicate_metadata.csv"
)
MISSING_COLUMN_METADATA = (
    PROJECT_ROOT / "week01/day04/data/missing_column_metadata.csv"
)
INVALID_REPLICATE_METADATA = (
    PROJECT_ROOT / "week01/day04/data/invalid_replicate_metadata.csv"
)
MULTIPLE_ERRORS_METADATA = (
    PROJECT_ROOT / "week01/day04/data/multiple_errors_metadata.csv"
)


class MetadataValidatorTests(unittest.TestCase):
    def run_validator(self, metadata_path):
        return subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                str(metadata_path)
            ],
            capture_output=True,
            text=True
        )

    def test_valid_metadata(self):
        result = self.run_validator(VALID_METADATA)

        self.assertEqual(result.returncode, 0)
        self.assertIn("Metadata valid.", result.stdout)
        self.assertIn("Sample count: 6", result.stdout)

    def test_duplicate_sample_id(self):
        result = self.run_validator(DUPLICATE_METADATA)

        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate sample_id: S1", result.stdout)

    def test_missing_required_column(self):
        result = self.run_validator(MISSING_COLUMN_METADATA)

        self.assertEqual(result.returncode, 1)
        self.assertIn("Missing column: replicate", result.stdout)

    def test_invalid_replicate(self):
        result = self.run_validator(INVALID_REPLICATE_METADATA)

        self.assertEqual(result.returncode, 1)
        self.assertIn(
            "replicate must be an integer: two",
            result.stdout
        )

    def test_multiple_errors(self):
        result = self.run_validator(MULTIPLE_ERRORS_METADATA)

        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate sample_id: S1", result.stdout)
        self.assertIn("condition cannot be empty", result.stdout)
        self.assertIn("replicate must be positive", result.stdout)
        self.assertIn("sample_id cannot be empty", result.stdout)
        self.assertIn(
            "replicate must be an integer: x",
            result.stdout
        )


if __name__ == "__main__":
    unittest.main()
    