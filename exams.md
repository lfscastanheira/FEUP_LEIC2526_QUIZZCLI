

---
# Document: teste1-24-25.pdf
---

Corrected

LCOM Test (4/4/2025)

Duration: 1H

Important notes

• Cell phones or other electronic devices are not allowed in the room. If you brought
a cell phone with you, put it in your backpack or on the desk with the teachers. The backpack
should be on the floor in front of you.

• Place your watch on the table in front of you.

• Only the test statement and writing materials (and possibly your watch) should be on the

table.

• Failure to comply with these rules will result in the exam being cancelled due to attempted

fraud.

• This is a multiple choice test and will be automatically graded.

• Use only blue or black pen. The use of pencils is not permitted.

• Answers are given on the answer sheet and only this sheet will be evaluated.
When answering, you must fill in the answer box completely. Partially filled boxes will
not be detected.

• The minimum score for each question is 0 points (getting one question wrong does not deduct

points from the others).

• All questions are worth 1 point for a total of 20 points.

Question 1 What is the main function of I/O devices in a computer system?

A To provide an interface between the computer and its environment.

B To execute software programs.

C To increase the processing speed of the CPU.

D To store data permanently.

Question 2

In POSIX system calls, what is typically the semantic behind the return values?

A 1 implies success and others error.

B 0 implies error and others success.

C 1 implies error and others success.

D 0 implies success and others error.

Question 3 What is a Device Driver?

A It is a software that allows the interaction with an hardware component.

B It is an hardware component of an external device that receives requests from the processor.

C It is a class of software specifically tailored to configure the processor timer.

D It is a software component that enables direct interaction with hardware without the involve-

ment of the operating system.

Question 4 What is the behavior of the driver_receive system call in Minix?

A It blocks until a software interrupt is received, allowing for context switches.

B It errors if there are no notifications pending for the calling process.

C It polls the PIC for interruptions of relevant peripherals.

D It blocks until a service request message is received, allowing for context switches.

Corrected

For the function timer_set_frequency, a frequency divisor d was required.
Question 5
Which formula correctly expresses its calculation? In this context, freq is the desired frequency,
TIMER_FREQ is the clock frequency for timer in the PC, and USHRT_MAX is the maximum frequency.

A d = TIMER_FREQ / freq

B d = TIMER_FREQ / USHRT_MAX * freq

C d = TIMER_FREQ * freq

D d = freq / USHRT_MAX

Question 6
A Device Driver wants to subscribe to timer interrupts to be notified by the kernel
via a payload with bit 7 set. What should be the value of the hook_id argument passed to the
sys_irqsetpolicy function?

A BIT(7)

B 0

C 7

D 1

Question 7 During class you have studied and used the sys_inb(int port, uint8_t *value)
function. What does it do?

A Reads a word value from the port register, and returns 0 in case of success.

B Writes a word value to the port register, and returns 0 in case of success.

C Reads a word port from the value register, and returns 0 in case of success.

D Writes a word port to the value register, and returns 0 in case of success.

Question 8 Which would be a valid makecode and breakcode combination?

A Makecode: 0xC2, Breakcode: 0xCA

B Makecode: 0x9E, Breakcode: 0x1E

C Makecode: 0x1E, Breakcode: 0x9E

D Makecode: 0xCA, Breakcode: 0xC2

Question 9

In the KBC, why are there scancodes with two bytes?

A For retrocompatibility purposes.

B We could not fit the entire set of scan codes in one byte.

C It allows the scan codes to map to different keyboard language mappings.

D For direct mapping to ASCII.

Question 10
Which one do you expect to perform the least amount of sys_inb() kernel calls?

To read keyboard scancodes you can choose between polling and using interrupts.

A Interrupts.

B Polling.

C The number of calls is random.

D They always perform the same number of calls.

Question 11

Choose the right statement.

A The interrupt mechanism allows for more CPU useful time.

B The polling mechanism allows for more CPU useful time.

