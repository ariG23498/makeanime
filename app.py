import gradio as gr
from functools import partial
from makeanime.cli import main

generate_image = partial(main, is_gradio=True)

with gr.Blocks() as demo:
    gr.Markdown("# makeanime: Turn your image into an anime")

    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="Upload your image")
            prompt_input = gr.Text(label="Prompt")
            style_weight_slider = gr.Slider(
                label="Style Weight", minimum=0.0, maximum=1.0, value=0.5, step=0.1
            )
            face_weight_slider = gr.Slider(
                label="Face Weight", minimum=0.0, maximum=1.0, value=0.5, step=0.1
            )
            generate_button = gr.Button("Generate Anime Image")

        with gr.Column():
            result_output = gr.Image()

    generate_button.click(
        fn=generate_image,
        inputs=[image_input, prompt_input, style_weight_slider, face_weight_slider],
        outputs=result_output,
    )

if __name__ == "__main__":
    demo.launch()
