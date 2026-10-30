# MLOps Internal POE — UAT Dry Run

This folder contains a simple Flask app plus sample automation and monitoring code for the internal POE.

## Files
- `hello.py`: Flask app with `/` and `/health`.
- `test_hello.py`: two Pytest tests.
- `requirements.txt`: Flask, Pytest, pandas and Evidently.
- `Dockerfile`: builds a small container with the Flask app.
- `Jenkinsfile`: Windows-agent Jenkins pipeline (checkout, install, tests, Docker build/run/health check, Evidently report).
- `monitor.py`: synthetic data-drift demo using Evidently.
- `POE_Summary_Report.pdf`: summary and verification checklist.

## Windows setup commands
Run these commands from this folder in VS Code Terminal / PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python --version
git --version
docker --version
java -version
```

If PowerShell blocks activation, use `\.venv\Scripts\python.exe -m pip install -r requirements.txt` instead.

## Dry run
```powershell
python -m pytest -v
python hello.py
```
Open `http://localhost:5000` and `http://localhost:5000/health`. Stop Flask with Ctrl+C.

In a second terminal:
```powershell
python monitor.py
```
Open `evidently_report.html` in a browser after the command completes.

## Docker dry run
```powershell
docker build -t mlops-uat-hello:latest .
docker run -d --name mlops-uat-hello -p 5001:5000 mlops-uat-hello:latest
curl.exe http://localhost:5001/health
docker ps
docker logs mlops-uat-hello
docker rm -f mlops-uat-hello
```
Port 5001 on the host avoids conflicting with SmartShelfX, which uses port 5000.

## Jenkins notes
1. Push these files to a GitHub repository and the `main` branch.
2. Create a Jenkins Pipeline job and select **Pipeline script from SCM**.
3. SCM: Git; Repository URL: your repository URL; Branch: `*/main`; Script Path: `Jenkinsfile`.
4. The pipeline assumes a Windows Jenkins agent with Python, Git, Docker Desktop and Docker CLI available to the Jenkins service account.
5. It uses `bat` commands. A Linux Jenkins agent needs equivalent `sh` commands.
6. The pipeline uses host port 5001 and removes the test container after the run.

## Important
Do not mark a tool as PASS until you have run it and captured output on your own machine. Evidently's datasets are synthetic and deliberately shifted; this demonstrates the tool, not a real production drift event.
