from fire import Fire
import torch
from diffusers import AutoPipelineForText2Image, DDIMScheduler
from transformers import CLIPVisionModelWithProjection
from diffusers.utils import load_image, make_image_grid


def main(image_url: str, prompt: str, style_weight: float = 0.5, face_weight: float = 0.5):
    image_encoder = CLIPVisionModelWithProjection.from_pretrained(
        "h94/IP-Adapter",
        subfolder="models/image_encoder",
        torch_dtype=torch.float16,
    )
    pipeline = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0",
        torch_dtype=torch.float16,
        image_encoder=image_encoder,
    )
    pipeline.scheduler = DDIMScheduler.from_config(pipeline.scheduler.config)
    pipeline.load_ip_adapter(
        "h94/IP-Adapter",
        subfolder="sdxl_models",
        weight_name=[
            "ip-adapter-plus_sdxl_vit-h.safetensors",
            "ip-adapter-plus-face_sdxl_vit-h.safetensors",
        ],
    )

    pipeline.set_ip_adapter_scale([style_weight, face_weight])
    pipeline.enable_model_cpu_offload()

    face_image = load_image(image_url)

    style_folder = (
        "https://huggingface.co/datasets/ariG23498/images/resolve/main/anime-style"
    )
    style_images = [load_image(f"{style_folder}/image00{i}.png") for i in range(10)]

    generator = torch.Generator(device="cpu").manual_seed(0)

    image = pipeline(
        prompt=prompt,
        height=1024,
        width=1024,
        ip_adapter_image=[style_images, face_image],
        negative_prompt="monochrome, lowres, bad anatomy, worst quality, low quality",
        num_inference_steps=50,
        num_images_per_prompt=1,
        generator=generator,
    ).images[0]

    image = make_image_grid(
        [
            face_image.resize((512, 512)),
            image.resize((512, 512)),
        ],
        rows=1,
        cols=2,
    )
    image.save("output.png")


def app():
    Fire(main)
