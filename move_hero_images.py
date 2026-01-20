import shutil
import os

source_dir = r"C:\Users\SUBARNA MONDAL\.gemini\antigravity\brain\a19e22db-0d89-464e-bcbc-7d76e8b2d46d"
dest_dir = r"c:\Users\SUBARNA MONDAL\Desktop\my-projects\gigma\assets\images"

files = {
    "hero_gaming_1_1767941490448.png": "hero-slide-1.png",
    "hero_gaming_2_1767941506805.png": "hero-slide-2.png",
    "hero_gaming_3_1767941537677.png": "hero-slide-3.png",
    "hero_gaming_4_1767941575339.png": "hero-slide-4.png",
    "hero_gaming_5_1767941593112.png": "hero-slide-5.png",
    "hero_gaming_6_1767941609186.png": "hero-slide-6.png"
}

for src_name, dest_name in files.items():
    src_path = os.path.join(source_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    
    if os.path.exists(src_path):
        try:
            shutil.copy2(src_path, dest_path)
            print(f"Copied {src_name} to {dest_name}")
        except Exception as e:
            print(f"Error copying {src_name}: {e}")
    else:
        print(f"Source file not found: {src_path}")
