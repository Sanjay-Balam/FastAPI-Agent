from fastapi import APIRouter, UploadFile, File
import pandas as pd
import io

router = APIRouter()

@router.post("/uploadcsv/")
async def upload_csv(file: UploadFile = File(...)):
    # Reading the CSV file content
    content = await file.read()

    # Use io.StringIO to create a file-like object for Pandas
    df = pd.read_csv(io.StringIO(content.decode("utf-8")))

    # Convert the DataFrame to JSON format
    json_data = df.to_json(orient="records")

    return {"filename": file.filename, "data": json_data}