C The polling mechanism is always more efficient than the interrupt mechanism.

D The interrupt mechanism implies active await by the CPU.

Corrected

Question 12 What is the primary purpose of the Status Register in the KBC ?

A To store the last typed character inside KBC.

B To display keyboard input on the screen.

C To store the state of the KBC.

D To store user passwords.

Question 13 What does the IRQ_REENABLE flag do in the context of interrupt notification
subscriptions in Minix?

A It makes it so one can later remove the respective subscription.

B It raises the priority of the installed interrupt handler, preventing the kernel from handling

it first.

C It allows the bundled Device Driver in Minix to handle interrupts from the respective IRQ

line once the subscription is removed.

D It makes it so the kernel unmasks interrupts on the IRQ line associated with the specified

hook_id automatically.

Question 14 What is the function of the control register at port 0x43 in the i8254?

A Stores the current time.

B Controls data transfer between CPU and memory.

C Stores user configuration settings.

D Programs the timers and selects counting modes.

Question 15 What does the Read-Back command in the i8254 allow?

A Increasing the processing speed of the timer.

B Changing the interrupt vector.

C Reading the current counter value and programmed configuration.

D Resetting the timer to its default settings.

Question 16

The PIC (Priority Interrupt Controller) is responsible for

A Warning the CPU of a new interrupt.

B Warning the I/O device of interrupts by the correct order.

C Executing the respective interrupt handler for each interrupt.

D Warning the CPU that the interrupt handler stopped executing.

Question 17

In Lab2, how was time measured and a message printed every second?

A Using the Read-Back command every second.

B By subscribing the timer interrupts and using the 60Hz Minix setting.

C By setting the timer with a 120Hz frequency.

D By subscribing the timer interrupts and using the 120Hz Minix setting.

Question 18 What is the primary function of the i8254 timer / counter on a PC?

A To generate random numbers.

B To measure time intervals and generate clock signals.

C To store data permanently.

D To increase CPU processing speed.

Corrected

Question 19 What will be the output of (12 & 10)?

A 8

B 12

C 2

D 10

Question 20 When a key is pressed, how is the scancode sent to the PC?

A The keyboard controller generates a scancode and sends it to the PC via a buffer.

B The keyboard directly modifies memory.

C The CPU manually checks each key for its state.

D The keyboard sends an electrical pulse to the CPU.

Corrected

Answer sheet

Answers are given on this
the version
sheet only.
of this answer sheet matches the version of the exam you received (top right:
+<version>/<page>/<revision>+).
Good luck!

Please check that

Identification

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

←− Code the digits of your number up-
YYYYXXXXX in the grid and fill in your
first and last name below.

First and Last name:

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Answers

Question 1: A B C D

Question 2: A B C D

Question 3: A B C D

Question 4: A B C D

Question 5: A B C D

Question 6: A B C D

Question 7: A B C D

Question 8: A B C D

Question 9: A B C D

Question 10: A B C D

Question 11: A B C D

Question 12: A B C D

Question 13: A B C D

Question 14: A B C D

Question 15: A B C D

Question 16: A B C D

Question 17: A B C D

Question 18: A B C D

Question 19: A B C D

Question 20: A B C D



---
# Document: teste2-24-25.pdf
---

Corrected

LCOM Test (29/4/2025)

Duration: 1H

Important notes

• Cell phones or other electronic devices are not allowed in the room. If you brought
a cell phone with you, put it in your backpack or on the desk with the teachers. The backpack
should be on the floor in front of you.

• Place your watch on the table in front of you.

• Only the test statement and writing materials (and possibly your watch) should be on the

table.

• Failure to comply with these rules will result in the exam being cancelled due to attempted

fraud.

• This is a multiple choice test and will be automatically graded.

• Use only blue or black pen. The use of pencils is not permitted.

• Answers are given on the answer sheet and only this sheet will be evaluated.
When answering, you must fill in the answer box completely. Partially filled boxes will
not be detected.

