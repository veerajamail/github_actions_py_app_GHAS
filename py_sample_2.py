import sys

def main():
    # Ensure there are enough arguments
    if len(sys.argv) < 4:
        print("Usage: python sample_script.py <region> <combine_file> <upload_to_gateway>")
        sys.exit(1)

    # Extract arguments
    region = sys.argv[1]  # First argument: Region
    combine_file = sys.argv[2]  # Second argument: Combine File
    upload_to_gateway = sys.argv[3]  # Third argument: Upload to Gateway

    # Display the arguments
    print(f"Region: {region}")
    print(f"Combine File: {combine_file}")
    print(f"Upload to Gateway: {upload_to_gateway}")

    # Add some dummy logic for testing
    print("Processing with the provided arguments...")
    print("Script execution completed successfully.")

if __name__ == "__main__":
    main()
