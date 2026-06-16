import os
import urllib.request
import urllib.error
import json
import time
import re

def download_dataset():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Please set GITHUB_TOKEN")
        return
        
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "python-urllib"
    }

    input_file = "/Users/titan/.gemini/antigravity/scratch/agents_md_analysis/top_100_agents_md.txt"
    output_dir = "/Users/titan/Code/ai-tooling/dataset/agents-benchmark/"
    os.makedirs(output_dir, exist_ok=True)
    
    repos = []
    try:
        with open(input_file, "r") as f:
            for line in f:
                # Match: "1. OWNER/REPO - 1234 stars"
                match = re.match(r'^\d+\.\s+([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\s+-', line)
                if match:
                    repos.append(match.group(1))
    except FileNotFoundError:
        print(f"Could not find {input_file}")
        return

    print(f"Found {len(repos)} repositories to download.")
    
    for i, repo in enumerate(repos, 1):
        # GitHub API to get the file (handles default branch automatically)
        api_url = f"https://api.github.com/repos/{repo}/contents/AGENTS.md"
        req = urllib.request.Request(api_url, headers=headers)
        
        try:
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    download_url = data.get("download_url")
                    
                    if download_url:
                        # Download the raw content
                        dl_req = urllib.request.Request(download_url)
                        with urllib.request.urlopen(dl_req) as dl_res:
                            content = dl_res.read().decode('utf-8')
                            
                        # Save the file safely
                        safe_name = repo.replace("/", "_") + ".md"
                        file_path = os.path.join(output_dir, safe_name)
                        with open(file_path, "w") as out_f:
                            out_f.write(content)
                        print(f"[{i}/{len(repos)}] Downloaded {repo}")
                    else:
                        print(f"[{i}/{len(repos)}] No download URL for {repo}")
        except urllib.error.HTTPError as e:
            print(f"[{i}/{len(repos)}] Error fetching {repo}: HTTP {e.code}")
            if e.code == 403: # Rate limit
                print("Sleeping for 60s due to rate limit...")
                time.sleep(60)
        except Exception as e:
            print(f"[{i}/{len(repos)}] Failed to download {repo}: {e}")
            
        time.sleep(0.5) # small delay to prevent abuse
        
if __name__ == "__main__":
    download_dataset()
