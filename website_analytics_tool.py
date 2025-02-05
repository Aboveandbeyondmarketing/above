from flask import Flask, request, jsonify, render_template
import requests
import whois

app = Flask(__name__, template_folder="templates")

# Ensure this route exists
@app.route('/')
def home():
    return render_template('index.html')

# Ensure this route exists
@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get("website_url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    domain = url.replace("https://", "").replace("http://", "").split("/")[0]

    # Fetch PageSpeed Insights
    def get_pagespeed_insights(url):
        PAGESPEED_API_KEY = "YOUR_GOOGLE_API_KEY"
        api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={PAGESPEED_API_KEY}"
        response = requests.get(api_url)
        return response.json() if response.status_code == 200 else {"error": "Failed to retrieve PageSpeed data"}

    pagespeed_data = get_pagespeed_insights(url)

    # Fetch Domain Info
    try:
        domain_info = whois.whois(domain)
        domain_details = {
            "domain_name": domain_info.domain_name,
            "creation_date": str(domain_info.creation_date),
            "expiration_date": str(domain_info.expiration_date),
            "registrar": domain_info.registrar,
        }
    except:
        domain_details = {"error": "Could not retrieve domain info"}

    return jsonify({
        "pagespeed": pagespeed_data,
        "domain_info": domain_details
    })

if __name__ == '__main__':
    print("Available Routes:")
    print(app.url_map)  # Print all registered routes
    app.run(debug=True)
