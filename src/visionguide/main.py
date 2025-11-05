"""
Minimal CLI stub for local flow testing.
No external dependencies required.
"""
from pathlib import Path

def run():
    print("VisionGuide Core – stub")
    cfg = Path(__file__).parent.parent / "config.example.yaml"
    if cfg.exists():
        print(f"Found example config: {cfg}")
    else:
        print("config.example.yaml not found")

if __name__ == "__main__":
    run()