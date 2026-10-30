# Launch FindYourSky Backend and Frontend locally
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Starting FindYourSky Application Stack  " -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

# 1. Start FastAPI Backend
Write-Host "Launching FastAPI backend on http://127.0.0.1:8000..." -ForegroundColor Yellow
$backendProcess = Start-Process -FilePath "powershell" -ArgumentList "-NoExit", "-Command", "cd backend; .\venv\Scripts\uvicorn.exe app.main:app --host 127.0.0.1 --port 8000 --reload" -PassThru

# Wait 2 seconds for backend to start
Start-Sleep -Seconds 2

# 2. Start Vite Frontend
Write-Host "Launching Vite React frontend on http://localhost:5173..." -ForegroundColor Yellow
$frontendProcess = Start-Process -FilePath "powershell" -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev" -PassThru

Write-Host "`nStack is booting up!" -ForegroundColor Green
Write-Host "API Swagger Docs: http://127.0.0.1:8000/docs" -ForegroundColor Cyan
Write-Host "Frontend Portal:  http://localhost:5173" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
