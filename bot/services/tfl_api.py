import requests

BASE_URL = "https://api.tfl.gov.uk/"


def get_line_status(modes: str = "tube"):
    """Fetch live status for the given transport modes (e.g. 'tube', 'dlr')."""
    url = f"{BASE_URL}Line/Mode/{modes}/Status"
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
    
def journey_planner(from_loc: str, to_loc: str):
    """Plan a journey from 'from_loc' to 'to_loc' using TFL API."""
    url = f"{BASE_URL}Journey/JourneyResults/{from_loc}/to/{to_loc}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "journeys" not in data or not data["journeys"]:
            return "No journey options found."

        journey = data["journeys"][0]
        legs = journey.get("legs", [])
        result_lines = []
        for leg in legs:
            mode = leg.get("mode", {}).get("name", "Unknown Mode")
            if mode.lower() == "walking":
                modeFormatted = "🚶 Walking" 
            elif mode.lower() == "bus":
                modeFormatted = "🚌"
            elif mode.lower() == "tube":
                modeFormatted = "🚇"
            elif mode.lower() == "dlr":
                modeFormatted = "🚆 DLR"
            elif mode.lower() == "overground":
                modeFormatted = "🚈 Overground"
            elif mode.lower() == "tram":
                modeFormatted = "🚊 Tram"
            elif mode.lower() == "river-bus":
                modeFormatted = "🛥️ River-Bus"
            elif mode.lower() == "national-rail":
                modeFormatted = "🚉 National Rail"     
            
            if mode.lower() == "bus" or mode.lower() == "tube":
                route_name = leg.get("instruction", {}).get("detailed", "")
                print(route_name)
                modeFormatted += f" {route_name}"

            departure = leg.get("departurePoint", {}).get("commonName", "Unknown Departure")
            arrival = leg.get("arrivalPoint", {}).get("commonName", "Unknown Arrival")
            duration = leg.get("duration", 0)

            result_lines.append(f"{modeFormatted} (⏱️{duration} mins): \n📍{departure} 🠮\n📍{arrival}\n")

        total_duration = journey.get("duration", 0)
        result_lines.append(f"⏱️Total Duration: {total_duration} mins")

        return "\n".join(result_lines)

    except requests.RequestException as e:
        return f"⚠️ Failed to fetch journey data: {e}"