• The minimum score for each question is 0 points (getting one question wrong does not deduct

points from the others).

• All questions are worth 0.8 points for a total of 20 points.

Question 1
code. What did test 1 do?

In Lab 4, the LCF framework provided different tests to allow you to check your

A The test provided packets in a sequence that corresponds to a vertical movement.

B The test provided packets in a sequence that corresponds to a horizontal movement.

C The test provided packets which report only mouse buttons’ events.

D The test provided random packets.

Question 2
represent?

In the XPM format used in Lab 5, what does each character in the image map

A A sprite’s speed.

B A color index.

C A memory address.

D A pixel position.

Question 3 What is the purpose of an event queue in event driven design?

A Log all past events and corresponding handlers.

B Map event types to event handlers.

C Provide first in first out scheduling of events.

D Provide buffering so that handling of an event may occur asynchronously to its occurrence.

Corrected

Question 4 What I/O device do you use to help you keep a constant refresh rate of the screen?

A The Clock.

B The VRAM.

C The VBE.

D The Timer.

Question 5 Which of the following statements describes a direct-color mode characteristic?

A Uses indexed color.

B Encodes color directly in VRAM.

C Can only show 256 colors.

D Uses palette-based color lookup.

Question 6 What is the primary reason for checking the KBC_ST_IBF bit before sending a
byte to the KBC?

A To ensure the output buffer is ready for data.

B To verify the input buffer is not full and the KBC can receive a new byte.

C To check whether the input buffer contains data to be read.

D To reset the keyboard status IBF before writing data.

Question 7 What is the default graphics mode in the Minix version used in Lab 5?

A 0x115

B 0x03

C 0x030

D 0x105

Question 8
Which of these is false?

Sending a "mouse byte" to the KBC involves a sequence of commands and answers.

A When a NACK response is received, the DD should retry the last sent byte, provided the

last one was acknowledged.

B When a NACK response is received, the DD should retry the entire command, not just the

byte that has failed.

C The KBC might take up to 20 ms to answer a command.

D Command 0xD4 means: “Write Byte to Mouse”

Question 9

How is a xpm image usually stored?

A As a simple 1-dimensional C array of bytes, where each byte is a color.

B As a single character sequence.

C As a simple C array of strings, with the first entries mapping a char to a colour, and then

the mapped chars in the appropriate positions.

D As a compact binary encoding, with a fixed mapping of colors to bit sequences, readable by

a function in the C standard library.

Question 10 When we send a command to the mouse controller, this I/O device returns some
success and failure codes. What are the values of ACK and NACK?

A ACK=EF; NACK=FE;

B ACK=FE; NACK=FA;

C ACK=FA; NACK=FE;

D ACK=FA; NACK=EF;

Corrected

Question 11 What is the main purpose of the BIOS?

A Load the operating system.

B Provide an interface to hardware devices, mainly used for application functionality.

C Load the kernel device drivers.

D Provide an interface to hardware devices, mainly used during boot.

Question 12 We want to set a pixel with an RGB color, using VBE mode 0x115, in a position
(x,y). How should the DD proceed?

A Copy the 3 bytes, one at a time, to the mapped graphics memory with an offset of x +

y*BytesPerColumn.

B Copy the 3 bytes, one at a time, to the mapped graphics memory with an offset of x*3 +

y*BytesPerScanLine.

C "Memcpy" the 3 bytes to the mapped graphics memory with an offset of x*3 +

y*BytesPerScanLine.

D "Memcpy" the 3 bytes to the mapped graphics memory with an offset of x +

y*BytesPerColumn.

Question 13 Which IRQ Line does the mouse controller raise?

A 12

B 2

C 1

D 15

Question 14

How many bytes per packet does a mouse send to its controller?

A It depends on the mouse.

B 2

C 3

D 4

Question 15 What is the VRAM for?

A Storing XPM data.

B Storing graphic card configurations.

C Storing data to be displayed on screen.

