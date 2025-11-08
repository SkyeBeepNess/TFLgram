import requests

BASE_URL = "https://api.tfl.gov.uk/Line/Mode"


def get_line_status(modes: str = "tube"):
    """Fetch live status for the given transport modes (e.g. 'tube', 'dlr')."""
    url = f"{BASE_URL}/{modes}/Status"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        results = []

        for line in data:
            name = line.get("name", "Unknown Line")
            statuses = line.get("lineStatuses", [])

            if statuses:
                first = statuses[0]
                desc = first.get("statusSeverityDescription", "Unknown")
                severity = first.get("statusSeverity", 0)

                if severity == 10:
                    name = f"✅ {name}"
                elif severity == 9:
                    name = f"⚠️ {name}"
                elif severity <= 8:
                    name = f"❌ {name}"
            else:
                desc = "No status info"

            results.append(f"{name}: {desc}")

        return "\n".join(results) if results else "No data available."

    except requests.RequestException as e:
        return f"⚠️ Failed to fetch data: {e}"