import wave
import os
import subprocess

def procurar_audio(letra):
    nome_arquivo = f"{letra}.wav"
    caminho_arquivo = os.path.join("E:\\Projects\\Jobs\\fun-voice\\Sounds", nome_arquivo)
    if os.path.exists(caminho_arquivo):
        return caminho_arquivo
    else:
        print(f"Áudio para a letra '{letra}' não encontrado.")
        return os.path.join("E:\\Projects\\Jobs\\fun-voice\\Sounds\\blank.wav")

def gerar_output(caminho_output, lista_audios):
    with wave.open(caminho_output, "w") as arquivo_wav:
        arquivo_wav.setnchannels(1)  # Mono
        arquivo_wav.setsampwidth(2)  # Largura de amostra de 2 bytes (16 bits)
        arquivo_wav.setframerate(44100 * 4)  # Taxa de amostragem de 44.1 kHz
        

        for caminho_audio in lista_audios:
            if caminho_audio:
                with wave.open(caminho_audio, "r") as audio:
                    frames = audio.readframes(audio.getnframes())
                    arquivo_wav.writeframes(frames)
        subprocess.Popen(["start", caminho_output], shell=True)

def main():
    texto = input("Digite uma frase:")
    caminho_output = r"E:\Projects\Jobs\fun-voice\output.wav"

    lista_audios = [procurar_audio(letra) for letra in texto.lower() if procurar_audio(letra)]

    if lista_audios:
        gerar_output(caminho_output, lista_audios)
        print(f"Arquivo de saída salvo em: {caminho_output}")
    else:
        print("Nenhum áudio encontrado para a frase.")

if __name__ == "__main__":
    main()
