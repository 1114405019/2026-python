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
    # 1 test case, 2 players, p=0.1666, target player 1
    # a = 0.1666, r = (1-0.1666)^2 = 0.8334^2 = 0.69455556
    # S = 0.1666 / (1 - 0.69455556) = 0.1666 / 0.30544444 = 0.5454...
    test_input = "1\n2 0.1666 1"
    expected_output = "0.5455"
    
    scripts = ["q10056.py", "q10056-detail.py", "q10056-easy.py", "q10056-Hand-typed.py"]
    
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
