import sys
import requests

def text_to_video(prompt: str):
    # RunwayML API endpoint for text-to-video (assuming it's text-to-image for now)
    api_url = "https://dev.runwayml.com/organization/ef7e72a7-2bc6-4943-8155-15ee48a4e805/api-keys"  # Replace with actual endpoint
    api_key = "key_fe3bfbc89282a0f31a9e0c0a8b1ce31f03b56ffa5ce025c6955c9f21ff826c0d25470704def1b9e99c7951176ff5461d7fca9d3336517d054e6c193b4025a065"  # Replace with your actual API key from RunwayML
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }   

    # Data payload containing the prompt
    payload = {
        "prompt": prompt,
        "num_frames": 30,  # Number of frames for the video (adjust as necessary)
        "resolution": "1080p",  # Adjust the resolution based on API settings
        "fps": 30  # Frames per second for the video (adjust as necessary)
    }

    # Send the request to RunwayML API
    response = requests.post(api_url, json=payload, headers=headers)

    if response.status_code == 200:
        # Video generated successfully, retrieve the video URL
        video_url = response.json().get('video_url')
        print(f"Video generated successfully! You can view it here: {video_url}")
    else:
        print(f"Error generating video. Status Code: {response.status_code}, Message: {response.text}")

if __name__ == "__main__":
    input_text = input("Enter the text :")
    text_to_video(input_text)
