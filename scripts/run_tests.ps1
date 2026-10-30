# Automated Test Runner for FindYourSky
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Running FindYourSky Quality Test Suite  " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Backend Pytest
Write-Host "`n[1/2] Executing Backend Pytest Suite..." -ForegroundColor Yellow
Set-Location -Path "$PSScriptRoot\..\backend"
& ".\venv\Scripts\pytest.exe" -o pythonpath=. -v
$backendExit = $LASTEXITCODE

# 2. Frontend Typecheck and Build
Write-Host "`n[2/2] Validating Frontend TypeScript & Production Build..." -ForegroundColor Yellow
Set-Location -Path "$PSScriptRoot\..\frontend"
npm run build
$frontendExit = $LASTEXITCODE

Set-Location -Path "$PSScriptRoot\.."

Write-Host "`n==========================================" -ForegroundColor Cyan
if ($backendExit -eq 0 -and $frontendExit -eq 0) {
    Write-Host "  ALL TESTS AND BUILDS PASSED! (READY)   " -ForegroundColor Green
    Write-Host "==========================================" -ForegroundColor Cyan
    exit 0
} else {
    Write-Host "  TEST OR BUILD FAILURE DETECTED!        " -ForegroundColor Red
    Write-Host "==========================================" -ForegroundColor Cyan
    exit 1
}
