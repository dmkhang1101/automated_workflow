import base64
from openai import OpenAI
from io import BytesIO
from PIL import Image
import tempfile
import time

client = OpenAI()

def generate_asset(task):
    description = task['description']
    asset_url = task.get('asset_url', '')
    output_format = task['output_format'].upper()

    prompt = f"Description: {description}"
    if asset_url:
        prompt += f"\nReference Asset: {asset_url}"

    # -------------------- IMAGE GENERATION --------------------
    if output_format in ["PNG", "JPG"]:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            response_format="b64_json"
        )
        image_bytes = base64.b64decode(response.data[0].b64_json)
        ext = "png" if output_format == "PNG" else "jpg"
        filename = f"{description[:40].replace(' ', '_')}.{ext}"
        return filename, image_bytes

    # -------------------- AUDIO GENERATION --------------------
    elif output_format == "MP3":
        response = client.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=description
        )
        audio_bytes = response.content
        filename = f"{description[:40].replace(' ', '_')}.mp3"
        return filename, audio_bytes

    # -------------------- TEXT / OTHER --------------------
    else:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful AI asset generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        text_asset = response.choices[0].message.content
        filename = f"{description[:40].replace(' ', '_')}.txt"
        return filename, text_asset
