# import os
# import requests
# import zipfile
# from duckduckgo_search import DDGS


# # List of Indian states and union territories
# states_ut = [
#     "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
#     "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
#     "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
#     "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", 
#     "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
#     "Uttarakhand", "West Bengal",
#     "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
#     "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
# ]

# # Create dataset folder
# dataset_dir = "Cultural_Dataset"
# os.makedirs(dataset_dir, exist_ok=True)

# def download_images(query, folder, max_images=3):
#     results = DDGS(query, max_results=max_images)
#     if not results:
#         print(f"No results for {query}")
#         return
#     for i, result in enumerate(results):
#         try:
#             img_data = requests.get(result["image"], timeout=10).content
#             file_path = os.path.join(folder, f"{query}_{i+1}.jpg")
#             with open(file_path, "wb") as f:
#                 f.write(img_data)
#         except Exception as e:
#             print(f"Error downloading {query} image {i+1}: {e}")

# # Download images for each state
# for state in states_ut:
#     state_folder = os.path.join(dataset_dir, state.replace(" ", "_"))
#     os.makedirs(state_folder, exist_ok=True)
#     query = f"{state} culture festival monument traditional attire"
#     download_images(query, state_folder, max_images=5)
#     print(f"Downloaded images for {state}")

# # Zip the dataset
# zip_filename = "Cultural_Dataset.zip"
# with zipfile.ZipFile(zip_filename, 'w') as zipf:
#     for root, dirs, files in os.walk(dataset_dir):
#         for file in files:
#             file_path = os.path.join(root, file)
#             zipf.write(file_path, os.path.relpath(file_path, dataset_dir))

# print(f"\n✅ Dataset created and zipped as {zip_filename}")
# import os
# import requests
# import zipfile
# from duckduckgo_search import DDGS
# from tqdm import tqdm   # progress bar

# # List of Indian states and union territories
# states_ut = [
#     "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
#     "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
#     "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
#     "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", 
#     "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
#     "Uttarakhand", "West Bengal",
#     "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
#     "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
# ]

# # Create dataset folder
# dataset_dir = "Cultural_Dataset"
# os.makedirs(dataset_dir, exist_ok=True)

# def download_images(query, folder, max_images=3):
#     with DDGS() as ddgs:
#         results = ddgs.images(query, max_results=max_images)
#         for i, result in enumerate(results):
#             try:
#                 img_url = result["image"]
#                 img_data = requests.get(img_url, timeout=10).content
#                 file_path = os.path.join(folder, f"{query.replace(' ', '_')}_{i+1}.jpg")
#                 with open(file_path, "wb") as f:
#                     f.write(img_data)
#             except Exception as e:
#                 print(f"❌ Error downloading {query} image {i+1}: {e}")

# # Download images for each state with progress bar
# for state in tqdm(states_ut, desc="Downloading cultural images"):
#     state_folder = os.path.join(dataset_dir, state.replace(" ", "_"))
#     os.makedirs(state_folder, exist_ok=True)
#     query = f"{state} culture festival monument traditional attire"
#     download_images(query, state_folder, max_images=5)

# # Zip the dataset
# zip_filename = "Cultural_Dataset.zip"
# with zipfile.ZipFile(zip_filename, 'w') as zipf:
#     for root, dirs, files in os.walk(dataset_dir):
#         for file in files:
#             file_path = os.path.join(root, file)
#             zipf.write(file_path, os.path.relpath(file_path, dataset_dir))

# print(f"\n✅ Dataset created and zipped as {zip_filename}")
import os
import requests
import zipfile
import time
from ddgs import DDGS   # ✅ use new package (pip install ddgs)
from tqdm import tqdm   # progress bar

# List of Indian states and union territories
states_ut = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", 
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", 
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Delhi", "Jammu and Kashmir", "Ladakh", "Lakshadweep", "Puducherry"
]

# Create dataset folder
dataset_dir = "Cultural_Dataset"
os.makedirs(dataset_dir, exist_ok=True)

def download_images(query, folder, max_images=3):
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=max_images)
        for i, result in enumerate(results):
            img_url = result.get("image")
            if not img_url:
                continue
            retries = 3
            for attempt in range(retries):
                try:
                    response = requests.get(img_url, timeout=10)
                    if response.status_code == 200:
                        file_path = os.path.join(folder, f"{query.replace(' ', '_')}_{i+1}.jpg")
                        with open(file_path, "wb") as f:
                            f.write(response.content)
                        break  # ✅ success, stop retrying
                except Exception as e:
                    if attempt == retries - 1:
                        print(f"❌ Failed to download {query} image {i+1}: {e}")
                time.sleep(2)  # ⏳ wait to avoid rate limit

# Download images for each state with progress bar
for state in tqdm(states_ut, desc="Downloading cultural images"):
    state_folder = os.path.join(dataset_dir, state.replace(" ", "_"))
    os.makedirs(state_folder, exist_ok=True)
    query = f"{state} culture festival monument traditional attire"
    download_images(query, state_folder, max_images=5)

# Zip the dataset
zip_filename = "Cultural_Dataset.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, dataset_dir))

print(f"\n✅ Dataset created and zipped as {zip_filename}")
