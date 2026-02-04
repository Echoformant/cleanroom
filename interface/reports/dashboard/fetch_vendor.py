import argparse
import hashlib
import urllib.request
from pathlib import Path


FILES = [
    ("https://cdn.jsdelivr.net/npm/vega@5/build/vega.min.js", "vega.min.js"),
    ("https://cdn.jsdelivr.net/npm/vega-lite@5/build/vega-lite.min.js", "vega-lite.min.js"),
    ("https://cdn.jsdelivr.net/npm/vega-embed@6/build/vega-embed.min.js", "vega-embed.min.js"),
]


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Download Vega/Vega-Lite/Vega-Embed JS into vendor/ for offline use")
    parser.add_argument("--dir", default=None, help="Output dir (default: interface/reports/dashboard/vendor)")
    args = parser.parse_args()

    base = Path(args.dir) if args.dir else (Path(__file__).resolve().parent / "vendor")
    base.mkdir(parents=True, exist_ok=True)

    for url, name in FILES:
        out = base / name
        print(f"Downloading {url} -> {out}")
        with urllib.request.urlopen(url, timeout=60) as r:
            data = r.read()
        out.write_bytes(data)
        print(f"  bytes={len(data)} sha256={sha256_bytes(data)}")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
