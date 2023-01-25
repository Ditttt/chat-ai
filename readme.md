# Chat GPT 

chatbot dengan teknologi kecerdasan buatan

## Description
ChatGPT adalah model bahasa besar yang dikembangkan oleh OpenAI. Model ini dilatih pada dataset yang besar yang berisi teks percakapan, sehingga mampu menghasilkan teks yang mirip dengan manusia ketika diberikan pertanyaan atau prompt yang beragam. Beberapa fitur utama dari ChatGPT antara lain:
* Menghasilkan teks dalam beragam gaya dan format, seperti menjawab pertanyaan, melengkapi teks, dan percakapan.
* Memahami dan menggunakan konteks untuk menghasilkan jawaban yang lebih akurat dan relevan.
* Dapat menangani beragam topik dan konten, sehingga cocok untuk berbagai aplikasi.

ChatGPT didasarkan pada arsitektur GPT (Generative Pre-training Transformer), yaitu jenis jaringan saraf transformer. Arsitektur ini memungkinkan untuk pemrosesan paralel yang efisien pada data input, sehingga memungkinkan untuk melatih model dengan miliaran parameter seperti ChatGPT.

ChatGPT open source dan dapat dine-tuning untuk kasus penggunaan khusus, seperti terjemahan bahasa, ringkasan, dan lainnya. Model ini juga dapat diintegrasikan ke dalam berbagai aplikasi dan layanan, seperti chatbot dan asisten virtual.

Sebagai tambahan, perlu diingat bahwa ChatGPT adalah model belajar mesin dan outputnya mungkin bias, salah atau tidak dapat diandalkan, sehingga tidak dapat digunakan untuk keputusan penting.

## Install Via Termux
```bash
> $ pkg update && pkg upgrade
> $ pkg install python
> $ pkg install git
> $ git clone https://github.com/Ditttt/chat-bot.git
> $ cd chat-bot
> $ pip install -r requirements.txt
> $ python main.py
```

### Error Termux
```bash
> $ N: Possible cause: repository is under maintenance or down (wrong sources.list URL?).
```

### Solusi
```bash
> $ pkg remove game-repo
> $ pkg remove science-repo
> $ pkg update
```

## Install Via Ubuntu (debian)
```bash
> $ sudo apt update
> $ sudo apt upgrade
> $ sudo apt install git
> $ sudo apt-get install python3-pip
> $ git clone https://github.com/Ditttt/chat-bot.git
> $ cd chat-bot
> $ pip3 install -r requirements.txt
> $ python main.py
```
