import requests
import time

zosmf_url = "https://mainframe:443/zosmf/restjobs/jobs"
auth = ("YOURID", "YOURPASS")
headers = {"Content-Type": "text/plain"}

# Load JCL from file
with open("HELLOCLG.jcl") as f:
    jcl_data = f.read()

# Submit job
resp = requests.post(zosmf_url, auth=auth, headers=headers, data=jcl_data, verify=False)
jobinfo = resp.json()
jobname = jobinfo.get("jobname")
jobid = jobinfo.get("jobid")
print(f"Submitted job {jobname} ({jobid})")

# Poll job status until it completes
status_url = f"{zosmf_url}/{jobname}/{jobid}"
while True:
    r = requests.get(status_url, auth=auth, verify=False)
    status = r.json()
    print("Status:", status.get("status"))
    if status.get("status") in ["OUTPUT", "ABEND", "CC"]:
        break
    time.sleep(3)

# Fetch SYSOUT files list
out_url = f"{status_url}/files"
resp = requests.get(out_url, auth=auth, verify=False)
files = resp.json()

# Download and print SYSOUT content
for fdesc in files:
    ddname = fdesc.get("ddname")
    fileid = fdesc.get("id")
    content_url = f"{status_url}/files/{fileid}/content"
    resp = requests.get(content_url, auth=auth, verify=False)
    print(f"--- SYSOUT DD: {ddname} ---")
    print(resp.text)
