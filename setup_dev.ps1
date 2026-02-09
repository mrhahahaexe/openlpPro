# OpenLP Development Setup Script

Write-Host "Setting up OpenLP Development Environment..." -ForegroundColor Cyan

# 1. Check Python
$pythonVersion = python --version
if ($?) {
    Write-Host "Python found: $pythonVersion" -ForegroundColor Green
} else {
    Write-Host "Error: Python not found!" -ForegroundColor Red
    exit 1
}

# 2. Install Build Tools
Write-Host "Installing build tools (hatch)..." -ForegroundColor Yellow
pip install hatch
if (-not $?) {
    Write-Host "Failed to install hatch. Please check your python environment." -ForegroundColor Red
    exit 1
}

# 3. Install Python Dependencies
Write-Host "Installing OpenLP in editable mode..." -ForegroundColor Yellow
# Try installing in editable mode
pip install -e .[test,mysql,postgresql]
if (-not $?) {
    Write-Host "Editable install failed. Trying standard install..." -ForegroundColor Red
    # Fallback to standard install
    pip install .
}

# 4. Install JavaScript Dependencies
Write-Host "Checking JavaScript dependencies..." -ForegroundColor Yellow
if (Test-Path "package.json") {
    if (Test-Path "node_modules") {
        Write-Host "Cleaning existing node_modules..."
        Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
    }
    
    if (Get-Command "yarn" -ErrorAction SilentlyContinue) {
        Write-Host "Installing with yarn..."
        yarn install
    } elseif (Get-Command "npm" -ErrorAction SilentlyContinue) {
        Write-Host "yarn not found. Installing with npm..."
        npm install
    } else {
        Write-Host "Error: Neither yarn nor npm found!" -ForegroundColor Red
    }
}

Write-Host "Setup complete! Try running: python run_openlp.py" -ForegroundColor Green
