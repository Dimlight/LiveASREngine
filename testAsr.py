from live_asr import LiveWav2Vec2

english_model = ""
#german_model = "maxidl/wav2vec2-large-xlsr-german"
asr = LiveWav2Vec2(english_model, device_name="default")
asr.start()

try:        
    while True:
        text,sample_length,inference_time = asr.get_last_text()    
        res = [sub.split() for sub in text]
  
        # print result
        # print("The list after split of strings is : " + str(res))
        print(f"{sample_length:.3f}s"
        +f"\t{inference_time:.3f}s"
        +f"\t{text}")
        
except KeyboardInterrupt:   
    asr.stop()  