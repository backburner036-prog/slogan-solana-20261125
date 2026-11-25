"""Entry for make.fun bounty "One-Line Slogan for a Solana Wallet Agent".

One line for a Solana wallet agent: the wallet is handled for you -- send,
swap, and stash, all without lifting a finger. The slogan lands because the
triple alliteration (send, swap, stash) gives it rhythm, the turn at the end
("without lifting a finger") is the agent's promise in plain words, and it
names Solana and the wallet in the first four words, with no crypto jargon.
"""

from pathlib import Path

TEXT = "Your Solana wallet, handled — send, swap, and stash it all without lifting a finger."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=140):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def check_one_line(text):
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    words = text.split()
    assert len(words) <= 20, f"entry must be at most 20 words, got {len(words)}"
    return len(words)


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    check_one_line(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
