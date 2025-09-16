# COBOL + JCL + Python

This package demonstrates how to compile, link, and run a simple COBOL program on z/OS,
and how to automate job submission from Python.

## Contents

- `HELLO.cbl` : COBOL "Hello World" program
- `HELLOCLG.jcl` : JCL to compile, link, and run the COBOL program
- `submit_ftp.py` : Python script to submit JCL via FTP to JES
- `submit_zosmf.py` : Python script to submit JCL via z/OSMF REST API (with SYSOUT fetcher)
- `samples/` : folder containing 10 additional JCL workflow automation examples
- `README.md` : this documentation

## Instructions

### Step 1: Upload COBOL Source
Save `HELLO.cbl` into a COBOL source library, for example: `USER.SOURCE(HELLO)`.

### Step 2: Upload and Edit JCL
- Place `HELLOCLG.jcl` in your JCL library (e.g., `USER.JCL(HELLOCLG)`).
- Update dataset names (`USER.SOURCE`, `USER.LOAD`) and compiler library (`IGYV6R3.SIGYCOMP`) 
  to match your site's standards.

### Step 3: Submit JCL

You can run the job by submitting `HELLOCLG.jcl` directly from TSO/ISPF with the SUB command.

Or automate with Python:

#### Option A: FTP to JES
Update `submit_ftp.py` with your mainframe hostname, user ID, and password, then run:
```bash
python3 submit_ftp.py
```

#### Option B: z/OSMF REST API (Recommended)
Update `submit_zosmf.py` with your mainframe hostname, user ID, and password, then run:
```bash
python3 submit_zosmf.py
```

This script will:
1. Submit the JCL to JES.
2. Poll until the job finishes.
3. Fetch all SYSOUT DDs.
4. Print SYSOUT content directly in your Python console.

### Step 4: Check Output
- The COBOL program writes `HELLO, WORLD FROM COBOL ON Z/OS` to SYSOUT.
- With `submit_zosmf.py`, this message will automatically appear in your Python console.
- You can also manually view SYSOUT via SDSF or JES spool.

---

⚠️ **Notes:**
- You must have access to COBOL compiler libraries and appropriate dataset permissions.
- Replace placeholders (`mainframe.host`, `YOURID`, `YOURPASS`) with real values.
- Ensure your mainframe has **z/OSMF enabled** if you use the REST API method.
