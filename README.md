---

# Virtual Try-On Flask Application

This Flask application provides a simple API endpoint to interact with the Texel Virtual Try-On service. It allows users to upload clothing and avatar image URLs to see how clothing items look on different avatars.

## Features

- POST endpoint to accept clothing and avatar image URLs.
- Integration with Texel Virtual Try-On API.
- JSON responses.

## Requirements

- Python 3.6+
- Flask
- requests

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://yourrepository.git
cd yourrepository
```

2. Install the required Python packages.

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application.

```bash
python app.py
```

2. The application will start on `http://localhost:5000`. To interact with the application, send a POST request to `http://localhost:5000/virtual-try-on` with a JSON payload that includes `clothing_image_url` and `avatar_image_url`.

Example using `curl`:

```bash
curl -X POST http://localhost:5000/virtual-try-on \
-H 'Content-Type: application/json' \
-d '{"clothing_image_url": "https://example.com/clothing.jpg", "avatar_image_url": "https://example.com/avatar.jpg"}'
```

## Configuration

Replace `"YOUR_RAPIDAPI_KEY_HERE"` in the `app.py` file with your actual RapidAPI key to authenticate requests to the Texel Virtual Try-On API.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.


