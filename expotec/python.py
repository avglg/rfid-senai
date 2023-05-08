import machine
import mfrc522
import time

# Configuração dos pinos
sck = machine.Pin(18)
mosi = machine.Pin(23)
miso = machine.Pin(19)
sda = machine.Pin(5)
rst = machine.Pin(22)

# Inicializa o módulo RFID RC522
rfid = mfrc522.MFRC522(sck, mosi, miso, sda, rst)

# Função para converter o UID em string hexadecimal
def uid_to_string(uid):
    return ":".join([hex(i)[2:].zfill(2) for i in uid])

# Loop principal
while True:
    # Verifica se há uma tag RFID próxima ao leitor
    (status, tag_type) = rfid.request(rfid.REQIDL)

    if status == rfid.OK:
        print("Tag detectada!")

        # Faz a leitura do UID da tag
        (status, uid) = rfid.anticoll()

        if status == rfid.OK:
            # Converte o UID em string hexadecimal
            uid_str = uid_to_string(uid)
            print("UID da tag:", uid_str)

            # Realiza a autenticação com a chave padrão para o setor 8
            key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            status = rfid.auth(rfid.AUTHENT1A, 8, key, uid)

            if status == rfid.OK:
                print("Autenticação bem-sucedida")

                # Faz a leitura dos dados do setor 8
                data = rfid.read(8)
                print("Dados do setor 8:", data)

                # Faz a escrita de dados no setor 8
                new_data = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10]
                rfid.write(8, new_data)
                print("Dados escritos no setor 8")

                # Realiza a leitura novamente para verificar se os dados foram escritos corretamente
                updated_data = rfid.read(8)
                print("Dados atualizados no setor 8:", updated_data)

                # Finaliza a autenticação
                rfid.stop_crypto()
            else:
                print("Falha na autenticação")
        else:
            print("Falha na leitura do UID")

    time.sleep(0.1)  # Aguarda um curto período antes de fazer a próxima leitura
