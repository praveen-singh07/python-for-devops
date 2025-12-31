import requests
import json


def get_data_from_api(url):
    # Fetch data from API
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Handles non-200 responses
        return response.json()

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed -> {e}")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON response.")

    return None


def extract_info(raw_data):
    # Filter useful information
    clean_data = []

    try:
        # Get first 5 items
        for item in raw_data[:5]:
            extracted = {
                "task_id": item.get("id"),
                "task_title": item.get("title"),
                "is_done": item.get("completed")
            }
            clean_data.append(extracted)

    except TypeError:
        print("Error: Invalid data format received from API.")

    return clean_data


def save_and_display(data):
    try:
        # Terminal par print karna
        print("--- Processed Data ---")
        print(json.dumps(data, indent=4))

        # JSON file mein save karna
        with open("output.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\nData successfully saved to output.json")

    except IOError:
        print("Error: Unable to write data to file.")
    except TypeError:
        print("Error: Data is not JSON serializable.")


def main():
    # Public API URL (JSONPlaceholder - Todos list)
    url = "https://jsonplaceholder.typicode.com/todos"

    # 1. API se data lena
    raw_json = get_data_from_api(url)

    # 2. Agar data mil gaya, toh usse process aur save karna
    if raw_json:
        processed_json = extract_info(raw_json)
        save_and_display(processed_json)
    else:
        print("No data to process.")


# Script ko start karna
if __name__ == "__main__":
    main()
