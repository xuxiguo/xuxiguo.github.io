#!/usr/bin/env python3
"""
Upload all blockchain case presentation videos to YouTube as Unlisted,
then patch _data/content.yml with the embed URLs automatically.

────────────────────────────────────────────────────
SETUP (one-time, ~5 minutes)
────────────────────────────────────────────────────
1. Install dependencies:
       pip install google-api-python-client google-auth-oauthlib

2. Create a Google Cloud project & enable the YouTube Data API v3:
   a. Go to https://console.cloud.google.com/
   b. Create a new project (e.g. "YouTube Uploader")
   c. APIs & Services → Enable APIs → search "YouTube Data API v3" → Enable

3. Create OAuth 2.0 credentials:
   a. APIs & Services → Credentials → Create Credentials → OAuth client ID
   b. Application type: Desktop app  (name it anything)
   c. Click "Download JSON" → save as  client_secrets.json
      next to this script (same folder as this .py file)

4. Add your Google account as a test user (needed while app is in testing):
   a. APIs & Services → OAuth consent screen → Test users → + Add users
   b. Add the Gmail/Google account that owns your YouTube channel

5. Run:
       python upload_to_youtube.py

   A browser window will open for Google sign-in on the first run.
   After that, the token is cached in youtube_token.json (never commit it).

────────────────────────────────────────────────────
WHAT THIS SCRIPT DOES
────────────────────────────────────────────────────
• Uploads every video as Unlisted (hidden from search/channel, embeddable)
• Saves progress to youtube_results.json (re-run is safe — already-uploaded
  videos are skipped automatically)
• Patches _data/content.yml: replaces local `video:` paths with
  `videoEmbed:` YouTube URLs
• Optionally removes local .mp4 files from assets/cases/ to save Git space
"""

import json
import os
import random
import re
import sys
import time
from pathlib import Path

# ── Dependencies ──────────────────────────────────────────────────────────────
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload
except ImportError:
    sys.exit(
        "Missing dependencies. Run:\n"
        "  pip install google-api-python-client google-auth-oauthlib\n"
    )

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR   = Path(__file__).parent
REPO_ROOT    = SCRIPT_DIR          # script lives at repo root
CONTENT_YML  = REPO_ROOT / "_data" / "content.yml"
ASSETS_CASES = REPO_ROOT / "assets" / "cases"
SECRETS_FILE = SCRIPT_DIR / "client_secrets.json"
TOKEN_FILE   = SCRIPT_DIR / "youtube_token.json"
RESULTS_FILE = SCRIPT_DIR / "youtube_results.json"

SRC = Path(r"C:\Users\gxxno\Dropbox\Teaching\Previous Class\Blockchain Case Package")

# ── Video manifest ────────────────────────────────────────────────────────────
COURSE_TAG = "Final project · Introduction to Blockchain & Cryptocurrency · Saint Louis University"

