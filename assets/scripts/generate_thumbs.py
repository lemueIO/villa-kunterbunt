import os
from PIL import Image
import glob

def create_thumbnail(image_path, size=(400, 400)):
    try:
        base, ext = os.path.splitext(image_path)
        thumb_path = f"{base}_thumb{ext}"
        
        # Check if thumb already exists (optional, but good for idempotency)
        # if os.path.exists(thumb_path):
        #     return thumb_path

        with Image.open(image_path) as img:
            # Convert to RGB if necessary (e.g. for PNGs with transparency if saving as JPG, 
            # but we are saving as PNG so it should be fine, actually PNG is safer for screenshots/illustrations)
            
            # Calculate aspect ratio to fit into size without distortion
            img.thumbnail(size)
            img.save(thumb_path)
            print(f"Created thumbnail: {thumb_path}")
            return thumb_path
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def main():
    target_dir = "/home/elliot/git_repos/villa-kunterbunt/assets/illustrations"
    # Pattern: Die Villa Kunterbunt_0*.PNG
    pattern = os.path.join(target_dir, "Die Villa Kunterbunt_0*.PNG")
    
    files = glob.glob(pattern)
    print(f"Found {len(files)} files matching pattern.")
    
    for file_path in files:
        # Avoid processing existing thumbnails
        if "_thumb" in file_path:
            continue
            
        create_thumbnail(file_path)

if __name__ == "__main__":
    main()
