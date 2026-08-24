
const int btnUp = 2; const int btnDown = 3;
const int btnLeft = 4; const int btnRight = 5;
const int ledUp = 6; const int ledDown = 7;
const int ledLeft = 8; const int ledRight = 9;


const int btnSprint = 10; 
const int btnFire = 12;   
const int ledSprint = A0; 
const int ledFire = A1;

const int signal_led = 11;

void setup() {
  Serial.begin(9600);
  

  for(int i=2; i<=5; i++) pinMode(i, INPUT_PULLUP);
  pinMode(btnSprint, INPUT_PULLUP);
  pinMode(btnFire, INPUT_PULLUP);

 
  for(int i=6; i<=9; i++) pinMode(i, OUTPUT);
  pinMode(ledSprint, OUTPUT);
  pinMode(ledFire, OUTPUT);
  pinMode(signal_led, OUTPUT);

  tone(signal_led, 2000, 100);
}

void loop() {
  
  checkButton(btnUp, ledUp, "W");
  checkButton(btnDown, ledDown, "S");
  checkButton(btnLeft, ledLeft, "A");
  checkButton(btnRight, ledRight, "D");

  // Actions
  checkButton(btnSprint, ledSprint, "SHIFT");
  checkButton(btnFire, ledFire, "CTRL");
}

void checkButton(int btnPin, int ledPin, String key) {
  if (digitalRead(btnPin) == LOW) {
    digitalWrite(ledPin, HIGH);
    tone(signal_led, 1200, 30); 
    Serial.println(key);
    
    while(digitalRead(btnPin) == LOW); 
    
    digitalWrite(ledPin, LOW);
  }
}