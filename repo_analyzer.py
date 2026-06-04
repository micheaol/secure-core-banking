import sys
import requests

class GitHubRepoAnalyzer:
    def __init__(self, target_org):
        self.target_org = target_org
        self.base_url = f"https://api.github.com/orgs/{target_org}/repos"
    
    def fetch_repositories(self):
        """Queries the public GitHub API securely."""
        print(f"[+] Querying GitHub API for organization: {self.target_org}...")
        try:
            headers = {
                "User-Agent": "AppSec-CLI-Scanner-v1",
                "Accept": "application/vnd.github+json"
            }
            
            response = requests.get(self.base_url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.HTTPError as http_err:
            print(f"[!] HTTP Error occurred: {http_err}")
            sys.exit(1)
        except requests.exceptions.JSONDecodeError:
            print("[!] Critical Error: Received invalid JSON payload from the server.")
            sys.exit(1)
        except requests.exceptions.RequestException as err:
            print(f"[!] Network Error occurred: {err}")
            sys.exit(1)

    def generate_report(self, repo_data):
        """Parses the JSON data payload and extracts key metadata properties."""
        if not repo_data or not isinstance(repo_data, list):
            print("[-] No repositories found or empty payload returned.")
            return

        print("\n=============================================")
        print(f" SECURITY RECON REPORT FOR: {self.target_org}")
        print("=============================================")
        
        for repo in repo_data:
            if not isinstance(repo, dict):
                continue
                
            name = repo.get("name", "Unknown")
            stars = repo.get("stargazers_count", 0)
            is_private = repo.get("private", False)
            license_info = repo.get("license")
            
            license_name = "No License Found"
            if isinstance(license_info, dict):
                license_name = license_info.get("name", "No License Found")
            
            print(f"\n[Repository]: {name}")
            print(f" ├─ Public/Private Status: {'Private (Alert!)' if is_private else 'Public'}")
            print(f" ├─ Popularity Metrics: {stars} Stars")
            print(f" └─ Compliance Check: {license_name}")

def main():
    if len(sys.argv) != 2:
        print("[-] Usage Error: Please provide an organization name.")
        print("[-] Example: python repo_analyzer.py hackthebox")
        sys.exit(1)
        
    # CORRECT STRING HANDLING: Pulls down only the string argument from terminal
    target = sys.argv[1]
    analyzer = GitHubRepoAnalyzer(target)
    data = analyzer.fetch_repositories()
    analyzer.generate_report(data)

if __name__ == "__main__":
    main()
