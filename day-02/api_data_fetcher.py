import requests
import json

def get_data_from_api(url):
    # Fetch data from API
    response = requests.get(url)
    
    # Check karna ki request sahi se kaam kar rahi hai (Status 200)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to get data. Status code: {response.status_code}")
        return None

def extract_info(raw_data):
    # Filter useful information
    clean_data = []
    
    # Get first 5 items
    for item in raw_data[:5]:
        extracted = {
            "task_id": item.get("id"),
            "task_title": item.get("title"),
            "is_done": item.get("completed")
        }
        clean_data.append(extracted)
        
    return clean_data

def save_and_display(data):
    # Terminal par print karna
    print("--- Processed Data ---")
    print(json.dumps(data, indent=4))
    
    # JSON file mein save karna
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)
    print("\nData successfully saved to output.json")

def main():
    # Public API URL (JSONPlaceholder - Todos list)
    url = "https://jsonplaceholder.typicode.com/todos"
    
    # 1. API se data lena
    raw_json = get_data_from_api(url)
    
    # 2. Agar data mil gaya, toh usse process aur save karna
    if raw_json:
        processed_json = extract_info(raw_json)
        save_and_display(processed_json)

# Script ko start karna
if __name__ == "__main__":
    main()