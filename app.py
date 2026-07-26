import gradio as gr
import numpy as np
import easyocr

reader = easyocr.Reader(['en', 'hi'])

def ext_text(image):
    imgar = np.array(image)
    result = reader.readtext(imgar, detail=0, paragraph=True)

    if result:
        text = ("\n").join(result)
    else:
        text = "No text found in Image"
    return text

app = gr.Interface(
    fn = ext_text,
    inputs = gr.Image(label="Upload Your Image Here", type='pil'),
    outputs = gr.Textbox(label="Output Text Here", lines="10")
)

app.launch()