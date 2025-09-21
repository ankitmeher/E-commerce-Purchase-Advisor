from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        def log_request(request):
            print("Request URL:", request.url)
            if 'updateFromSlug' in request.url:
                print("=== updateFromSlug request detected ===")
                print("Auth Header:", request.headers.get('auth'))
                print("All Headers:", request.headers)
                with open("./Web Scraping/API_KEY/auth_key.txt", "w") as f:
                    f.write(request.headers.get('auth', 'No auth header found'))
                

        page.on("request", log_request)

        page.goto("https://pricehistoryapp.com/product/tp-link-tapo-p110-mini-16a-smart-wi-fi-plug-energy-monitoring-controller-for-household-appliances-compatible-with-alexa-google-home-improved-pow")
        
        # Wait for 15 seconds to allow all possible requests
        page.wait_for_timeout(5000)

        browser.close()

if __name__ == "__main__":
    run()
