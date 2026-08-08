from __future__ import annotations

import os
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from generate_readme import is_dead, lifecycle, reference_time_from_values  # noqa: E402


class ReproducibilityTests(unittest.TestCase):
    def test_as_of_date_is_normalized_to_utc(self) -> None:
        self.assertEqual(
            reference_time_from_values("2026-08-08"),
            datetime(2026, 8, 8, tzinfo=timezone.utc),
        )

    def test_source_date_epoch_is_supported(self) -> None:
        with patch.dict(os.environ, {"SOURCE_DATE_EPOCH": "0"}):
            self.assertEqual(
                reference_time_from_values(),
                datetime(1970, 1, 1, tzinfo=timezone.utc),
            )

    def test_repository_inactivity_does_not_automatically_retire_a_tool(self) -> None:
        reference = datetime(2026, 8, 8, tzinfo=timezone.utc)
        quiet_stable = {"repo_updated_at": "2020-01-01T00:00:00Z", "catalog_status": "current"}
        self.assertEqual(lifecycle(quiet_stable, reference)[1], "Unmaintained")
        self.assertFalse(is_dead(quiet_stable, reference))

    def test_historical_status_is_an_explicit_editorial_decision(self) -> None:
        reference = datetime(2026, 8, 8, tzinfo=timezone.utc)
        historical = {
            "repo_updated_at": "2026-08-01T00:00:00Z",
            "catalog_status": "historical",
        }
        self.assertEqual(lifecycle(historical, reference)[1], "Historical")
        self.assertTrue(is_dead(historical, reference))


if __name__ == "__main__":
    unittest.main()
