# Setup Instructions

Complete setup guide for the Crisp Prompt Workshop. Follow the section for your operating system (**macOS** or **Windows**), then verify your installation with the [Verification Checklist](#-verification-checklist).

---

## 📋 What You'll Install

| Tool | Purpose |
|------|---------|
| **Node.js** (v18+) | Runs `npm` / `npx` — required for Claude Code |
| **Python** (v3.10+) | Runs the Flask workshop app |
| **Git** | Cloning the repository |
| **Claude Code** | AI pair-programming CLI used in exercises |

---

## 🍎 macOS

### Step 1: Install Homebrew (Package Manager)

Homebrew installs everything else below. Open **Terminal** (⌘ + Space, type `Terminal`) and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

> [!IMPORTANT]
> After the installer finishes, it prints two commands to add Homebrew to your shell. **Copy and run them** — they look like:
>
> ```bash
> echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
> eval "$(/opt/homebrew/bin/brew shellenv)"
> ```

Verify Homebrew:

```bash
brew --version
```

### Step 2: Install Node.js

```bash
brew install node
```

> [!TIP]
> For managing multiple Node versions (optional), consider `brew install nvm` instead. The direct install above is fine for this workshop.

### Step 3: Install Python

```bash
brew install python
```

This installs `python3` and `pip3`. macOS ships with an older system Python — always use `python3` explicitly.

### Step 4: Install Git

```bash
brew install git
```

Alternatively, Git may already be present via Apple's Command Line Tools. Check with `git --version` — if it prompts to install the tools, accepting also works.

### Step 5: Install Claude Code

Claude Code is distributed via npm. Install it globally:

```bash
npm install -g @anthropic-ai/claude-code
```

Verify Calude Code Starts by typing:

```bash
claude
```

> [!NOTE]
> If `npm install -g` fails with a permissions error, either:
>
> ```bash
> sudo npm install -g @anthropic-ai/claude-code
> ```
>
> — or (preferred) fix npm's global prefix, see [npm docs on resolving permission errors](https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally).

---

## 🪟 Windows

Choose **one** package manager below — **Winget** (recommended, built into Windows 10/11) or **Chocolatey**. Or use the direct installers linked in each step.

### Option A: Winget (Recommended)

Winget is preinstalled on Windows 10 (1809+) and Windows 11. Open **PowerShell** or **Terminal** and confirm:

```powershell
winget --version
```

If missing, install it from the [Microsoft Store](https://apps.microsoft.com/detail/9NBLGGH4NNS1) (search "App Installer").

### Option B: Chocolatey

Open **PowerShell as Administrator** (right-click → Run as administrator) and run:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Verify:

```powershell
choco --version
```

### Step 1: Install Node.js

**Winget:**

```powershell
winget install OpenJS.NodeJS.LTS
```

**Chocolatey:**

```powershell
choco install nodejs-lts -y
```

**Direct installer:** Download the LTS `.msi` from [nodejs.org](https://nodejs.org/) and run it. Keep all default options (they include `npm` and add Node to PATH).

> [!IMPORTANT]
> **Close and reopen your terminal** after installing so the updated PATH is picked up.

### Step 2: Install Python (with PATH)

**Winget:**

```powershell
winget install Python.Python.3.12
```

**Chocolatey:**

```powershell
choco install python -y
```

**Direct installer:** Download from [python.org](https://www.python.org/downloads/windows/).

> [!IMPORTANT]
> In the Python installer, **check the box "Add python.exe to PATH"** on the first screen **before** clicking "Install Now". If you skipped it:
>
> 1. Re-run the installer
> 2. Choose **Modify**
> 3. On "Optional Features", tick **Add Python to environment variables**

### Step 3: Install Git

**Winget:**

```powershell
winget install Git.Git
```

**Chocolatey:**

```powershell
choco install git -y
```

**Direct installer:** Download from [git-scm.com](https://git-scm.com/download/win). Defaults are fine; the installer adds Git to PATH automatically.

> [!TIP]
> After installing Git for Windows, use **Git Bash** (installed alongside) for the most Unix-like experience with the workshop commands.

### Step 4: Install Claude Code

Open a **new** PowerShell or Terminal window and install globally via npm:

```powershell
npm install -g @anthropic-ai/claude-code
```

Then start it inside your project directory:

```powershell
cd crisp-prompt-workshop
claude
```

> [!NOTE]
> Claude Code on Windows runs natively, or under **WSL** (Ubuntu) if you prefer a Linux-style workflow. For WSL: install Ubuntu from the Microsoft Store, then follow the [macOS steps](#-macos) inside WSL (Homebrew works there too, or use `apt`).

---

## ✅ Verification Checklist

Open a **new terminal** (macOS: Terminal / Windows: PowerShell) and run each command. All four should return a version number — no "command not found" errors.

- [ ] **Node.js**

  ```bash
  node -v
  ```

  Expected: `v18.x` or higher

- [ ] **npm**

  ```bash
  npm -v
  ```

- [ ] **Python**

  ```bash
  python3 --version   # macOS
  python --version    # Windows (or py --version)
  ```

  Expected: `Python 3.10` or higher

- [ ] **pip**

  ```bash
  pip3 --version      # macOS
  pip --version       # Windows
  ```

- [ ] **Git**

  ```bash
  git --version
  ```

- [ ] **Claude Code**

  ```bash
  claude --version
  ```

### First-Run Smoke Test

From the repository root, install the workshop dependencies and confirm the Flask app imports:

```bash
pip install -r requirements.txt
python -c "import app; print('Flask app OK')"
```

If every check passes, you're ready — run `claude` in the project directory and start the workshop. 🎉
