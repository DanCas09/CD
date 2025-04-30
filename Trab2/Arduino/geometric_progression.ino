void setup() {
  Serial.begin(9600);  // Inicializa a comunicação serial com a taxa de transmissão de 9600 bps
}

void loop() {
  int N = 10;  // Número de termos da progressão geométrica
  float primeiroTermo = 2.0;  // Primeiro termo da progressão geométrica
  float razao = 1.5;  // Razão da progressão geométrica

  for (int i = 0; i < N; i++) {
    float termo = primeiroTermo * pow(razao, i);  // Calcula o termo atual da progressão geométrica
    Serial.println(termo);  // Envia o termo pela porta serial
    delay(500);  // Aguarda 500 milissegundos antes de enviar o próximo termo
  }

  while (true) {
    // Aguarda indefinidamente para evitar que o programa reinicie e pare de enviar os termos
  }
}