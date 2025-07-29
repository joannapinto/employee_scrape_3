import os

print("Starting full pipeline...")

# Run ingestion
print("\nRunning ingestion:")
os.system("python ingestion/main.py")

# Run processing
print("\nRunning processing:")
os.system("python processing/main.py")

print("\nPipeline completed successfully.")