D Storing your application data for processing.

Question 16 What is the VBE?

A The VBE standard defines a set of functions related to the operation of the video card.

B The VBE standard defines a set of functions related to the operation of the memory.

C The VBE standard defines a set of functions related to the operation of Minix 3.0.

D The VBE standard defines a set of functions related with the operation of the PC screen.

Question 17
mid-packet. How should it deal with this issue?

In Lab 4, a mouse packet is 3-byte long, but a DD might subscribe interrupts

A Discard the bytes read from the KBC’s output buffer as long as the bit 3 is set.

B Wait 20ms and consider the first byte received afterwards.

C Discard the bytes read from the KBC’s output buffer as long as the bit 3 is unset.

D Infer the byte index in the packet by its structure and use a partial packet appropriately.

Corrected

Question 18 What is the purpose of double buffering?

A Eliminate visual artifacts.

B Prevent color mismatches.

C Save processing time.

D Store backups of images.

Question 19 What is indicated by the X Ovfl and Y Ovfl bits in a PS/2 mouse data packet?

A Overflow in 9-bit displacement counters.

B Interrupt signal to the CPU.

C Overflow in transmission buffer.

D Synchronization error.

Question 20 Which of the following is an advantage of the XPM format?

A It uses binary encoding.

B It is a human-friendly format.

C it uses video ram efficiently.

D It is a machine-efficient format.

Question 21
If we want to write 0x2 to channel Green of pixel in coordinate (x=2,y=3) in a
screen of size 10x10 supporting only two color channels, Red and Green, each using 1 byte, and
assuming the char *buffer is in linear mode, what operation correctly describes this?

A buffer[97] = 0x2;

B buffer[65] = 0x2;

C buffer[47] = 0x2;

D buffer[2][3][1] = 0x2;

Question 22
in pixel position of an image between frames?

In the test function video_test_move(), what argument specifies the difference

A xpm

B xi

C frame_rate

D speed

Question 23

How can a sprite be drawn without leaving a trail behind?

A Use a higher resolution.

B Erase its previous position.

C Draw it slower.

D Use direct memory access.

Question 24 What of the following statements is true?

A The DD must first write command 0xD4 to the KBC using port 0x60.

B The mouse commands and their arguments, must be passed as arguments of the 0xD4 KBC-

command.

C Communication between the mouse and the processor is not mediated by the KBC.

D The mouse command is sent to port 0x64.

Corrected

Question 25
((8:)8:8:8), take in memory?

How much does a frame of 100x100 pixels, with colour components with aRGB

A 240000 bits

B 32kB

C 40kB

D 400000 bits

Corrected

Answer sheet

Answers are given on this
the version
sheet only.
of this answer sheet matches the version of the exam you received (top right:
+<version>/<page>/<revision>+).
Good luck!

Please check that

Identification

←− Code the digits of your number up-
YYYYXXXXX in the grid and fill in your
information below. The number must be
filled in the grid AND below.

First and Last name:

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Number:

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

Question 1: A B C D

Question 14: A B C D

Answers

Question 2: A B C D

Question 3: A B C D

Question 4: A B C D

Question 5: A B C D

Question 6: A B C D

Question 7: A B C D

Question 8: A B C D

Question 9: A B C D

Question 10: A B C D

Question 11: A B C D

Question 12: A B C D

Question 15: A B C D

Question 16: A B C D

Question 17: A B C D

Question 18: A B C D

Question 19: A B C D

Question 20: A B C D

Question 21: A B C D

Question 22: A B C D

Question 23: A B C D

Question 24: A B C D

Question 13: A B C D

Question 25: A B C D



---
# Document: testerecurso-24-25.pdf
---

Corrigido

Teste de Laboratório de Computadores (27/06/2025)

Duração: 1H30

Notas importantes

• Não são permitidos telemóveis ou outros dispositivos electronicos na sala. Se trouxe
um telemóvel consigo, coloque-o na mochila ou na mesa junto dos docentes. A mochila deverá
estar no chão à sua frente.

