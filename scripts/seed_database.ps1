# Database Seeding Utility for FindYourSky
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  FindYourSky DGCA Database Seeder        " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

Set-Location -Path "$PSScriptRoot\..\backend"
Write-Host "Initializing schema and seeding 18 DGCA FTO records..." -ForegroundColor Yellow
& ".\venv\Scripts\python.exe" -m app.db.init_db
if ($LASTEXITCODE -eq 0) {
    Write-Host "Database successfully seeded at backend/skymatch.db!" -ForegroundColor Green
} else {
    Write-Host "Error seeding database!" -ForegroundColor Red
}
Set-Location -Path "$PSScriptRoot\.."
