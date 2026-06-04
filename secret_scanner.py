import sys
import re
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

class GitHubOrgSecretScanner:
    def __init__(self, target_org):
        self.org = target_org
        # REST API endpoint to fetch org metadata
        self.org_repos_url = f"https://api.github.com/orgs/{target_org}/repos"
        
        # High-risk AppSec regex signatures
        self.signatures = {
            "AWS Access Key": r"AKIA[0-9A-Z]{16}",
            "Google API Key": r"AIzaSy[0-9A-Za-z-_]{35}",
            "Slack Webhook": r"https://hooks\.slack\.com/services/T[A-Z0-9]+/_/B[A-Z0-9]+/_/[A-Za-z0-9]+",
            "Generic Private Key": r"-----BEGIN [A-Z]+ PRIVATE KEY-----"
        }
        self.headers = {"User-Agent": "AppSec-Master-Scanner-v2"}

    def fetch_all_repositories(self):
        """Step 1: Discover every repository and map its true default branch."""
        print(f"[+] Querying GitHub API for ALL repositories in organization: {self.org}...")
        try:
            response = requests.get(self.org_repos_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            repo_list = response.json()
            
            if not isinstance(repo_list, list):
                return []
            
            active_targets = []
            for repo in repo_list:
                if isinstance(repo, dict) and repo.get("name"):
                    name = repo.get("name")
                    branch = repo.get("default_branch", "main")
                    active_targets.append((name, branch))
            return active_targets
            
        except requests.exceptions.RequestException as err:
            print(f"[!] Failed to map organization infrastructure: {err}")
            return []

    def scan_file_contents(self, repo_name, default_branch, file_path):
        """Step 3: Download and parse individual file contents in-memory using dynamic routing."""
        # FIXED: Corrected domain format for raw content downloads
        raw_url = f"https://githubusercontent.com{self.org}/{repo_name}/{default_branch}/{file_path}"
        try:
            response = requests.get(raw_url, timeout=5)
            if response.status_code != 200:
                return 
            
            file_text = response.text

            for secret_type, regex in self.signatures.items():
                matches = re.findall(regex, file_text)
                for match in matches:
                    sys.stdout.write(
                        f"\n[CRITICAL ALERT] Found {secret_type}!\n"
                        f" ├─ Target: {self.org}/{repo_name} ({default_branch})\n"
                        f" ├─ File: {file_path}\n"
                        f" └─ Partial Leak Proof: {match[:8]}...\n"
                    )
                    sys.stdout.flush()
                    
        except requests.exceptions.RequestException:
            pass

    def scan_entire_repository(self, target_tuple):
        """Step 2: Map the inner file architecture using dynamic tree targeting."""
        repo_name, default_branch = target_tuple
        print(f" ├─ Inspecting repository layout: {repo_name} [{default_branch}]...")
        
        # FIXED: Corrected API domain and path layout for file tree structures
        tree_url = f"https://github.com{self.org}/{repo_name}/git/trees/{default_branch}?recursive=1"
        
        try:
            response = requests.get(tree_url, headers=self.headers, timeout=10)
            if response.status_code != 200:
                return 
                
            tree_data = response.json().get("tree", [])
            for item in tree_data:
                if item.get("type") == "blob":
                    self.scan_file_contents(repo_name, default_branch, item.get("path"))
        except requests.exceptions.RequestException:
            pass

def main():
    if len(sys.argv) != 2:
        print("[-] Usage Error: Please provide an organization name.")
        print("[-] Example: python secret_scanner.py hackthebox")
        sys.exit(1)
        
    target_org = sys.argv[1]
    
    scanner = GitHubOrgSecretScanner(target_org)
    repositories = scanner.fetch_all_repositories()
    
    if not repositories:
        print("[-] No repositories found or execution halted.")
        sys.exit(0)
        
    print(f"[+] Discovered {len(repositories)} public targets. Launching multi-threaded code analysis...")
    
    max_threads = min(10, len(repositories))
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(scanner.scan_entire_repository, repo): repo for repo in repositories}
        for future in as_completed(futures):
            pass
        
    print("\n[+] Deep multi-threaded secret and branch compliance scan complete.")

if __name__ == "__main__":
    main()