• Coloque o relógio em cima da mesa à sua frente.

• Em cima da mesa só deverá ter o enunciado do teste e o material de escrita (eventualmente,

o relógio).

• O não cumprimento destas regras implica a anulação do exame por tentativa de fraude.

• Este é um teste de escolha múltipla e será avaliado automaticamente.

• Utilize apenas caneta azul ou preta. Não é permitido o uso de lápis.

• As respostas são dadas na folha de respostas e apenas esta folha será avaliada. Ao
responder, deve preencher totalmente o quadrado de respsta. Quadrados parcialmente
preenchidos não serão detectados.

• A cotação mínima de cada questão é de 0 valores (errar uma questão não desconta nas

restantes).

• Todas as questões valem 0.8 valores para um total de 20 valores.

Questão 1

O que representa um break code no protocolo do teclado PS/2?

A A libertação de uma tecla

B Código de tecla pressionada

C O início de um novo scan code

D Um erro de paridade

Questão 2
posição (x,y). Como deve proceder o driver de dispositivo (DD)?

Queremos definir um pixel com uma cor RGB, usando o modo VBE 0x115, na

A Fazer memcpy dos 3 bytes para a memória gráfica mapeada com um offset de x*3 +

y*BytesPerScanLine.

B Copiar os 3 bytes, um de cada vez, para a memória gráfica mapeada com um offset de x +

y*BytesPerColumn.

C Copiar os 3 bytes, um de cada vez, para a memória gráfica mapeada com um offset de x*3

+ y*BytesPerScanLine.

D Fazer memcpy dos 3 bytes para a memória gráfica mapeada com um offset de x +

y*BytesPerColumn.

Supondo que um rato inclui todas as funcionalidades do laboratório 4 — como
Questão 3
movimento, botões esquerdo, direito e do meio, mas agora também com suporte para a roda —
qual é o número mínimo de bytes necessário para tal protocolo?

A 5

B 4

C 3

D 6

Corrigido

Questão 4
variável local a determinada função?

Qual é o significado da palavra-chave "static" quando usada na declaração de uma

A Torna a variável thread-safe

B Torna a função privada.

C Permite partilhar estado entre invocações da função.

D Torna a variável privada em relação ao uso externo do ficheiro

Questão 5
que está subscrito às interrupções do temporizador (Timer) e do teclado (Keyboard).

Qual é a forma mais correta de lidar com múltiplos tipos de interrupções? Suponha

A Ignoramos as interrupções de um dos dispositivos para poder tratar convenientemente as do

outro dispositivo.

B Realizamos polling e, cada vez que ocorre um dos dois tipos de evento, tratamo-lo separada-

mente.

C Executar uma cadeia de instruções if-else onde, em cada ciclo, verificamos quais interrupções

ocorreram e tratamos cada uma separadamente.

D Quando ocorre um evento do temporizador, verificamos então se também ocorreu um evento

do teclado.

Questão 6
Qual dos dois espera que faça mais chamadas "sys_inb()" ao kernel?

Para ler scancodes do teclado pode escolher entre polling ou usar interrupções.

A Fazem sempre o mesmo número de chamadas.

B O número de chamadas é aleatório.

C Polling.

D Interrupções.

Questão 7

O que é o double buffering em programação gráfica?

A Uma técnica para desenhar diretamente no ecrã para maior desempenho.

B Uma funcionalidade do hardware que duplica a resolução da imagem.

C Um método que utiliza dois buffers para evitar flickering, desenhando numa imagem oculta

antes de a apresentar.

D Um modo de compressão de dados que utiliza dois buffers para maior eficiência.

Questão 8

Para que serve a porta de série?

A Para substituir o teclado e rato em sistemas modernos.

B Para permitir comunicação assíncrona entre o sistema e dispositivos externos, como outros

terminais.

C Para serializar dados em memória.

