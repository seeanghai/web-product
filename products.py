import requests

def fetch_products():
    """Fetches product data from the Fake Store API."""
    url = "https://fakestoreapi.com/products"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Warning: Failed to fetch products from API ({e}). Falling back to empty list.")
        return []

# Fetch products once when the module is imported
products = fetch_products()