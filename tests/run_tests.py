import subprocess
from datetime import datetime

current_date_time = datetime.now()
test_run_name = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
qase_api_token = "c1aa598a817f528a7628de41f3c5ebb3967cef92428ce4626add14c914e27531"

subprocess.run(["pytest", "tests.py", "--qase-testops-api-token"
                                      f"={qase_api_token}",
                "--qase-testops-project=B24TAP", f"--qase-testops-run-title={test_run_name}"])