D Para enviar dados gráficos diretamente para o ecrã sem passar pelo sistema operativo.

Questão 9
Considera-se um tipo union que contém um campo char[10], um campo int e um
campo short numa arquitetura de 32 bits. Qual é o tamanho em memória de uma variável deste
tipo union?

A 10 bytes

B 12 bytes

C 4 bytes

D 8 bytes

Corrigido

Questão 10

Os deslocamentos do rato são representados em quantos bits?

A 9

B 4

C 8

D 16

Questão 11

Qual o comportamento da chamada ao sistema "driver_receive" no Minix?

A Bloqueia até receber uma mensagem "service request", permitindo trocas de contexto.

B Emite um erro se não existirem notificações pendentes associadas ao processo que a chama.

C Faz polling ao PIC para obter interrupções de periféricos relevantes.

D Bloqueia até receber uma interrupção de software, permitindo trocas de contexto.

Questão 12
notificações de interrupção no Minix?

Qual o significado da flag "IRQ_REENABLE", no contexto de subscrição a

A Permite remover a subscrição correspondente mais tarde.

B Permite ao Device Driver incluído no Minix tratar interrupções da linha de IRQ correspon-

dente, assim que a subscrição é removida.

C Eleva a prioridade do handler de interrupção, impedindo que o kernel a trate primeiro.

D Permite ao kernel desmascarar automaticamente interrupções na linha de IRQ associada ao

hook_id especificado.

Questão 13
KBC ao ler dados/valores devolvidos pelo KBC?

Qual é o principal objetivo de verificar o bit KBC_OBF no registo de estado do

A Reiniciar o sinalizador OBF do estado do KBC

B Verificar se o buffer de saída contém dados para serem lidos

C Reiniciar a porta KBC_OUT_BUF

D Determinar se o buffer de entrada do KBC está pronto para aceitar novos dados

Questão 14
Um DD quer subscrever as interrupções do Timer e deseja ser notificado pelo
kernel através de um payload com o bit 5 ativado. Qual deve ser o valor do argumento "hook_id"
usado pelo DD?

A 5

B 1

C 0

D 8

Questão 15

O que é o POSIX?

A Um conjunto de normas que define interfaces para compatibilidade entre sistemas operativos

Unix-like

B Um sistema operativo baseado em Unix

C Um compilador específico para C em sistemas Unix

D Um protocolo de comunicação entre processos em rede

Questão 16

Quanta memória é ocupada por 700x800 pixels com 4 canais de 2 Bytes?

A 560000 bytes

B 800kB

C 4480KB

D 4.48MB

Corrigido

Questão 17

Qual das seguintes afirmações descreve melhor o formato XPM?

A É um formato textual que representa imagens como arrays de strings em C.

B É um formato binário de imagem usado em sistemas Minix.

C É um formato comprimido usado para otimizar armazenamento de imagens bitmap.

D É um formato vetorial usado para representar gráficos dimensionáveis.

Questão 18

Qual é o propósito dos ficheiros .o gerados como artefactos da compilação?

A São ficheiros temporários usados pelo compilador para otimização do uso de memória.

B São artefactos de código compilado para posterior operação de ligação com outros artefactos

semelhantes.

C Acompanham dependências entre ficheiros fonte e de cabeçalho, permitindo compilação in-

cremental.

D Contêm código compilado otimizado para a máquina em que foram gerados.

Questão 19

Qual das seguintes funções pode ser oferecida pelo RTC (Real Time Clock)?

A Gerar interrupções periódicas

B Armazenar informação sobre o Timer do PC

C Monitorização em tempo real do barramento PCI

D Reiniciar automaticamente o sistema após falha de energia

Questão 20

Quantos bytes compõem o pacote padrão do rato PS/2?

A 2

B 3

C 6

D 4

Questão 21

Qual syscall Minix deve ser usada para registar um handler de interrupção?

A sys_alarm

B sys_enable

C sys_irqsetpolicy

D sys_outb

