# rfid-senai
Ajudando trabalho expotec

Claro! Aqui está um passo a passo para integrar o módulo RFID RC522 com um Arduino Uno:

Materiais necessários:

Arduino Uno
Módulo RFID RC522
Jumpers macho-fêmea
Passo 1: Conexões físicas

Conecte o pino VCC do módulo RFID ao pino 3.3V do Arduino Uno.
Conecte o pino RST do módulo RFID ao pino digital 9 do Arduino Uno.
Conecte o pino GND do módulo RFID ao pino GND do Arduino Uno.
Conecte o pino IRQ do módulo RFID a qualquer pino digital disponível no Arduino Uno (por exemplo, pino digital 2).
Conecte o pino MISO do módulo RFID ao pino digital 12 do Arduino Uno.
Conecte o pino MOSI do módulo RFID ao pino digital 11 do Arduino Uno.
Conecte o pino SCK do módulo RFID ao pino digital 13 do Arduino Uno.
Conecte o pino SDA do módulo RFID ao pino digital 10 do Arduino Uno.
Passo 2: Instalação da biblioteca

Abra a IDE do Arduino.
Vá em "Sketch" -> "Incluir Biblioteca" -> "Gerenciar Bibliotecas".
Pesquise por "MFRC522" na caixa de pesquisa.
Selecione a biblioteca "MFRC522" e clique em "Instalar".
Passo 3: Escrevendo o código

Abra um novo sketch na IDE do Arduino.
Cole o seguinte código:
cpp
Copy code
#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Inicializa o MFRC522

void setup() {
  Serial.begin(9600);  // Inicializa a comunicação serial
  SPI.begin();         // Inicializa a comunicação SPI
  mfrc522.PCD_Init();  // Inicializa o MFRC522
  
  Serial.println("Aproxime uma tag RFID para leitura...");
}

void loop() {
  // Verifica se há uma tag RFID próxima ao leitor
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    Serial.println("Tag detectada!");
    
    // Faz a leitura do UID da tag
    String uid = "";
    for (byte i = 0; i < mfrc522.uid.size; i++) {
      uid.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? "0" : ""));
      uid.concat(String(mfrc522.uid.uidByte[i], HEX));
      uid.toUpperCase();
      uid.concat(":");
    }
    uid.remove(uid.length() - 1);  // Remove o último ":" da string UID
    
    Serial.print("UID da tag: ");
    Serial.println(uid);
    
    mfrc522.PICC_HaltA();  // Interrompe a comunicação com a tag
  }
}
Passo 4: Carregando o código

Conecte o Arduino Uno ao computador usando um cabo USB.
Selecione a placa "Arduino/Genuino Uno" e a porta correta na IDE do Arduino.
Clique no botão "Carregar" para carregar o código para o Arduino Uno.
Passo
