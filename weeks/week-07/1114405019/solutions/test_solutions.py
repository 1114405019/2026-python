import re
import sys
import subprocess
from pathlib import Path


INPUT_LABEL_PATTERN = re.compile(r'^\s*(?:輸入|Input|Sample Input)\s*:\s*(.*)$')
OUTPUT_LABEL_PATTERN = re.compile(r'^\s*(?:輸出|Output|Sample Output)\s*:\s*(.*)$')


def normalize_text(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip("\n")


def extract_section(lines, title):
    start = None
    end = len(lines)
    for i, line in enumerate(lines):
        if line.strip() == title:
            start = i + 1
            break
    if start is None:
        return []
    for j in range(start, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    section = lines[start:end]
    leading = 0
    while leading < len(section) and section[leading].strip() == "":
        leading += 1
    if leading < len(section) and section[leading].strip().startswith("```"):
        fence = section[leading].strip()
        for k in range(leading + 1, len(section)):
            if section[k].strip() == fence:
                return section[leading + 1:k]
    return section


def read_block(lines, start):
    if start < len(lines) and lines[start].strip().startswith("```"):
        fence = lines[start].strip()
        block = []
        i = start + 1
        while i < len(lines) and lines[i].strip() != fence:
            block.append(lines[i])
            i += 1
        return "\n".join(block).strip("\n"), i + 1

    block = []
    i = start
    while i < len(lines):
        line = lines[i]
        if INPUT_LABEL_PATTERN.match(line) or OUTPUT_LABEL_PATTERN.match(line) or line.startswith("## "):
            break
        block.append(line)
        i += 1
    return "\n".join(block).strip("\n"), i


def extract_samples(markdown: str):
    lines = markdown.splitlines()
    section = extract_section(lines, "## 測試用例")
    if not section:
        section = lines

    samples = []
    current_input = None
    current_output = None
    i = 0
    while i < len(section):
        line = section[i]
        input_match = INPUT_LABEL_PATTERN.match(line)
        if input_match:
            if current_input is not None and current_output is not None:
                samples.append((current_input, current_output))
                current_input = None
                current_output = None
            content = input_match.group(1).strip()
            if content:
                current_input = content
                i += 1
            else:
                current_input, i = read_block(section, i + 1)
            continue

        output_match = OUTPUT_LABEL_PATTERN.match(line)
        if output_match:
            content = output_match.group(1).strip()
            if content:
                current_output = content
                i += 1
            else:
                current_output, i = read_block(section, i + 1)
            if current_input is not None and current_output is not None:
                samples.append((current_input, current_output))
                current_input = None
                current_output = None
            continue

        i += 1

    if current_input is not None and current_output is not None:
        samples.append((current_input, current_output))

    if samples:
        return samples

    labels = []
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped in {"輸入:", "Input:", "Sample Input:"}:
            labels.append(("input", idx))
        elif stripped in {"輸出:", "Output:", "Sample Output:"}:
            labels.append(("output", idx))

    i = 0
    while i < len(labels) - 1:
        kind, idx = labels[i]
        next_kind, next_idx = labels[i + 1]
        if kind == "input" and next_kind == "output":
            input_lines = lines[idx + 1:next_idx]
            end_idx = len(lines)
            if i + 2 < len(labels):
                end_idx = labels[i + 2][1]
            output_lines = lines[next_idx + 1:end_idx]
            samples.append(("\n".join(input_lines).strip("\n"), "\n".join(output_lines).strip("\n")))
            i += 2
        else:
            i += 1
    return samples


def run_solution(solution_path: Path, input_text: str):
    result = subprocess.run(
        [sys.executable, str(solution_path)],
        input=input_text,
        text=True,
        capture_output=True,
    )
    return result.returncode, result.stdout, result.stderr


def find_question_id(path: Path) -> str:
    return path.stem.split("-")[-1]


def main():
    base_dir = Path(__file__).resolve().parent
    root_dir = base_dir.parent
    md_dir = root_dir
    solution_files = sorted(base_dir.glob("solution-*.py"))

    if not solution_files:
        print("No solution files found.")
        return

    total_passed = 0
    total_failed = 0
    total_skipped = 0

    for sol_path in solution_files:
        question_id = find_question_id(sol_path)
        md_path = md_dir / f"QUESTION-{question_id}.md"
        if not md_path.exists():
            print(f"[SKIP] {sol_path.name}: missing markdown QUESTION-{question_id}.md")
            total_skipped += 1
            continue

        markdown = md_path.read_text(encoding="utf-8")
        samples = extract_samples(markdown)
        if not samples:
            print(f"[SKIP] {sol_path.name}: no sample input/output found in {md_path.name}")
            total_skipped += 1
            continue

        for idx, (sample_input, sample_output) in enumerate(samples, start=1):
            returncode, stdout, stderr = run_solution(sol_path, sample_input)
            stdout_norm = normalize_text(stdout)
            expected_norm = normalize_text(sample_output)
            passed = returncode == 0 and stdout_norm == expected_norm
            name = f"{sol_path.name}#{idx}" if len(samples) > 1 else sol_path.name
            if passed:
                print(f"[PASS] {name}")
                total_passed += 1
            else:
                print(f"[FAIL] {name}")
                print("--- sample input ---")
                print(sample_input)
                print("--- expected output ---")
                print(sample_output)
                print("--- actual output ---")
                print(stdout)
                if stderr:
                    print("--- stderr ---")
                    print(stderr)
                print("--- return code ---")
                print(returncode)
                total_failed += 1

    print()
    print(f"Summary: passed={total_passed}, failed={total_failed}, skipped={total_skipped}")


if __name__ == "__main__":
    main()
