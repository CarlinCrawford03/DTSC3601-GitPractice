import os
from dotenv import load_dotenv
from supabase import create_client, Client

def get_client() -> Client:
    # Load environment variables from .env
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    if not url or not key:
        raise RuntimeError("Missing SUPABASE_URL or SUPABASE_KEY in .env")
    return create_client(url, key)

def main():
    supabase = get_client()

    # Query the Players table
    players = supabase.table("players").select("*").limit(5).execute()
    print("Players:")
    for row in players.data:
        print(row)

    # Query the Achievements table
    achievements = supabase.table("achievements").select("*").limit(5).execute()
    print("\nAchievements:")
    for row in achievements.data:
        print(row)

if __name__ == "__main__":
    main()
