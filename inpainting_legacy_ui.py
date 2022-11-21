import gradio as gr
import PIL
from PIL import Image
import os
from diffusers import OnnxStableDiffusionInpaintPipelineLegacy

auth_token = os.environ.get("API_TOKEN") or True

pipe = OnnxStableDiffusionInpaintPipelineLegacy.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    provider="DmlExecutionProvider",
    revision="onnx",
    safety_checker=None,
    use_auth_token=auth_token
)

def predict(dict, prompt=""):
    init_image = dict["image"].convert("RGB").resize((512, 512))
    mask = dict["mask"].convert("RGB").resize((512, 512))
    output = pipe(prompt = prompt, init_image=init_image, mask_image=mask, strength=0.8)
    return output.images[0]

css = '''
.container {max-width: 1150px;margin: auto;padding-top: 1.5rem}
#image_upload{min-height:400px}
#image_upload [data-testid="image"], #image_upload [data-testid="image"] > div{min-height: 400px}
.footer {margin-bottom: 45px;margin-top: 35px;text-align: center;border-bottom: 1px solid #e5e5e5}
.footer>p {font-size: .8rem; display: inline-block; padding: 0 10px;transform: translateY(10px);background: white}
.dark .footer {border-color: #303030}
.dark .footer>p {background: #0b0f19}
#image_upload .touch-none{display: flex}
'''

image_blocks = gr.Blocks(css=css)
with image_blocks as demo:
    gr.HTML(
        """
            <div style="text-align: center; max-width: 650px; margin: 0 auto;">
              <div
                style="
                  display: inline-flex;
                  align-items: center;
                  gap: 0.8rem;
                  font-size: 1.75rem;
                "
              >
                <h1 style="font-weight: 900; margin-bottom: 7px;">
                  Stable Diffusion Inpainting (Legacy) - Onnx w/DirectML
                </h1>
              </div>
              <p style="margin-bottom: 10px; font-size: 94%">
                Inpaint Stable Diffusion by drawing a mask and providing a prompt
              </p>
            </div>
        """
    )
    with gr.Row():
        with gr.Column():
            image = gr.Image(source='upload', tool='sketch', elem_id="image_upload", type="pil", label="Upload").style(height=400)
            with gr.Box(elem_id="mask_instructions").style(border=False):
                gr.Markdown("Draw a mask above")
            prompt = gr.Textbox(label = 'Your prompt (what you want to add in place of what you are removing)')
            btn = gr.Button("Run")
        with gr.Column():
            result = gr.Image(label="Result")
        btn.click(fn=predict, inputs=[image, prompt], outputs=result)
    gr.HTML(
            """
                <div class="footer">
                </div>
           """
        )
demo.launch()