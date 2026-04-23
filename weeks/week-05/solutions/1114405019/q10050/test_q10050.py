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
    # Based on the example in the problem description:
    # N=14 days, P=3 parties, h1=3, h2=4, h3=8
    # Expected: 5 days (3, 4, 8, 9, 12)
    test_input = "1\n14\n3\n3\n4\n8"
    expected_output = "5"
    
    scripts = ["q10050.py", "q10050-detail.py", "q10050-easy.py", "q10050-Hand-typed.py"]
    
    for script in scripts:
        print(f"Testing {script}...")
        actual_output = run_test(script, test_input)
        if actual_output == expected_output:
            print(f"  {script} PASSED")
        else:
            print(f"  {script} FAILED")
            print(f"    Expected: {expected_output}")
            print(f"    Actual:   {actual_output}")

if __name__ == "__main__":
    main()
