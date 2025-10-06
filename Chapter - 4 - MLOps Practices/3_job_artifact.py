import oci
import argparse
import os
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--greeting", help="Custom greeting message", default="Hello")
    args = parser.parse_args()

    name = os.getenv("NAME", "Unknown User")

    print(f"Job started at: {datetime.now()}")
    print(f"{args.greeting}, {name}!")

    # Detect if running locally or within OCI Job
    try:
        signer = oci.auth.signers.get_resource_principals_signer()
        print("Running inside OCI Data Science environment using Resource Principal authentication.")
    except Exception:
        print("Running locally without Resource Principal authentication.")
        signer = None

    # Example OCI SDK usage (e.g., fetching user info)
    if signer:
        identity_client = oci.identity.IdentityClient(config={}, signer=signer)
        user = identity_client.get_user(signer.tenancy_id).data
        print(f"Authenticated OCI user: {user.name}")

    print("Job is finished.")

if __name__ == "__main__":
    main()
