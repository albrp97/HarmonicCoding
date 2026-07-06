#!/usr/bin/env python3
"""Run lightweight workflow contract evaluations for the Harmonic Coding docs repo."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Result:
    name: str
    passed: bool
    detail: str


def load_spec(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def file_exists(root: Path, check: dict[str, Any]) -> Result:
    target = root / check["path"]
    passed = target.exists()
    return Result(check["name"], passed, f"{check['path']} {'exists' if passed else 'is missing'}")


def contains_all(root: Path, check: dict[str, Any]) -> Result:
    target = root / check["path"]
    if not target.exists():
        return Result(check["name"], False, f"{check['path']} is missing")
    content = target.read_text()
    missing = [item for item in check["all"] if item not in content]
    if missing:
        return Result(check["name"], False, f"Missing strings in {check['path']}: {', '.join(missing)}")
    return Result(check["name"], True, f"All required strings found in {check['path']}")


def glob_min(root: Path, check: dict[str, Any]) -> Result:
    matches = list(root.glob(check["pattern"]))
    minimum = int(check["min"])
    passed = len(matches) >= minimum
    return Result(check["name"], passed, f"{len(matches)} matches for {check['pattern']} (min {minimum})")


CHECK_HANDLERS = {
    "file_exists": file_exists,
    "contains_all": contains_all,
    "glob_min": glob_min,
}


def run_checks(root: Path, spec: dict[str, Any]) -> list[Result]:
    results: list[Result] = []
    for check in spec["checks"]:
        check_type = check["type"]
        handler = CHECK_HANDLERS[check_type]
        results.append(handler(root, check))
    return results


def write_report(path: Path, results: list[Result], pass_ratio: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "pass_ratio": pass_ratio,
        "results": [
            {"name": result.name, "passed": result.passed, "detail": result.detail}
            for result in results
        ],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n")


def write_markdown(path: Path, results: list[Result], pass_ratio: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Workflow Eval Report",
        "",
        f"- Pass ratio: `{pass_ratio:.2f}`",
        "",
        "| Check | Result | Detail |",
        "|---|---|---|",
    ]
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        lines.append(f"| {result.name} | {status} | {result.detail} |")
    path.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--spec", required=True)
    parser.add_argument("--threshold", type=float, default=1.0)
    parser.add_argument("--report-json", default="ai-evals/reports/workflow-report.json")
    parser.add_argument("--report-md", default="ai-evals/reports/workflow-report.md")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    spec = load_spec(root / args.spec)
    results = run_checks(root, spec)
    passed = sum(1 for result in results if result.passed)
    pass_ratio = passed / len(results) if results else 1.0

    write_report(root / args.report_json, results, pass_ratio)
    write_markdown(root / args.report_md, results, pass_ratio)

    return 0 if pass_ratio >= args.threshold else 1


if __name__ == "__main__":
    raise SystemExit(main())
