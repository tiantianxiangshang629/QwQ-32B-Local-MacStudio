import os
import gradio as gr
from mlx_lm import load, generate
from modelscope import snapshot_download

# Use ModelScope for model loading
os.environ['MLXLM_USE_MODELSCOPE'] = 'True'

# Download and load the model
model_dir = snapshot_download('okwinds/QwQ-32B-Preview-MLX-8bit')
model, tokenizer = load(model_dir, tokenizer_config={"eos_token": "<|im_end|>"})

# Function to interact with the model
def chat_with_model(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    response = generate(
        model, tokenizer,
        prompt=text,
        verbose=True,
        max_tokens=512
    )
    return response  # <- No `.text`, it's already a string

# Gradio interface
iface = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(lines=4, placeholder="Enter your question, e.g., provide C++ code for the Fibonacci sequence"),
    outputs=gr.Textbox(label="QwQ-32B Response"),
    title="QwQ-32B Chatbot (MLX)",
    description="Powered by ModelScope + MLX, running locally on Mac M3"
)

iface.launch()
