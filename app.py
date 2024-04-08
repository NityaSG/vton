from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/virtual-try-on', methods=['POST'])
def virtual_try_on():
    # Get the image URLs from the request
    clothing_image_url = request.json.get('clothing_image_url')
    avatar_image_url = request.json.get('avatar_image_url')

    if not clothing_image_url or not avatar_image_url:
        return jsonify({'error': 'Please provide both clothing_image_url and avatar_image_url'}), 400

    # Prepare the payload for the Texel Virtual Try-On API
    payload = {
        "clothing_image_url": clothing_image_url,
        "avatar_image_url": avatar_image_url
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY_HERE",  # Replace YOUR_RAPIDAPI_KEY_HERE with your actual RapidAPI Key
        "X-RapidAPI-Host": "texel-virtual-try-on.p.rapidapi.com"
    }

    try:
        # Make the POST request to the Texel Virtual Try-On API
        response = requests.post("https://texel-virtual-try-on.p.rapidapi.com/try-on-url", data=payload, headers=headers)
        response.raise_for_status()  # Raises a HTTPError for bad responses
        # Return the JSON response from the API
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        # Return the error if something went wrong with the request
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