Questão 22
mação de device drivers em Minix?

Qual é a principal vantagem de utilizar um design orientado a eventos na progra-

A Reduz a necessidade de interrupções, simplificando o sistema operativo.

B Permite reagir eficientemente a eventos assíncronos, melhorando o desempenho e o consumo

de CPU.

C Garante que todos os dispositivos são tratados em ordem de chegada.

D Permite que o driver use pooling de forma mais intensiva para obter dados em tempo real.

Corrigido

Questão 23

Qual é a principal vantagem de utilizar interrupções em vez de polling em Minix?

A As interrupções permitem que o processador responda mais rapidamente ao utilizador, sem

overhead adicional.

B As interrupções permitem uma utilização mais eficiente do CPU, evitando a verificação con-

stante de eventos.

C As interrupções garantem que todos os dispositivos recebem prioridade máxima em tempo

real.

D As interrupções reduzem a complexidade do código ao eliminar a necessidade de sincroniza-

ção.

Questão 24

Qual bit é utilizado para sincronizar os pacotes do rato?

A Bit 0 do primeiro byte = 1

B Bit 3 do primeiro byte = 1

C Bit 7 do segundo byte = 1

D Bit 5 do terceiro byte = 0

Questão 25

O que é um Device Driver (DD)?

A É um componente de hardware de um dispositivo externo que recebe pedidos do processador.

B É uma classe de software especificamente desenhada para configurar o temporizador do pro-

cessador.

C É um software que permite interagir com um componente de hardware.

D É um componente de software que permite interacção com hardware sem involver o sistema

operativo.

Questão 26

O que é mapeado com vm_map_phys() em Minix?

A Endereço virtual do processo

B Região de memória de vídeo

C Área da BIOS

D Ficheiros XPM

Questão 27

Que afirmação diz respeito ao modo cor indexado?

A Representamos os canais RGB e o canal alfa.

B Cada cor é representada pelo seu complemento para 2 em 8 bits por canal.

C Representamos os índices de uma tabela de cores.

D Representamos cada canal de cor com um valor de 8 bits.

Questão 28

O que significa um movimento negativo no eixo X do rato?

A Movimento para a direita

B Movimento para cima

C Movimento para a esquerda

D Movimento para baixo

Questão 29

Qual o valor de "i" após a expressão de "int i = 12 & 12" em C?

A 12

B 10

C 2

D 8

Corrigido

Questão 30

Que valor retorna o rato como ACK após comando bem-sucedido?

A 0xFE

B 0xFF

C 0xFA

D 0x00

Corrigido

Folha de respostas

As respostas são dadas apenas nesta folha. Verifique que a versão desta folha de
respostas corresponde à versão do exame que lhe foi atribuído (canto superior direito:
+<versão>/<página>/<revisão>+).
Boa sorte!

Indentificação

←− Codifique os dígitos do seu número
upYYYYXXXXX na grelha e preencha a
sua informação de identificação abaixo. O
número deve ser preenchido na grelha e
abaixo.

Primeiro e último nome:

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Número:

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

0

1

2

3

4

5

6

7

8

9

Questão 1: A B C D

Questão 2: A B C D

Questão 3: A B C D

Questão 4: A B C D

Questão 5: A B C D

Questão 6: A B C D

Questão 7: A B C D

Questão 8: A B C D

Questão 9: A B C D

Respostas

Questão 16: A B C D

Questão 17: A B C D

Questão 18: A B C D

Questão 19: A B C D

Questão 20: A B C D

Questão 21: A B C D

Questão 22: A B C D

Questão 23: A B C D

Questão 24: A B C D

Questão 10: A B C D

Questão 25: A B C D

Questão 11: A B C D

Questão 26: A B C D

Questão 12: A B C D

Questão 27: A B C D

Questão 13: A B C D

Questão 28: A B C D

Questão 14: A B C D

Questão 29: A B C D

Questão 15: A B C D

Questão 30: A B C D

