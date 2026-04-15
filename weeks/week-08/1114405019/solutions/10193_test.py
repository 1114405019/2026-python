import subprocess
import sys
from pathlib import Path


def normalize(text: str) -> str:
    return '\n'.join(line.rstrip() for line in text.strip().splitlines())


def main():
    script_dir = Path(__file__).resolve().parent
    ai_path = script_dir / '10193_ai.py'

    sample_input = '101011 10\n1100 1010\n'
    expected_output = 'Pair #1: 1\nPair #2: 10'

    result = subprocess.run(
        [sys.executable, str(ai_path)],
        input=sample_input,
        text=True,
        capture_output=True,
    )

    if result.returncode != 0:
        print('測試失敗：程式回傳非零狀態碼')
        print(result.stderr)
        sys.exit(1)

    actual = normalize(result.stdout)
    expected = normalize(expected_output)

    if actual == expected:
        print('PASS: sample input output match')
        sys.exit(0)

    print('FAIL: output mismatch')
    print('--- expected ---')
    print(expected)
    print('--- actual ---')
    print(actual)
    sys.exit(1)


if __name__ == '__main__':
    main()
