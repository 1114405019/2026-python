import subprocess
import sys
from pathlib import Path


def normalize(text: str) -> str:
    """標準化輸出：移除末端空白並統一換行符號。"""
    return '\n'.join(line.rstrip() for line in text.strip().splitlines())


def main():
    sample_input = '''4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
'''

    expected_output = '''Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100'''

    script_dir = Path(__file__).resolve().parent
    ai_path = script_dir / '10189_ai.py'
    result = subprocess.run(
        [sys.executable, str(ai_path)],
        input=sample_input,
        text=True,
        capture_output=True,
    )

    if result.returncode != 0:
        print('測試失敗：程式回傳非零狀態碼')
        print('stderr:')
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
