#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN     5
#define SS_PIN      4
#define LED_PIN     13

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Instancia o objeto MFRC522
bool ledState = LOW;

void setup() {
  Serial.begin(9600);  // Inicializa a comunicação serial
  SPI.begin();         // Inicializa a interface SPI
  mfrc522.PCD_Init();  // Inicializa o leitor RFID

  pinMode(LED_PIN, OUTPUT);  // Configura o pino do LED como saída

  Serial.println("Aproxime um cartao RFID para ler...");
  Serial.println();
}

void loop() {
  // Verifica se há cartões presentes
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    // Lê o UID do cartão
    byte* uid = mfrc522.uid.uidByte;
    int uidLength = mfrc522.uid.size;

    Serial.print("UID do Cartao: ");
    for (int i = 0; i < uidLength; i++) {
      Serial.print(uid[i] < 0x10 ? " 0" : " ");
      Serial.print(uid[i], HEX);
    }
    Serial.println();

    // Acende o LED verde
    digitalWrite(LED_PIN, HIGH);
    ledState = HIGH;

    delay(1000);  // Mantém o LED aceso por 1 segundo

    mfrc522.PICC_HaltA();  // Encerra a comunicação com o cartão

    // Desliga o LED verde
    digitalWrite(LED_PIN, LOW);
    ledState = LOW;
  }
}