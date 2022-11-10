#Live ASR Engine 

I have implemented (not from scratch) LiveASREngine using whisper using the following codebase: 

https://github.com/oliverguhr/wav2vec2-live

Installation requirements for whisper (developing anaconda environment): 

1. conda create --name tips -c nvidia -c pytorch -c huggingface -c defaults -c conda-forge python autopep8 pytorch torchvision torchaudio 
2. pytorch-cuda=11.7 transformers pyaudio webrtcvad rx halo onnx onnxruntime pyctcdecode 
3. pip install pysoundfile 
4. conda install -c conda-forge ffmpeg
