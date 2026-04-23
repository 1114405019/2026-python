import subprocess
import sys

def run_test(script_name, input_str):
    process = subprocess.Popen(
        [sys.executable, script_name],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_str)
    return stdout.strip()

def main():
    # Example 1: n=2, nums=[10, 10] -> median 10, count 2, possible 1
    # Example 2: n=4, nums=[1, 2, 2, 4] -> median 2, count 2, possible 1 (range [2, 2])
    test_input = "2\n10 10\n4\n1 2 2 4"
    expected_output = "10 2 1\n2 2 1"
    
    scripts = ["q10057.py", "q10057-detail.py", "q10057-easy.py", "q10057-Hand-typed.py"]
    
    for script in scripts:
        print(f"Testing {script}...")
        actual_output = run_test(script, test_input)
        if actual_output.replace("\r", "") == expected_output:
            print(f"  {script} PASSED")
        else:
            print(f"  {script} FAILED")
            print(f"    Expected:\n{expected_output}")
            print(f"    Actual:\n{actual_output}")

if __name__ == "__main__":
    main()
