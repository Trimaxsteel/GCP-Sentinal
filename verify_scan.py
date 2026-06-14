from google.cloud import bigquery
from google.api_core import exceptions

def run_real_audit(target_id):
    print(f"\n[SCANNING] Target: {target_id}")
    client = bigquery.Client()
    
    try:
        # STEP 1: Fetch the datasets (This is the 'Discovery' phase)
        datasets = list(client.list_datasets(project=target_id, max_results=3))
        print(f"--- SUCCESS: Found {len(datasets)} datasets in {target_id} ---")
        
        for ds in datasets:
            print(f"[!] Metadata Leak: Dataset '{ds.dataset_id}' is publicly listable.")
            
            # STEP 2: Deep dive into the first dataset's ACL (Access Control List)
            dataset_ref = client.get_dataset(f"{target_id}.{ds.dataset_id}")
            for entry in dataset_ref.access_entries:
                if entry.entity_id in ['allUsers', 'allAuthenticatedUsers']:
                    print(f"[CRITICAL] IAM Exposure: '{entry.entity_id}' has '{entry.role}' role on this dataset!")

    except exceptions.Forbidden:
        print(f"--- ACCESS DENIED: {target_id} is properly shielded. ---")
    except Exception as e:
        print(f"--- ERROR: {str(e)} ---")

if __name__ == "__main__":
    # Test 1: Your project (Should likely be 'Denied' or 'Empty')
    run_real_audit("tranquil-well-478609-e9")
    
    # Test 2: The LIVE Public Target (This is the one that proves the scanner works)
    run_real_audit("bigquery-public-data")