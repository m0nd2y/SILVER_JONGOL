int i = 0;
void setup(){
  Serial.begin(9600);            
}
void loop(){    
  Serial.println(i);                  // 태그의 ID출력
  delay(4000);
  i++;
}
  
