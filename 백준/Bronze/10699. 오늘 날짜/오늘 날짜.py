from datetime import datetime, timezone, timedelta

def main():
    utc_today = datetime.now(timezone.utc)
    kst_today = utc_today + timedelta(hours=9)
    print(kst_today.strftime("%Y-%m-%d"))
    
if __name__ == "__main__":
    main()