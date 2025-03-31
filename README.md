# QwQ-32B-Local-MacStudio [Deploy in 20mins]

Deploy QwQ-32B locally on Mac Studio (M3 Ultra) using MLX + ModelScope.  
Experience fast, private inference of a 32B-parameter LLM optimized for Apple Silicon.  
Powered by [ModelScope](https://modelscope.cn) + [MLX](https://github.com/ml-explore/mlx).

🚀 No cloud. No latency. 100% local inference.

在 Mac Studio（M3 Ultra）上使用 MLX 和 ModelScope 本地部署 QwQ-32B 模型。
体验为 Apple Silicon 优化的 320 亿参数大语言模型的高速、私密本地推理。
由 ModelScope 和 MLX 提供技术支持。

🚀 无需云端，无延迟，100% 本地推理。
知乎专栏：[在 Mac 上本地部署 QwQ-32B 模](https://zhuanlan.zhihu.com/p/1889893175897872136)

---

## ✨ Demo

![QwQ-32B Gradio Demo](demo.gif)

---

## 🧠 Features

- 🤖 Open-source chatbot interface powered by Gradio  
- 🧱 Quantized 8-bit QwQ-32B model optimized for Mac  
- ⚡️ MLX backend tailored for Apple Silicon (M3, M2, M1)  
- 🔧 Easy, Conda-based installation  
- 🪄 No GPU or cloud dependency

---

## 🧰 System Requirements

- Mac Studio (M3 Ultra recommended)  
- macOS 15+ (tested on Sequoia 15.3)  
- 16GB+ RAM (96GB recommended)  
- Python 3.12  
- ~30GB disk space for model files

---

## 🛠️ Installation

### Step 1: Install Miniconda

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
source ~/miniconda3/bin/activate
conda init --all
```

### Step 2: Create a new Conda environment

```bash
conda create -n qwq python=3.12 -y
conda activate qwq
```

### Step 3: Install dependencies

```bash
pip install modelscope
pip install mlx==0.21.1
pip install mlx-lm==0.21.5
pip install mlx-vlm==0.1.12
pip install gradio
```

### Step 4: Run the Chatbot

```bash
python app.py
```

Then open your browser at: [http://127.0.0.1:7860](http://127.0.0.1:7860)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Credits

- [ModelScope](https://modelscope.cn/)
- [MLX](https://github.com/ml-explore/mlx)
- [QwQ-32B by @okwinds](https://modelscope.cn/models/okwinds/QwQ-32B-Preview-MLX-8bit)
