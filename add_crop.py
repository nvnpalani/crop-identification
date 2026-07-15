import os
import sys

def create_crop_structure(crop_name):
    crop_name = crop_name.lower().strip()
    
    # Base directories
    base_dirs = ["crop_datasets", "user_uploads"]
    
    # Subdirectories to create
    sub_dirs = [
        "fruit_disease",
        "leaf_disease",
        f"{crop_name}_types"
    ]
    
    print(f"Initializing folder structure for crop: '{crop_name.capitalize()}'...\n")
    
    created_count = 0
    for base in base_dirs:
        for sub in sub_dirs:
            target_path = os.path.join(base, crop_name, sub)
            if not os.path.exists(target_path):
                os.makedirs(target_path)
                print(f"[+] Created: {target_path}")
                created_count += 1
            else:
                print(f"[-] Already exists: {target_path}")
                
    if created_count > 0:
        print(f"\n[SUCCESS] Successfully initialized {created_count} new folders for '{crop_name.capitalize()}'!")
    else:
        print(f"\n[INFO] Folders for '{crop_name.capitalize()}' already exist.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python add_crop.py <crop_name>")
        print("Example: python add_crop.py tomato")
        sys.exit(1)
        
    crop_input = sys.argv[1]
    create_crop_structure(crop_input)