VIDEOS = [
    # ── Spring 2025 ──────────────────────────────────────────────────────────
    {
        "key":  "2025-autoledger",
        "year": 2025,
        "slug": "autoledger",
        "file": SRC / "Spring 2025" / "AutoLedger" / "AutoLedger.mp4",
        "title": "AutoLedger – Blockchain Business Case | Spring 2025",
        "description": (
            "A trusted vehicle history, end-to-end on-chain.\n\n"
            "AutoLedger replaces fragmented vehicle-history reports with a single "
            "immutable record on Ethereum: every sale, service, accident, and odometer "
            "reading is signed by the responsible party and verifiable by buyers and lenders.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2025-bagblock",
        "year": 2025,
        "slug": "bagblock",
        "file": SRC / "Spring 2025" / "BagBlock" / "BagBlock.mp4",
        "title": "BagBlock – Blockchain Business Case | Spring 2025",
        "description": (
            "Lost-luggage insurance that pays itself.\n\n"
            "BagBlock turns airline baggage tags into smart contracts: passengers stake "
            "a small premium, airline scans feed real-time custody data on-chain, and if "
            "a bag goes missing the policy auto-pays without a single claim form.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2025-fanpass",
        "year": 2025,
        "slug": "fanpass",
        "file": SRC / "Spring 2025" / "FanPass" / "FanPass.mp4",
        "title": "FanPass – Blockchain Business Case | Spring 2025",
        "description": (
            "Memberships that travel with the fan, not the venue.\n\n"
            "A portable fan-loyalty NFT that survives across teams, seasons, and resale "
            "markets, giving sports franchises a richer view of their most engaged "
            "supporters and giving fans real ownership of their fandom.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2025-fundforge",
        "year": 2025,
        "slug": "fundforge",
        "file": SRC / "Spring 2025" / "FundForge" / "FundForge.mp4",
        "title": "FundForge – Blockchain Business Case | Spring 2025",
        "description": (
            "Decentralized venture funding for student innovators.\n\n"
            "A token-curated crowdfunding platform for university entrepreneurs: backers "
            "stake capital in milestone-gated smart contracts, founders unlock funds only "
            "as deliverables ship.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2025-ideafirst",
        "year": 2025,
        "slug": "ideafirst",
        "file": SRC / "Spring 2025" / "IdeaFirst" / "IdeaFirst.mp4",
        "title": "IdeaFirst – Blockchain Business Case | Spring 2025",
        "description": (
            "Stake an idea before someone else does.\n\n"
            "IdeaFirst lets innovators register a hash of an early-stage idea on Ethereum "
            "to establish priority, then progressively reveal details to vetted "
            "collaborators — a Web3 answer to provisional patents.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2025-splitchain",
        "year": 2025,
        "slug": "splitchain",
        "file": SRC / "Spring 2025" / "SplitChain" / "SplitChain.mp4",
        "title": "SplitChain – Blockchain Business Case | Spring 2025",
        "description": (
            "Group expenses, settled trustlessly.\n\n"
            "SplitChain is a Web3 take on Splitwise: friends and roommates log shared "
            "expenses to a smart contract that nets balances and settles in stablecoins, "
            "eliminating the awkward 'who owes whom' spreadsheet.\n\n"
            + COURSE_TAG
        ),
    },
    # ── Spring 2026 ──────────────────────────────────────────────────────────
    {
        "key":  "2026-collabproof",
        "year": 2026,
        "slug": "collabproof",
        "file": SRC / "Spring 2026" / "CollabProof" / "CollabProof.mp4",
        "title": "CollabProof – Blockchain Business Case | Spring 2026",
        "description": (
            "Tamper-proof attribution for creative collaboration.\n\n"
            "A decentralized registry that timestamps and signs contributions across "
            "creative teams, so writers, designers, and engineers can prove authorship, "
            "split royalties automatically, and resolve IP disputes without a middleman.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2026-creditchain",
        "year": 2026,
        "slug": "creditchain",
        "file": SRC / "Spring 2026" / "CreditChain" / "CreditChain.mp4",
        "title": "CreditChain – Blockchain Business Case | Spring 2026",
        "description": (
            "Portable credit identity for the underbanked.\n\n"
            "A decentralized credit-scoring layer that aggregates on- and off-chain "
            "financial signals into a self-sovereign credit identity, giving thin-file "
            "borrowers a fair shot at lending markets worldwide.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2026-datavault",
        "year": 2026,
        "slug": "datavault",
        "file": SRC / "Spring 2026" / "DataVault" / "DataVault.mp4",
        "title": "DataVault – Blockchain Business Case | Spring 2026",
        "description": (
            "User-owned data, monetized on your terms.\n\n"
            "A consent-based data marketplace where individuals encrypt and license "
            "their personal data to researchers and advertisers, with smart contracts "
            "enforcing usage limits and streaming payments back to the data owner.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2026-proofnet",
        "year": 2026,
        "slug": "proofnet",
        "file": SRC / "Spring 2026" / "ProofNet" / "ProofNet.mp4",
        "title": "ProofNet – Blockchain Business Case | Spring 2026",
        "description": (
            "Verifiable credentials for a remote-first workforce.\n\n"
            "A decentralized credentialing network that lets employers, universities, "
            "and certifying bodies issue tamper-evident proofs of skills, employment, "
            "and education that candidates can selectively share with recruiters.\n\n"
            + COURSE_TAG
        ),
    },
    {
        "key":  "2026-whistleblower",
        "year": 2026,
        "slug": "whistleblower",
        "file": SRC / "Spring 2026" / "Whistleblower Reward System" / "Whistleblower Reward System.mp4",
        "title": "Whistleblower Reward System – Blockchain Business Case | Spring 2026",
        "description": (
            "Anonymous integrity, on-chain incentives.\n\n"
            "A zero-knowledge framework that lets whistleblowers submit verified evidence "
            "of misconduct anonymously, with smart-contract-escrowed bounties released "
            "once authorities confirm the report.\n\n"
            + COURSE_TAG
        ),
    },
]

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# ── Auth ──────────────────────────────────────────────────────────────────────

def authenticate():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not SECRETS_FILE.exists():
                sys.exit(
                    f"\nERROR: {SECRETS_FILE} not found.\n"
                    "Follow the SETUP instructions at the top of this script.\n"
                )
            flow = InstalledAppFlow.from_client_secrets_file(str(SECRETS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
    return build("youtube", "v3", credentials=creds)


# ── Upload ─────────────────────────────────────────────────────────────────────

def upload_video(youtube, entry):
    body = {
        "snippet": {
            "title": entry["title"],
            "description": entry["description"],
            "tags": ["blockchain", "ethereum", "solidity", "fintech", "smart contracts", "slu"],
            "categoryId": "27",  # Education
        },
        "status": {
            "privacyStatus": "unlisted",
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(
        str(entry["file"]),
        chunksize=4 * 1024 * 1024,   # 4 MB chunks
        resumable=True,
    )
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    response = None
    retry = 0
    RETRIABLE_STATUS = [500, 502, 503, 504]

    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                pct = int(status.progress() * 100)
                print(f"  {pct:3d}% uploaded …", end="\r", flush=True)
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS:
                retry += 1
                if retry > 10:
                    raise
                sleep = random.random() * (2 ** retry)
                print(f"\n  HTTP {e.resp.status} – retrying in {sleep:.1f}s …")
                time.sleep(sleep)
            else:
                raise

    print(f"  ✓ https://youtu.be/{response['id']}          ")
    return response["id"]


# ── Patch content.yml ─────────────────────────────────────────────────────────

def patch_content_yml(results: dict):
    """Replace local `video:` lines and fill empty `videoEmbed:` lines."""
    if not CONTENT_YML.exists():
        print(f"WARNING: {CONTENT_YML} not found – skipping yml patch.")
        return

    text = CONTENT_YML.read_text(encoding="utf-8")

    for key, val in results.items():
        _, slug = key.split("-", 1)
        embed_url = val["embed"]

        # Replace local video path:  video: "assets/cases/..."
        text = re.sub(
            rf'(\bvideo:\s*"assets/cases/\d{{4}}/{re.escape(slug)}/[^"]+\.mp4")',
            f'videoEmbed: "{embed_url}"',
            text,
        )
        # Fill empty videoEmbed placeholder (slug block context)
        # Match:  videoEmbed: ""  within the slug's block
        # We do a targeted replacement keyed on slug proximity
        text = re.sub(
            rf'(slug:\s*"{re.escape(slug)}".*?videoEmbed:\s*)""\s*\n',
            lambda m: m.group(0).replace('videoEmbed: ""', f'videoEmbed: "{embed_url}"'),
            text,
            flags=re.DOTALL,
        )

    CONTENT_YML.write_text(text, encoding="utf-8")
    print(f"  ✓ Patched {CONTENT_YML}")


# ── Cleanup local videos ──────────────────────────────────────────────────────

def remove_local_videos(results: dict):
    removed = []
    for key in results:
        year, slug = key.split("-", 1)
        mp4 = ASSETS_CASES / year / slug / f"{slug}.mp4"
        if mp4.exists():
            mp4.unlink()
            removed.append(str(mp4))
    if removed:
        print(f"\n  Removed {len(removed)} local .mp4 file(s) from assets/cases/:")
        for p in removed:
            print(f"    {p}")
    else:
        print("  No local .mp4 files found to remove (already clean).")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    # Load existing progress
    results: dict = {}
    if RESULTS_FILE.exists():
        results = json.loads(RESULTS_FILE.read_text())

    # Check which videos are missing / already done
    to_upload = [v for v in VIDEOS if v["key"] not in results]
    skipped   = [v for v in VIDEOS if v["key"] in results]

    if skipped:
        print(f"\nSkipping {len(skipped)} already-uploaded video(s):")
        for v in skipped:
            print(f"  {v['key']} → {results[v['key']]['embed']}")

    missing_files = [v for v in to_upload if not v["file"].exists()]
    if missing_files:
        print(f"\nWARNING: {len(missing_files)} source file(s) not found:")
        for v in missing_files:
            print(f"  {v['file']}")
        to_upload = [v for v in to_upload if v["file"].exists()]

    if not to_upload:
        print("\nAll videos already uploaded.")
    else:
        total_mb = sum(v["file"].stat().st_size / 1e6 for v in to_upload)
        print(f"\nUploading {len(to_upload)} video(s)  ({total_mb:.0f} MB total)")
        print("A browser window will open for Google sign-in on the first run.\n")

        youtube = authenticate()

        for i, v in enumerate(to_upload, 1):
            size_mb = v["file"].stat().st_size / 1e6
            print(f"[{i}/{len(to_upload)}] {v['key']}  ({size_mb:.0f} MB)")
            try:
                vid_id = upload_video(youtube, v)
                results[v["key"]] = {
                    "id":    vid_id,
                    "embed": f"https://www.youtube.com/embed/{vid_id}",
                }
                # Save after every upload so a crash doesn't lose progress
                RESULTS_FILE.write_text(json.dumps(results, indent=2))
            except Exception as e:
                print(f"  ERROR uploading {v['key']}: {e}")
                print("  Progress saved. Re-run the script to resume.\n")
                break

    # ── Post-upload actions ───────────────────────────────────────────────────
    if results:
        print("\n── Patching _data/content.yml ──────────────────────────────")
        patch_content_yml(results)

        answer = input("\nRemove local .mp4 files from assets/cases/ to save Git space? [y/N] ").strip().lower()
        if answer == "y":
            remove_local_videos(results)

    # ── Summary ───────────────────────────────────────────────────────────────
    print("\n══ FINAL RESULTS ══════════════════════════════════════════════")
    for key, val in sorted(results.items()):
        print(f"  {key:<25}  {val['embed']}")
    print(f"\nFull results saved to: {RESULTS_FILE}")
    print("\nNext step: commit & push the updated _data/content.yml (and"
          " removed .mp4 files if you chose that option).")


if __name__ == "__main__":
    main()
