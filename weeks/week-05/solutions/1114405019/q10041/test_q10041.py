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
    test_input = "2\n2 2 4\n3 2 4 6"
    expected_output = "2\n4"
    
    scripts = ["q10041.py", "q10041-detail.py", "q10041-easy.py", "q10041-Hand-typed.py"]
    
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
