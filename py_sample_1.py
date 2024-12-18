import argparse

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Sample Python script for testing GitHub Actions workflow.")

    # Define arguments
    parser.add_argument('--region', type=str, help="The region to process (e.g., INT, PVS)", required=True)
    parser.add_argument('--combine_file', type=str, help="Combine files option (Yes/No)", required=False, default="No")
    parser.add_argument('--upload_to_gateway', type=str, help="Upload to gateway option (Yes/No)", required=False, default="No")
    parser.add_argument('--custom_arg', type=str, help="Custom argument to pass", required=False)

    # Parse the arguments
    args = parser.parse_args()

    # Display the parsed arguments
    print(f"Region: {args.region}")
    print(f"Combine File: {args.combine_file}")
    print(f"Upload to Gateway: {args.upload_to_gateway}")
    if args.custom_arg:
        print(f"Custom Argument: {args.custom_arg}")

    # Add some dummy logic for testing
    print("Processing with the provided arguments...")
    print("Script execution completed successfully.")

if __name__ == "__main__":
    main()
