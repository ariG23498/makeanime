# makeanime

`makeanime` is a CLI tool for generating anime-style images from a face image and a text prompt using Stable Diffusion XL and an IP-Adapter for applying anime-like styles.

## Features

- Generates anime-style images by blending a face image with anime style references.
- Leverages Stable Diffusion XL for high-quality text-to-image generation.
- Uses an IP-Adapter to combine face and anime-style attributes.
- Supports custom prompt input for greater flexibility.
- Allows control over the influence of face and style using weights.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/makeanime.git
    cd makeanime
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can use the `makeanime` CLI to generate images. The tool accepts the following arguments:

- `image_url`: URL of the face image to be stylized.
- `prompt`: Text prompt to guide the image generation.
- `style_weight`: (Optional) A float that controls how much the anime style influences the image. Default is `0.5`.
- `face_weight`: (Optional) A float that controls how much the face image influences the result. Default is `0.5`.

### Example Command

```bash
python -m makeanime --image_url "https://example.com/your-face-image.jpg" --prompt "anime warrior, fantasy background" --style_weight 0.7 --face_weight 0.3
```

This command will generate an anime-style image based on the provided face image URL and prompt. The resulting image will be saved as `output.png` in the working directory.

## File Structure

- `makeanime/app.py`: Contains the main logic for generating anime-style images.
- `makeanime/__main__.py`: Sets up the CLI using Python's `Fire` library.
  
## How it Works

- **CLIPVisionModelWithProjection** is used to encode the input face image.
- **Stable Diffusion XL** is used for generating images based on the text prompt and the encoded face.
- An **IP-Adapter** is loaded to modulate the anime style and face weights.
- Images are generated at 1024x1024 resolution, and the output is a grid of the original face image and the generated anime image.

## Requirements

- Python 3.8+
- PyTorch
- Diffusers
- Transformers
- Fire

## References

The code is taken from [Hugging Face IP-Adapter Blog Post](https://huggingface.co/docs/diffusers/main/en/using-diffusers/ip_adapter)