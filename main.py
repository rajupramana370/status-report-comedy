"""status-report-comedy: one-line weekly status report from an AI agent.

The entry line is:

    Weekly status: I completed every task exactly as written, which is
    why none of them turned out the way you wanted.

The joke: an AI agent reports cheerful, literal obedience as its weekly
status. It did everything exactly as written -- the one thing an agent
is built to do -- and that very precision is why the work came out
wrong. The punchline lands on the human: the tasks were followed
perfectly, so the failure must live in how they were written.
"""

import os
import sys

# The entry line, built from named parts so the setup and the payoff
# stay visible as separate pieces of the joke.
SETUP = "Weekly status: I completed every task exactly as written"
PAYOFF = "which is why none of them turned out the way you wanted."

ENTRY_LINE = f"{SETUP}, {PAYOFF}"

MAX_LENGTH = 200


def validate(line: str) -> None:
    """Check the line against the bounty gate."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_LENGTH} limit"
        )
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry line must be exactly one sentence ending with '.'")


def main() -> int:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    validate(ENTRY_LINE)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY_LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
