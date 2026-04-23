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
    # N=3 functions, Q=4 queries
    # 2 1 3 -> query f1(f2(f3(x))). Initially all inc. Result 0.
    # 1 2 -> toggle f2 to dec.
    # 2 1 3 -> query f1(f2(f3(x))). Result 1.
    # 2 1 2 -> query f1(f2(x)). Result 1.
    test_input = "3 4\n2 1 3\n1 2\n2 1 3\n2 1 2"
    expected_output = "0\n1\n1"
    
    scripts = ["q10055.py", "q10055-detail.py", "q10055-easy.py", "q10055-Hand-typed.py"]
    
    for script in scripts:
        print(f"Testing {script}...")
        actual_output = run_test(script, test_input)
        if actual_output.replace("\r", "") == expected_output:
            print(f"  {script} PASSED")
        else:
            print(f"  {script} FAILED")
            print(f"    Expected: {expected_output!r}")
            print(f"    Actual:   {actual_output!r}")

if __name__ == "__main__":
    main()
