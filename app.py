from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/slicing/api/run")
async def run_slicer():
    try:
        # Run PrusaSlicer command
        result = subprocess.run(['prusa-slicer', '--help'], 
                              capture_output=True,
                              text=True,
                              check=True)
        
        return {
            "status": "success",
            "output": result.stdout,
            "message": "PrusaSlicer command executed successfully"
        }
        
    except subprocess.CalledProcessError as e:
        return {
            "status": "error", 
            "error": str(e),
            "message": "Failed to execute PrusaSlicer command"
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "message": "An unexpected error occurred"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

