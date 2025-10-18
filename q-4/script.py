import base64

# Path to your invoice image
image_path = "download.png"

# Read and encode image as base64
with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

# Format it as a base64 URL
base64_url = f"data:image/png;base64,{encoded_string}"

# Json output
json_result = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Extract text from this image."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": base64_url
          }
        }
      ]
    }
  ]
}

print(json_result)