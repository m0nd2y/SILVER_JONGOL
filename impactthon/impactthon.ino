#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN   9
#define SS_PIN    10

MFRC522 mfrc(SS_PIN, RST_PIN);// MFR522를 이용하기 위해 mfrc객체를 생성해 줍니다.

void setup() {
  Serial.begin(9600);                          // 시리얼 통신, 속도는 9600
  SPI.begin();                                // SPI 초기화
  // (SPI : 하나의 마스터와 다수의 SLAVE(종속적인 역활)간의 통신 방식)
  mfrc.PCD_Init();
}

void loop() {
  if ( !mfrc.PICC_IsNewCardPresent() || !mfrc.PICC_ReadCardSerial() ) {
    // 태그 접촉이 되지 않았을때 또는 ID가 읽혀지지 않았을때
    delay(500);                                // 0.5초 딜레이
    return;                                    // return
  }

  Serial.println(mfrc.uid.uidByte[0]);        // mfrc.uid.uidByte[0] ~ mfrc.uid.uidByte[3]까지 출력
}

