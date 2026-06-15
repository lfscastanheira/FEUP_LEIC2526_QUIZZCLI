

---
# Document: 10oo.pdf
---

Computer Labs: OO-programming with C
Or C vs. C++
2º MIEIC

Pedro F. Souto (pfs@fe.up.pt)

May 3, 2024

1/27

Contents

OO and Abstract Data Types

Implementing "Classes" in C

Generic Classes

Conclusion

2/27

Object Oriented Programming

▶ Object-oriented programming is a programming paradigm
that facilitates the development of programs in general and
of some classes of programs in particular:

▶ Graphical user interfaces (GUI)
▶ Computer graphics programs (e.g. games)
▶ Computer simulations

▶ C, unlike C++, is not object-oriented

▶ However, it is possible to develop code in object-oriented

style with C

▶ Actually, to be more precise we should say:

▶ It is possible to develop abstract data types in C

3/27

OO and Classes (A Short and Simplistic View)

▶ A language is OO if it supports the concept of Class
▶ A class is a (data-)type that includes both

State i.e. data members/fields
Behavior i.e. functions/methods that operate on the class’s

state

▶ An object is an instance of a class
▶ A key concept in OO is data encapsulation or data

hiding, i.e.:

▶ Access to the state of an object is possible only by invoking

its methods

Most of the advantages of object orientation stem from this
property.

Problem How can we implement classes/objects in C in such a

way that ensures data-encapsulation?

4/27

Contents

OO and Abstract Data Types

Implementing "Classes" in C

Generic Classes

Conclusion

5/27

Specifying a Class in C

Idea Use:

structs to store the state of an object
functions as the methods of a class

▶ The first argument of each function should be a

pointer to the state of the object on which the method
will operate

▶ Define each class in its own C source (.c) file

▶ This further contributes to the modularity and to the

pluggability of the code

▶ Helps ensuring data hiding (see below)

6/27

Example: A Queue Class – queue.h

typedef struct {
int *buf;
int in,out;

int size;
int count;

} queue_t;

// pointer to array that stores queue elements
// indices of the array pointed by buf
//

to insert/remove elements

// size of the array

// number of elements in queue

queue_t *new_queue(unsigned int ini_size); // "constructor":

void delete_queue(queue_t *q);
int put_queue(queue_t *q, int n); // enqueue ’n’ in queue, returns

//
// queue destructor

ini_size, initial queue size

//
//
//

0 in case of success
-1 otherwise (queue full,

or no space)

int get_queue(queue_t *q, int *p); // dequeue first element from queue to *p, returns

//
//

0 in case of success
-1 otherwise (queue empty)

▶ Note that for all “methods” but the constructor, the first
argument specifies the object that is the target, i.e. the
object on which the method will operate.

7/27

Parenthesis: typedef

▶ Defines a new data type name

▶ E.g.

typedef unsigned char uchar;
makes uchar a synonym of unsigned char

It does not define a new type

▶ POSIX recommends(?reserves?) that data type names
have the _t suffix to distinguish them from other names

▶ There are two main reasons to use typedef:

Portability E.g. the size of integer types may differ among

architectures/compilers

Readability The name queue_t is clearer than using
some complicated struct, although we might use
struct queue instead

besides aesthetics.

8/27

Example: Constructor and Destructor
C has no new nor delete instructions
Use malloc() and free() instead

▶ These are functions of the C standard library
▶ In addition to malloc() there is also realloc() (and

calloc())
#include <stdlib.h>

...
int *buf, *ptr;
...
// allocate an array for 100 ints
buf = (int *) malloc(100*sizeof(int));
...
// reallocate more space for 100 ints
//
ptr = (int *) realloc(buf, 100*sizeof(int));
if( ptr == NULL ) { // run out of memory

-- preserve the value of the first 100 ints

...
} else

buf = ptr;

...
free(buf);

9/27

Parenthesis: The sizeof Operator

▶ sizeof allows to compute the size in bytes of:

▶ a variable, an array or structure;
▶ a type i.e. a basic type, or a derived type such as a

structure or pointer

typedef struct {int color, char *msg} Msg;
int size = sizeof(Msg); // size of struct in bytes
Msg msgs[20];
int size_msgs = sizeof(msgs); // size of array in bytes
// number of elements in array
// int num_el = msgs.size(); // in C++
int num_el = sizeof(msgs)/sizeof(Msg) ;
// dynamically allocate an arry with N elements
// Msg *mptr = new Msg[N]; // in C++
Msg *mptr = (Msg *) malloc(N*sizeof(Msg));
// free memory
// delete[] mptr; // in C++
free(mptr)

10/27

Example: Queue Implementation – queue.c

queue_t *new_queue(unsigned int in_size) {

// allocate queue object
queue_t *q = malloc(sizeof(*q));
if( q == NULL )

return NULL;

// allocate space to store queue elements
q->size = in_size ? in_size : 1;
q->buf = malloc(q->size * sizeof(int));
if( q->buf == NULL ) {

free(q);
return NULL;

}
// initialize state of queue
q->in = q->out = q->count = 0;

return q;

}
void delete_queue(queue_t *q) {

free(q->buf);
free(q);

}

11/27

Example Queue Implementation – queue.c

int put_queue(queue_t *q, int n) {
if( q->count == q->size )

if( resize_queue(q) ) // private function

return -1;

q->buf[q->in++] = n;
q->count++;
adjust_queue(q); // private function
return 0;

}
int get_queue(queue_t *q, int *n) {

if( q->count != 0 ) {

*n = q->buf[q->out++];
q->count--;
adjust_queue(q);
return 0;

}
return -1;

}

Question: How to ensure that resize_queue() and

adjust_queue() are private?

▶ In C, by default, all functions are global, i.e. public

12/27

Answer: Use the static Keyword

▶ The static keyword limits the scope of an “object”, i.e.

function
variable
to the C source (.c) file where that “object” is defined

▶ The static keyword provides a means of hiding names of

global objects from other modules, i.e. C source files

// private: can be invoked only in queue.c
static void adjust_queue(queue_t *q) {

q->in %= q->size;
q->out %= q->size;

}
static int resize_queue(queue_t *q) {

int *p = (int *)realloc(q->buf, 2*(q->size)*sizeof(int));
int i;
if( p == NULL )

return -1;

q->buf = p;
for( i = 0; i < q->in; i++)

q->buf[q->size + i] = q->buf[i];

q->in += q->size;
q->size *= 2;
return 0;

}

13/27

Parenthesis: More on static

▶ When applied to local variables, i.e. variables defined

inside a function, static means that that variable and its
value persist between invocations of that function

Static Global Variables vs. Global Variables
foo.c:

bar.c:

int totallyGlobal;
static int locallyGlobal;
void foo() {

totallyGlobal = 1;
locallyGlobal = 2;

}

Private Functions
popo.c:

// invokable only in popo.c
static void popo() {

...

}

extern int totallyGlobal;

void bar() {

totallyGlobal = 1;

}

Persistent Local Variables
xpto.c:

// counts number of xpto() invocations
void xpto() {

static int count = 0;
count++;
...

}

14/27

Ensuring Encapsulation

▶ Encapsulation hides the details of implementation of an

object from its users

▶ The use of private methods by means of static is not

enough:

▶ In our implementation, a user can access any field of the

object using a pointer to the corresponding struct:
q->size += 10;
Question: How can we prevent it?
Answer: Hiding the implementation of the queue_t
queue.h
struct queue;
typedef struct queue queue_t;

queue.c
#include "queue.h"
struct queue {
char *buf;
int in, out;
int size, count;

The user “class”’ only uses
pointers to queue_t, thus
there is no problem if the type
is incomplete

};
Only the implementation “class”
needs to know the data members
of struct queue

15/27

Example: Use of Queue

#include "queue.h"

int main(int argc, char *argv[]) {

queue_t *q;
char *end_ptr;
unsigned int size = 20;
int n;

// queue default size

if( argc == 2 )

size = strtoul(argv[1], &endptr, 10);

if( endptr == argv[1] )

return -1;

if( (q = new_queue(size)) == NULL )

return -1;

if( put_queue(q, 77) != 0 )
printf("Queue full\n");
if( get_queue(q, &n) != 0 )

printf("Queue empty\n");

else

printf("Dequeued %d\n", n);

delete_queue(q);
return 0;

}

16/27

Contents

OO and Abstract Data Types

Implementing "Classes" in C

Generic Classes

Conclusion

17/27

Generic “Classes”

Problem: queue_t (or struct queue) is able to store values

of type int only

▶ To store values of other types we could write a different

class

Question How about to implement something like C++

templates?

Answer Yes, we can

▶ All we need is to use generic pointers, i.e. void *
▶ But ... we cannot take advantage of pointer arithmetic

18/27

Parenthesis: Pointer Arithmetic

▶ A C pointer is a data type whose values are memory

addresses of variables of a given type

▶ In C, the name of an array is the address of the first

element of that array:

int a[5];
p = a;
p = & (a[0]); /* same as above */

/* set p to point to the first element */

▶ Conversely, we can use the “array notation” to refer to

element i of array a;

for( i = 0; i < 5; i++) {

p[i] = 0;

}

▶ C supports pointer arithmetic – meaningful only when used

with arrays:

for( i = 0; i < 5; i++, p++) {

*p = 0;

}

▶ In the implementation of queue_t, we used the array
notation to access the elements in the queue. E.g. in
put_queue():

q->buf[q->in++] = c;

19/27

Example: Generic Queue

▶ Because we are using generic pointers we cannot rely on

the C compiler for pointer arithmetic:

▶ The compiler does not know the size of each element in the

queue

▶ The size of each element must be kept as part of the state

of the generic queue

#include "gqueue.h"
struct gqueue {

void *buf;
int in, out;
int size, count;
int el_size;

};

// void * instead of int *

// for pointer arithmetic

Question: What is the meaning of in and out (size and

count)?

20/27

Example: Generic Queue

Alternative I: Same meaning as in queue_t

in index of element in array pointed to by buf
out index of element in array pointed to by buf
This is the alternative closer to what the C compiler does when
a pointer to a type is used

Alternative II
in offset of element in array pointed to by buf
out offset of element in array pointed to by buf
In this case, it might be better to name the members in_off
and out_off

Alternative III
in pointer to position in array pointed to by buf
out pointer to position in array pointed to by buf
It would have been better to define in and out as void *

21/27

Example: Generic Queue – gqueue.c

gqueue_t * new_gqueue(unsigned int n_el, int el_size) {

gqueue_t * q = malloc(sizeof(gqueue_t));
if( q == NULL )

return q;

// The user must provide the size of each queue element
q->size = n_el ? n_el : 1;
q->buf = malloc(q->size * el_size);
if( q->buf == NULL ) {

free(q);
return NULL;

}
q->in = q->out = q->count = 0;
q->el_size = el_size;
return q;

}
void delete_gqueue(gqueue_t *q) {

free(q->buf);
free(q);

}
int is_empty_gqueue(gqueue_t *q) {

return q->count == 0;

}

22/27

Example: Generic Queue – gqueue.c

int is_full_gqueue(gqueue_t *q) {

return q->count == q->size;

}
int put_gqueue(gqueue_t *q, void *el) {

if( is_full_queue(q) )

return -1;

// memcpy(dst, src, n_bytes): memory copy
// must do pointer arithmetic explicitly
memcpy(q->buf + q->in*q->el_size, el, q->el_size);
q->in = (q->in + 1) % q->size;
q->count++;
return 0;

}
int get_gqueue(gqueue_t *q, void *el) {

if( is_empty_gqueue(q) )

return -1;

memcpy(el, q->buf + q->out*q->el_size, q->el_size);
q->out = (q->out + 1) % q->size;
q->count--;
return 0;

}

23/27

Example: Use of Generic Queue

typedef struct {int time, freq;} note_t;

gqueue_t *nq = new_gqueue(10, sizeof(note_t));

note_t in, on;
for( i = 0; i<30; i++) {

in.time = 1; in.freq = (i+2)*10;
if( put_gqueue(nq, &in) != 0 )
printf("Full queue\n");

if( get_gqueue(nq, &out) == 0 ) {

printf("%d-%d \n", on.time, on.freq;

} else {

// This should never occur
printf("Empty queue\n");

}

}
delete_gqueue(nq);

24/27

Contents

OO and Abstract Data Types

Implementing "Classes" in C

Generic Classes

Conclusion

25/27

Conclusion

▶ It is possible to use C, thinking in C++
▶ However:

▶ C is not C++
▶ You need more discipline to structure your program and

write your code

▶ We expect you to apply these concepts in your project

▶ If you need some well known data structure (queue, stack,
...) take a look to the interfaces of the classes supported by
OO languages, such as C++, Java or C#

26/27

Thanks to:

I.e. shamelessly translated material by:
▶ João Cardoso (jcard@fe.up.pt)

27/27



---
# Document: 10rtc.pdf
---

Computer Labs: The PC’s Real Time Clock
(RTC)
2º MIEIC

Pedro F. Souto (pfs@fe.up.pt)

April 19, 2024

1/24

The Real Time Clock (RTC)

▶ Integrated circuit that maintains:

▶ The date and
▶ The time of the day

even when the PC is switched-off and unplugged

▶ In addition, it:

▶ Includes alarm functionality and can generate interrupts at

specified times of the day;

▶ Can generate interrupts periodically
▶ Includes at least 50 non-volatile one-byte registers, which
are usually used by the BIOS to store PC’s configuration
▶ Modern RTCs are self-contained subsystems, including:
▶ A micro lithium battery that ensures over 10 years of

operation in the absence of power (when the power is on,
the RTC draws its power from the external power supply)

▶ A quartz oscillator and support circuitry

2/24

Lab 6: The RTC (2013)

▶ Write functions:

int test_config();
int test_date();
int test_int();

that require interfacing with the RTC

▶ These functions are not the kind of functions that you can reuse

later in your project

▶ The idea is that you design the lower level functions (with the final

project in mind).

▶ What’s new?

▶ Use the RTC

▶ Asynchronous concurrent access to shared registers
▶ Develop interrupt handler in assembly (mixed C-assembly

programming)

▶ Some details of what you’ll have to implement revealed only in

class

3/24

The RTC’s Internal Address Space

▶ ... is an array of at least 64 one-byte registers, whose

content is non-volatile. Each register can be:

▶ Addressed individually
▶ Both read and written

▶ The first 10 registers are reserved for time-related

functionality

▶ The following 4 registers are reserved for control of the

RTC

▶ The remaining registers can be used for arbitrary purposes

4/24

Access to the RTC in the PC

▶ The PC uses two ports to access the RTC’s internal

registers:
RTC_ADDR_REG on port 0x70, which must be loaded with

the address of the RTC register to be accessed

RTC_DATA_REG on port 0x71, which is used to transfer

the data to/from the RTC’s register accessed
▶ To read/write a register of the RTC requires always:

1. writing the address of the register to the RTC_ADDR_REG
2. reading/writing one byte from/to the RTC_DATA_REG

5/24

Time of the Day, Alarm and Date Registers

▶ It is possible to program whether the data format is binary

or BCD, but this applies to all registers

▶ It is also possible to program whether the hours range from
0 to 23 or 1 to 12 (plus AM and PM), but this applies both
to the time and the alarm registers

6/24

Reading the Date or the Time of the Day (1/2)

Issue To read the time/date we need to read multiple registers,

sequentially.

Problem What if there is an update while we are reading the

time/date?

▶ E.g. the time updates from 7:32:59 to 7:33:00.

Question How big can the error be?

▶ Does it matter the order in which registers are read?

7/24

Reading the Date or the Time of the Day (2/2)

Solution The RTC offers 3 mechanisms to overcome this issue:

Update in progress flag (UIP) of the RTC

▶ The RTC sets the UIP of REGISTER_A 244 µs before
starting the update and resets it once the update is
done

Update-ended interrupt of the RTC

▶ If enabled, the RTC will interrupt at the end of the

update cycle, the next cycle will occur at least 999
ms later

▶ Register_C should be read in the IH, to clear the

IRQF

Periodic interrupt of the RTC

▶ Periodic interrupts are generated in such a way that
updates occur sensibly in the middle of the period
(actually, 244µs after)

▶ As long as the period is long enough
▶ Thus, after a periodic interrupt occurs, there are at least

P/2 + 244µ seconds before the next update

8/24

Contents

Parenthesis: Preemptions and Concurrent DD’s

9/24

Preemptions and Races Reading the Time

What if: the DD is preempted while reading

the time, e.g.?

Note The arrows labeled IN(XXX)

represent one output to port 0x70 and
one input from port 0x71

How to prevent this?

▶ Disable interrupts before starting to

read (what?)

▶ Enable interrupts again, after reading
▶ Define assembly functions to
enable/disable interrupts

10/24

DDRTCIN(Reg_A)UIP==0IN(hours)hours++IN(minutes)hoursminutesOther Races caused by Preemptions

What if: the DD is preempted while trying to access the RTC and

the preempting process accesses the RTC?

How to prevent this?

▶ Disabling interrupts may not work with more than one

processor

▶ Interrupts are disabled only on one processor/core

▶ Need not worry with this for the RTC in Minix
▶ You’ll study concurrency problems in the OS class

11/24

DD1RTCoutb(0x70,0x0A)Reg_Coutb(0x70,0x0C)inb(0x71)inb(0x71)Reg_?DD2Updating the Date or the Time of the Day

Problem Updates can also make time/date inconsistent

▶ They occur asynchronously the updates of the time/date

registers by the RTC itself

Solution Set the SET bit of Register_B before updating

▶ It prevents the RTC from updating the time/date registers

with the values of the date/time keeping counters
Date/time counters are internal counting registers that

are kept for reading time.

▶ At the end of the update the SET bit should be reset so

that the RTC updates the counters with the values of the
registers

Question Can we use the SET bit of REGISTER_B also for

reading the date/time registers?

12/24

Alarm Registers and ... Alarms

▶ The alarm registers allow to configure an alarm
▶ When the time of day registers match the corresponding
alarm registers, the RTC alarm generates an alarm
interrupt, if that interrupt is enabled at the RTC

▶ Bit AIE (5) of REGISTER_B

▶ The RTC supports don’t care values – values with the 2

MS bits set (11XXXXXX)– for alarm registers

▶ These values match any value of the corresponding

register of the time of day register set

▶ This makes it possible to configure alarms for multiple times

of the day, without changing the contents of the alarm
registers

▶ For example, if all 3 alarm registers are set to “don’t care”,

then the RTC will generate an alarm every second

13/24

Interrupts

▶ The RTC can generate interrupts on 3 different events

Alarm interrupts (AI)
Update interrupts (UI)
Periodic interrupts (PI) with a period between 122 µs and
0.5 s, as determined by bits RS0-RS3 in REGISTER_A

▶ Each of the interrupts can be enabled/disabled individually,

using bits AIE, UIE and PIE of REGISTER_B

▶ The RTC has only one IRQ line, which is connected to line

IRQ0 of PIC2, i.e. IRQ8.

▶ The source of the interrupt can be determined by checking

the flags AF, UF and PF of REGISTER_C

▶ Note that more than one of these flags may be set

simultaneously

▶ REGISTER_C must be read to clear these flags, even if

there is only one enabled interrupt

▶ Flags AF, UF and PF of REGISTER_C are activated upon
the corresponding events even if interrupts are disabled

▶ It is possible to use polling to check for the corresponding

events

14/24

Control/Status Register A

REGISTER_A
BIT 7
UIP

BIT 6
DV2

BIT 5
DV1

BIT 4
DV0

BIT 3
RS3

BIT 2
RS2

BIT 1
RS1

BIT 0
RS0

UIP If set to 1, update in progress. Do not access time/date

registers

▶ More precisely, this bit is set to 1, 244µs before an

update and reset immediately afterwards

DV2-DV0 Control the couting chain (not relevant)
RS3-RS0 Rate selector – for periodic interrupts and square

wave output

15/24

Control/Status Register B

REGISTER_B
BIT 7
SET

BIT 6
PIE

BIT 5
AIE

BIT 4
UIE

BIT 3
SQWE

BIT 2
DM

BIT 1
24/12

BIT 0
DSE

SET Set to 1 to inhibit updates of time/date registers.
PIE, AIE, UIE Set to 1 to enable the corresponding

interrupt source

SQWE Set to 1 to enable square-wave generation
DM Set to 1 to set time, alarm and date registers in binary.

Set to 0, for BCD.

24/12 Set to 1 to set hours range from 0 to 23, and to 0 to

range from 1 to 12

DSE Set to 1 to enable Daylight Savings Time, and to 0 to

disable

▶ Useless: supports only old US DST ...

IMPORTANT Do not change DM, 24/12 or DSE, because it

may interfere with the OS

▶ In any case, changes to DM or 24/12 require setting

the registers affected by those changes

16/24

Control/Status Registers C and D

REGISTER_C
BIT 7
IRQF

BIT 6
PF

BIT 5
AF

BIT 4
UF

BIT 3
0

BIT 2
0

BIT 1
0

BIT 0
0

IRQF IRQ line active
PF Periodic interrupt pending
AF Alarm interrupt pending
UE Update interrupt pending

REGISTER_D
BIT 7
VRT

BIT 6
0

BIT 5
0

BIT 4
0

BIT 3
0

BIT 2
0

BIT 1
0

BIT 0
0

VRT Valid RAM/time – set to 0 when the internal lithium

battery runs out of energy – RTC readings are
questionable

17/24

Lab 6 (2013): test_config()

What? Read and display the configuration of the RTC

▶ The time of day is the state, not the configuration
▶ The value of the alarm registers ... should be considered as

state, not as configuration

For class preparation need not display the configuration in a fancy

way

▶ Just show the value of the registers in hexadecimal

18/24

Lab 6 (2013): test_date()

What? Display the date and time, in a human readable way

▶ Need not support all formats, only those the RTC is configured

with

▶ The mechanism to be used to ensure consistency will be told

in class

▶ Your implementation can use another mechanism, but you will

be penalized (between 50 and 67%)

19/24

Example Code: Waiting for Valid Time/Date

void wait_valid_rtc(void) {
unsigned long regA = 0;

do {

disable();
sys_outb(RTC_ADDR_REG, RTC_REG_A);
sys_inb(RTC_DATA_REG, &regA);
enable();

} while ( regA & RTC_UIP);

}

▶ Assuming that functions enable()/disable()

enable/disable processor interrupts

▶ May not be what you want!!!

▶ What if code is preempted or interrupted?

20/24

Lab 6 (2013): test_int()

What? Handle one of the 3 types of interrupts

▶ Which one will be told in class

▶ Your implementation can handle a different one, but you will be

penalized (between 50 and 67%)

How? Need to implement the handler partially in assembly
▶ At least the I/O part, and may be something else
▶ The variables to be used in the communication between the
assembly code and C code must be declared in assembly

▶ If you prefer the Intel’s syntax, check if it is supported

21/24

Example Code: RTC IH in C

void rtc_ih(void) {

int cause;
unsigned long regA;

sys_outb(RTC_ADDR_REG, RTC_REG_C);
cause = sys_inb(RTC_DATA_REG, &regA);

if( cause & RTC_UF )

handle_update_int();

if( cause & RTC_AF )

handle_alarm_int();

if( cause & RTC_PF )

handle_periodic_int();

}

22/24

Lab6 (2013): Hints for a successful test_int()

Read Register C to clear any pending interrupt

▶ For example, the interrupt may have occurred the last time
you run lab6, but it was not processed because lab6 was
already out of the interrupt dispatching loop.

Write it in C first and only afterwards in assembly
Assembly file must have .S (upper case ’s’) extension
▶ Otherwise, gcc does not call the C pre-processor
Header files used in assembly should include only #defines
▶ In particular, the assembler is not aware of C function

prototypes and will generate an error

sys_iopenable() must be called, otherwise if you try to

execute protected instructions you’ll get a somewhat weird
message, such as:
lab6

255949 0x2ec6 0x22d1 0x28b3 0x100a

23/24

Further Reading

▶ Data sheet of a relatively recent RTC IC
▶ Lab 6 Handout

24/24



---
# Document: 1C.pdf
---

Computer Labs: Introduction to C
2º L.EIC

Pedro F. Souto (pfs@fe.up.pt)

February 20, 2025

1/22

Contents

C vs. C++

I/O in C

Bitwise and Shift Operators

C Integer Conversion

C Pointers

2/22

C vs. C++

▶ C++ is a super-set of C

▶ C++ has classes – facilitates OO programming
▶ C++ has references – safer and simpler than C pointers
▶ It is possible, and often desirable, to use OO programming

in C

▶ We’ll dedicate a full class to that

3/22

C++CContents

C vs. C++

I/O in C

Bitwise and Shift Operators

C Integer Conversion

C Pointers

4/22

I/O in C

▶ C provides standard streams for I/O:

stdin
stdout
stderr

▶ But C does not have the cin and cout objects nor the >>

or the << operators

▶ C does not support classes

▶ Instead you should use the functions:

scanf

▶ Not very useful for LCOM

printf or fprintf()
declared in <stdio.h>

5/22

printf()

printf("video_txt:: vt_print_string(%s, %lu, %lu, 0x%X)\n",
str, row, col, (unsigned)attr);

▶ The first argument is the format string, which comprises:
▶ Standard characters, which will be printed verbatim
▶ Conversion specifications, which start with a % character
▶ Format characters, such as \n or \t, for newline and tabs.

▶ The syntax of the conversion specifications is somewhat
complex. As a minimum, a conversion specification
indicates the type of the value to be printed:

▶ %c for a character, %x for an unsigned integer in

hexadecimal, %d for an integer in decimal, %u for an
unsigned integer in decimal, %l for a long in decimal, %lu
for an unsigned long in decimal, %s for a string, %p for an
address

▶ The remaining arguments should:

▶ Match in number that of conversion specifications;
▶ Have types compatible to those of the corresponding

conversion specification

▶ The first conversion specification refers to the 2nd argument,

and so on

6/22

Contents

C vs. C++

I/O in C

Bitwise and Shift Operators

C Integer Conversion

C Pointers

7/22

▶ The CPU performs all these bitwise operations in parallel

Bitwise Operations

▶ Bitwise operations

▶ are boolean operations, either binary or unary
▶ take integer operands, i.e. one of the following types char,

short, int, long, whether signed or unsigned
▶ apply the operation on every bit of these operands

8/22

opxnynx0x1z0y0z0z1y1zn▶ The CPU performs all these bitwise operations in parallel

Bitwise Operations

▶ Bitwise operations

▶ are boolean operations, either binary or unary
▶ take integer operands, i.e. one of the following types char,

short, int, long, whether signed or unsigned
▶ apply the operation on every bit of these operands

8/22

opxnynx0x1z0y0z0z1y1zn▶ The CPU performs all these bitwise operations in parallel

Bitwise Operations

▶ Bitwise operations

▶ are boolean operations, either binary or unary
▶ take integer operands, i.e. one of the following types char,

short, int, long, whether signed or unsigned
▶ apply the operation on every bit of these operands

8/22

opxnynx0x1z0y0z0z1y1znBitwise Operations

▶ Bitwise operations

▶ are boolean operations, either binary or unary
▶ take integer operands, i.e. one of the following types char,

short, int, long, whether signed or unsigned
▶ apply the operation on every bit of these operands

▶ The CPU performs all these bitwise operations in parallel

8/22

opxnynx0x1z0y0z0z1y1znBitwise Operators

▶ Bitwise operators:

& bitwise AND
| bitwise inclusive OR
^ bitwise exclusive OR
~ one’s complement (unary)

▶ Do not confuse them with the logical operators which

evaluate the truth value of an expression:
&& logical and
|| logical or
! negation

9/22

Bitwise Operators: Use with bit masks

▶ Testing if MS bit is 1:
uchar mask = 0x80;
...
if ( flags & mask )

// 10000000b

// test value of flags MS bit

▶ What if you want to test if the MS bit is 0?

▶ The dual:

mask = ~mask;
if( flags | mask )
does not work! Why?

▶ Other operations:

// mask becomes 01111111b
// could use: flags | ~mask

flags = flags | mask;
flags ^= mask;
flags &= ~mask;

// set flags MS bit
// toggle flags MS bit
// reset flags MS bit

▶ In Lab 2, you can use the | operator to set the operating

mode of the i8254 timer/counter:
#define SQR_WAVE 0x06

[...]
control |= SQR_WAVE;
[...]

10/22

Shift Operators

▶ Similar to corresponding assembly language shift

operations
>> right shift of left hand side (LHS) operand by the
number of bits positions given by the RHS operand

▶ Vacated bits on the left are filled with:
0 if the LHS is unsigned (logical shift)
either 0 or 1 (machine/compiler dependent) if the LHS

operand is signed

<< left shift

▶ Vacated bits on the right are always filled with 0’s

▶ LHS operand must be of any integer type
▶ RHS operand must be non-negative

11/22

Shift Operators: Application

▶ Integer multiplication/division by a power of 2:

unsigned int n;

n <<= 4;
n >>= 3;

// multiply n by 16 (2^4)
// divide n by 8 (2^3)
▶ Flags definitions (to avoid mistakes)

#define SQR_WAVE_BIT0 1
#define SQR_WAVE_BIT1 2

#define BIT(n) (0x1 << (n))

mode |= BIT(SQR_WAVE_BIT1) | BIT(SQR_WAVE_BIT0);

12/22

Contents

C vs. C++

I/O in C

Bitwise and Shift Operators

C Integer Conversion

C Pointers

13/22

C Integer Conversion Rules

▶ C supports different integer types, which differ in their:

Signedness i.e. whether they can represent negative numbers
Precision i.e. the number of bits used in their representation
▶ The C standard specifies a set of rules for conversion from one

integer type to another integer type so that:

▶ The results of code execution are what the programmer expects

▶ One such rule is that:

▶ Operands of arithmetic/logic operators whose type is smaller than

int are promoted to int before performing the operation

the rational for this is

▶ To prevent errors that result from overflow. E.g:

signed char cresult, c1, c2, c3;
c1 = 100;
c2 = 3;
c3 = 4;
cresult = c1 * c2 / c3;

source: CMU SEI

14/22

Problems Source: CMU SEI
Let:

uchar port = 0x5a;
uchar result_8 = ( ~port ) >> 4;

15/22

Problems Source: CMU SEI
Let:

uchar port = 0x5a;
uchar result_8 = ( ~port ) >> 4;

Question: What is the value of result_8?

15/22

Problems Source: CMU SEI
Let:

uchar port = 0x5a;
uchar result_8 = ( ~port ) >> 4;

Question: What is the value of result_8?
Answer: Most likely, you’ll think in terms of 8-bit integers:

8-bit
Expr.
0x5a
port
~port
0xa5
(~port)>>4 0x0a
0x0a
result_8

15/22

Problems Source: CMU SEI
Let:

uchar port = 0x5a;
uchar result_8 = ( ~port ) >> 4;

Question: What is the value of result_8?
Answer: ... but because of integer promotion, need to think in terms

of sizeof(int):

32-bit
8-bit
Expr.
0x5a 0x0000005a
port
~port
0xa5 0xffffffa5
(~port)>>4 0x0a 0xfffffffa
result_8

0x0a 0xfa

15/22

Problems Source: CMU SEI
Let:

uchar port = 0x5a;
uchar result_8 = ( ~port ) >> 4;

Question: What is the value of result_8?
Answer: ... but because of integer promotion, need to think in terms

of sizeof(int):

32-bit

Solution

8-bit
0x5a 0x0000005a 0x0000005a
0xa5 0xffffffa5 0xffffffa5
N/A

Expr.
port
~port
0xa5
(uint_8)
(~port)>>4 0x0a 0xfffffffa 0x0a
0x0a
0x0a 0xfa
result_8

N/A

Solution: One way to fix this is to use a cast on the value after the

complement:

uchar port = 0x5a;
uchar result_8 = (uint8_t) ( ~port ) >> 4;

The cast tells the compiler to handle the complement as an
unsigned 8 bit integer, and the right shift works as expected

15/22

Size of C’ Integer Types and <stdint.h>

▶ To facilitate code portability, C does not specify the size of integer

types

▶ The range of a given type, say int, varies from one platform to

another

▶ However, sometimes we need to use a particular range,

independently of the platform

▶ E.g. the registers of an I/O controller have a size that is

independent of the platform it is integrated into

▶ In this case, you should use the <stdint.h> which includes a
set of typedefs specifying the size and the signedness of
different integer types:

uint8_t
uint16_t
uint32_t
uint64_t

E.g.:

int8_t
int16_t
int32_t
int64_t

uint8_t port = 0x5a;
uint8_t result_8 = (uint8_t) ( ~port ) >> 4;

16/22

Further Reading

▶ INT02-C. Understand integer conversion rules

17/22

Contents

C vs. C++

I/O in C

Bitwise and Shift Operators

C Integer Conversion

C Pointers

18/22

C Variables and Memory

▶ C variables abstract memory, and in particular memory

addresses.

▶ When we declare a variable, e.g.:

int n;

/* Signed int variable */
what the compiler does is to allocate a region of the
process’ address space large enough to contain the value
of a signed integer variable, usually 4 bytes;

▶ Subsequently, while that declaration is in effect (this is

usually called the scope of the declaration), uses of this
variable name translate into accesses to its memory
region:

n = 2*n; /* Double the value of n */
▶ However, in C, almost any “real world” program must

explicitly use addresses

▶ C++ provides references which are substitutes of C

addresses that work in most cases

19/22

C Pointers

▶ A C pointer is a data type whose value is a memory

address.

▶ Program variables are stored in memory
▶ Other C entities are also memory addresses
▶ C provides two basic operators to support pointers:
& to obtain the address of a variable. E.g.

p = &n; /* Initialize pointer p with

the address of variable n */
* to dereference the pointer, i.e. to read/write the

memory positions it refers to.

*p = 8; /* Assign the value 8 to memory position

▶ To declare a pointer (variable), use the * operator:

whose address is
the value of p (variable n) */

int *p; /* Variable/pointer p points to integers or

the value pointed to by p is of type int */

▶ Use of pointers in C is similar to the use of indirect

addressing in assembly code, and as prone to errors.

20/22

C Pointers as Function Arguments

▶ In C, function arguments (or parameters) are passed by

value

▶ In a function call the value of the (actual) arguments are
copied onto the stack, and then used as values of the
function’s formal arguments

▶ Thus the following code snippet will not work as a naïve C

programmer is likely to expect:
int
[...]
swap(a,b);

a, b;

▶ To actually swap the values of variables a and b, you need

a different swap() function:
int
[...]
swap(&a,&b);

a, b;

▶ One of the most common uses of pointers in C is as

function arguments to return values from the callee to the
caller function

▶ Unlike C++, C does not support reference variables

21/22

Strings and Pointers in C

▶ In C, a string is stored as a sequence of characters

terminated by character code 0x00 (zero), also known as
end of string character.

▶ In C, a string is completely defined by the address of its first

character
#define HELLO "Hello, World!"
...
char *p = HELLO; /* Set p to point to string HELLO */
for( len = 0; *p != 0; p++, len++);

▶ The C standard library provides a set of string operations,

that are declared in <string.h>

#include <string.h>
...
char *p = HELLO; /* Set p to point to string HELLO */
len = strlen(p);

▶ String literals are constants not variables. The following is

WRONG:

char *p;
[...]
HELLO = p;

/* p’s initialization; */

/* This is similar to: 5 = n,

with n an integer variable */

22/22



---
# Document: 2timer.pdf
---

Computer Labs: The i8254 Timer/Counter
2º L.EIC

Pedro F. Souto (pfs@fe.up.pt)

February 20, 2025

1/21

Lab 2: The PC’s Timer/Counter - Part I

↭ Write functions:

int timer_test_read_config(uint8_t timer,

int timer_test_time_base(uint8_t timer, uint32_t freq)

enum timer_status_field field)

that require programming the PC’s Timer/Counter

↭ These functions are at a high level for pedagogical reasons

↭ The idea is that you design the lower level functions (with the ﬁnal

project in mind)

↭ Higher-level functions should be in lab2.c
↭ Lower-level functions should be in timer.c

↭ In this lab we have also deﬁned the lower level functions

↭ What’s new?

↭ Program an I/O controller: the PC’s timer counter (i8254)
↭ Use interrupts (Part II)

2/21

The i8254

↭ It is a programmable timer/counter

↭ Each PC has a functionally equivalent circuit, nowadays it is

integrated in the so-called south-bridge

↭ Allows to measure time in a precise way, independently of the

processor speed

↭ It has 3 16-bit counters, each of which
↭ May count either in binary or BCD

↭ If enabled, the count value is decremented

on every clock pulse

↭ The initial counting value must be

previously loaded

↭ Has 6 counting modes, which determine
↭ What happens when the counting value

reaches 0

↭ How the Out pin changes with the value of

the timer/counter

3/21

i8254 Counting Modes (4 of 6)

Mode 0 Interrupt on terminal count – for counting events

↭ OUT goes high and remains high when count reaches 0

Mode 1 Hardware retriggerable one-shot

↭ OUT goes low and remains low until count reaches 0, the
counter is reloaded on a rising edge of the ENABLE input

Mode 2 Rate Generator (divide-by-N counter)

↭ OUT goes low for one clock cycle when count reaches 0,
the counter is reloaded with its initial count afterwards,
and ...

Mode 3 Square Wave Generator – for Lab 2

↭ Similar to mode 2, except for the duty-cycle: OUT will be
high for half of the cycle and low for the remaining half of
the cycle

Note In all modes, the counters perform a down count from a

programmable initial counting value

4/21

i8254 Block Diagram

↭ Three independent 16-bit

counters

↭ Ports 0x40, 0x41 and 0x42
↭ MSB and LSB addressable

separately

↭ Independent counting modes
↭ Independent initial counting

values

↭ An 8 bit-control register

↭ Port 0x43
↭ Programming of each counter

independently

5/21

i8254 Control Word

↭ Used to program the timers, one at a

time

↭ The control word must be written to

the Control Register (0x43)

↭ The initial counting value must be
written on the timer’s port (one of
0x40, 0x41, 0x42)

↭ If programming the initial value of a
single byte, the other byte will be
initialized to 0

Bit
7,6

5,4

3,2,1

0

Value

00
01
10

01
10
11

000
001
x10
x11
100
101

0
1

Function
Counter selection
0
1
2
Counter Initialization
LSB
MSB
LSB followed by MSB
Counting Mode
0
1
2
3
4
5
BCD
Binary (16 bits)
BCD (4 digits)

6/21

i8254 Control Word: Example

Bit
7,6

5,4

3,2,1

0

Value

00
01
10

01
10
11

000
001
x10
x11
100
101

0
1

Function
Counter selection
0
1
2
Counter Initialization
LSB
MSB
LSB followed by MSB
Counting Mode
0
1
2
3
4
5
BCD
Binary (16 bits)
BCD (4 digits)

Example

↭ Timer 2 in mode 3
↭ Binary counting
↭ Initial counting value: 1234 =

0x04D2

Control Register: 10110110

↭ "NOTE: Don’t care bits (X)

should be 0 to insure
compatibility with future Intel
products."

Timer2 LSB 0xD2
Timer2 MSB 0x04

How to assemble the control word?

7/21

How to assemble the control word?

Use the macros deﬁned in i8254.h

Use bitwise operations

8/21

i8254: Read-Back Command

The command

↭ Allows to retrieve

↭ the programmed conﬁguration
↭ and/or the current counting

value

of one or more timers

↭ The bars over COUNT and

STATUS means that these bits
are active in 0

↭ Written to the Control Register

(0x43)

Reading of the status/count

↭ The conﬁguration (status) is read
from the timer’s data register

↭ The 6 LSBs match those of the

Control Word

Read-Back Command Format

Value

Function

Read-Back Command

11

0

0

1

1

1

COUNT

Read counter value

STATUS

Read programmed mode

Select Timer 2

Yes

Select Timer 1

Yes

Select Timer 0

Yes

Reserved

Bit

7,6

5

4

3

2

1

0

Value

Read-Back Status Format
Function
Output
Null Count
Counter Initialization
Programmed Mode
BCD

Bit
7
6
5,4
3,2,1
0

9/21

↭ The counting value is also read from the timer’s data register

↭ If both status and count are requested, the status is the ﬁrst

value returned

How to parse the the status word?

Use the macros deﬁned in i8254.h

Use bitwise operations

10/21

i8254: Use in the PC (1/2)

↭ Timer 0 is used to provide a time base.
↭ Timer 1 was used for DRAM refresh

↭ Via DMA channel 0

(Most likely this is not true any more.)

↭ Timer 2 is used for tone generation

11/21

i8254: Use in the PC (2/2)

↭ The i8254 is mapped in the I/0 address space:
Timer 0:
0x40
Timer 1:
0x41
0x42
Timer 2:
Control Register: 0x43

↭ Need to use IN/OUT assembly instructions

↭ Minix 3 provides the SYS_DEVIO kernel call for doing I/O

#include <minix/syslib.h>

int sys_inb(int port, u32_t *byte);
int sys_outb(int port, u32_t byte);

↭ Note that the second argument of sys_inb() must be the

address of a 32-bit unsigned integer variable.

↭ Hint (must) implement

util_sys_inb(int port, u8_t *byte)

↭ This is a wrapper to sys_inb()
↭ You can use it thereafter instead of sys_inb()
↭ Need to write to the control register before accessing any

of the timers

↭ Both to program (control word) a timer, or to read its

conﬁguration (read-back command)

12/21

Minix 3 and Timer 0

↭ At boot time, Minix 3 programs Timer 0 to generate a

square wave with a ﬁxed frequency

↭ Timer 0 will generate an interrupt at a ﬁxed rate:

↭ Its output is connected to IRQ0
↭ Minix 3 uses these interrupts to measure time

↭ The interrupt handler increments a global variable on every

interrupt

↭ The value of this variable increments at a ﬁxed, known, rate

↭ Minix 3 uses this variable mainly for:
↭ Keeping track of the date/time
↭ Implementing SW timers

13/21

Lab 2: Part 1 - Reading Timer Conﬁguration (1/2)

What to do? Read timer conﬁguration in Minix

int timer_test_read_config(uint8_t timer,

enum timer_status_field field)

1. Write read-back command to read input timer

conﬁguration:

↭ Make sure 2 MSBs are both 1
↭ Select only the status (not the counting value)

↭ Remember, these are active low, i.e.when the bit value is 0

2. Read the timer port
3. Parse the conﬁguration read
4. Call the function timer_print_config() that we

provide you

How to design it? Try to develop an API that can be used in the

project.
int timer_get_conf(uint8_t timer, uint8_t *st);
int timer_display_conf(uint8_t timer, uint8_t st,

enum timer_status_field status);

14/21

Lab 2: Part 1 - Reading Timer Conﬁguration (2/2)
Stuff we provide you

int timer_print_config(uint8_t timer,

enum timer_status_field field,
union timer_status_field_val val);

enum timer_status_field {

tsf_all,
tsf_initial,
tsf_mode,
tsf_base

// configuration in hexadecimal
// timer initialization mode
// timer counting mode
// timer counting base

};
enum timer_init {
INVAL_val,
LSB_only,
MSB_only,
MSB_after_LSB

};
union timer_status_field_val {

byte;

uint8_t
enum timer_init in_mode;
uint8_t
bool

// status, in hexadecimal
// initialization mode

count_mode; // counting mode: 0, 1, ..., 5
bcd;

// true, if counting in BCD

};

15/21

C Enumerated Types

↭ This is a user-deﬁned type that can take one of a ﬁnite

number of values
enum timer_status_field {

tsf_all,
tsf_initial,
tsf_mode,
tsf_base

// configuration in hexadecimal
// timer initialization mode
// timer counting mode
// timer counting base

};
enum timer_status_field info = tsf_base;

↭ The C compiler represents each possible value of an
enumerated type by an integer value. By default:

↭ The ﬁrst value is represented with 0
↭ Any other value, is one more than the previous value
↭ However, it is possible to assign to an enumerated value an

integer value different from the default (e.g.

tsf_all = 255;)

↭ The names of the members of an enumerated type have global

scope

↭ To avoid collisions we use the tsf_ preﬁx

↭ The use of enumerated types makes the code more readable

16/21

C Unions

↭ Syntatically, a union data type appears like a struct:

union timer_status_field_val {

byte;

uint8_t
enum timer_init in_mode;
uint8_t
bool

// status, in hexadecimal
// initialization mode

count_mode; // counting mode: 0, 1, ..., 5
bcd;

// true, if counting in BCD

};

↭ Access to the members of a union is via the dot operator

↭ However, semantically, there is a big difference:

Union contains space to store any of its members, but not all

of its members simultaneously

↭ The name union stems from the fact that a variable of this
type can take values of any of the types of its members

Struct contains space to store all of its members

simultaneously

In timer_print_config() we are using it to reduce the

number of arguments passed

↭ But need another argument the kind of information passed

17/21

Lab 2: Part 1 - Setting the Time-Base (1/2)

What to do? Change the rate at which a timer 0 generates

interrupts.
int timer_test_time_base(uint8_t timer, uint32_t freq)

1. Write control word to conﬁgure Timer 0:

↭ Do not change 4 least-signiﬁcant bits

↭ Mode (3)
↭ BCD/Binary counting

You need to read the Timer 0 conﬁguration ﬁrst.

↭ Preferably, LSB followed by MSB

2. Load timer’s register with the value of the divisor to

generate the frequency corresponding to the desired
rate

↭ Depends on the previous step
↭ Remember that the frequency of the Clock input of all

timers is 1 193 181 Hz

18/21

Lab 2: Part 1 - Setting the Time-Base (2/2)

How to design it? Try to develop an API that can be used in the

project.
int timer_set_frequency(uint8_t timer, uint32_t freq);

This function should work for every timer, not only Timer 0.

How do we know it works? Use the date command.

Minix 3 programs Timer 0 to generate interrupts at a ﬁxed
rate (60 Hz) at boot-time and assumes that rate is not
changed thereafter

↭ By programming a different rate, Minix 3 will measure

time incorrectly. E.g. with a 30 Hz rate ...

↭ Or, even better, use the test code provided.

19/21

Further Reading

↭ Lab 2 Handout
↭ i8254 Data-sheet

21/21



---
# Document: 3ints.pdf
---

Computer Labs: I/O and Interrupts
2º L.EIC

Pedro F. Souto (pfs@fe.up.pt)

February 27, 2025

1/20

I/O Operation

▶ I/O devices are the interface between the computer and its

environment

▶ Most of the time, the processor is not synchronized with its

environment

▶ I/O operations are asynchronous wrt the processor

operation

▶ Usually, I/O devices are much slower than the processor
▶ The processor must wait for an I/O device to complete its

current operation before it can request a new one

2/20

Response time Highly variable – depends on what the

processor has to do between consecutive polls.

Efficiency/Overhead Depends on the frequency of the event

▶ The more frequent the more efficient

▶ Assuming, polling at a constant rate

Response time Usually responsive – depends on the time:

▶ interrupts are disabled or

▶ higher priority interrupts take to be served

Efficiency/Overhead Depends on the frequency of the event

▶ The more frequent the less efficient

▶ Overhead per interrupt is higher than that per poll

How Does the Processor Know about an I/O event?

Polling The processor polls the I/O device, i.e. reads a status

register, to find out

Interrupts The I/O device notifies the processor, via the

interrupt mechanism

3/20

Efficiency/Overhead Depends on the frequency of the event

▶ The more frequent the more efficient

▶ Assuming, polling at a constant rate

Efficiency/Overhead Depends on the frequency of the event

▶ The more frequent the less efficient

▶ Overhead per interrupt is higher than that per poll

How Does the Processor Know about an I/O event?

Polling The processor polls the I/O device, i.e. reads a status

register, to find out
Response time Highly variable – depends on what the

processor has to do between consecutive polls.

Interrupts The I/O device notifies the processor, via the

interrupt mechanism
Response time Usually responsive – depends on the time:

▶ interrupts are disabled or
▶ higher priority interrupts take to be served

3/20

How Does the Processor Know about an I/O event?

Polling The processor polls the I/O device, i.e. reads a status

register, to find out
Response time Highly variable – depends on what the

processor has to do between consecutive polls.

Efficiency/Overhead Depends on the frequency of the event

▶ The more frequent the more efficient
▶ Assuming, polling at a constant rate

Interrupts The I/O device notifies the processor, via the

interrupt mechanism
Response time Usually responsive – depends on the time:

▶ interrupts are disabled or
▶ higher priority interrupts take to be served

Efficiency/Overhead Depends on the frequency of the event

▶ The more frequent the less efficient
▶ Overhead per interrupt is higher than that per poll

3/20

Lab 2: timer_test_int()

What to do? Print one message per second, for a time interval

whose duration is specified in its argument, by using:

▶ Timer 0 interrupts
▶ LCF function:

void timer_print_elapsed_time()

4/20

PC Interrupt HW: Priority Interrupt Controller (PIC)

Imp: If a bit of the Interrupt Mask is set, the corresponding IRQ is
disabled.

5/20

0PIC101102711PIC20100271IRQ2IRQ1IRQ0IRQ7CPUIRQ10IRQ9IRQ8IRQ15InterruptMaskInterruptRequestAcknowledgeVectorIDTRMemory8×Vectorpushmovpopeoiiretd...IHaddressInterruptHandler1.Devicegeneratesinterrupt2.PICchecksmask3.PICraisesrequesttoCPU4.CPUacksinterrupt5.PICforwardsvector6.CPUcomputesIH’saddress7.CPUjumpstoIH8.CPUexecutesIH9.CPUnotiﬁesPIC(eoi)andreturnswithiretdIDTPC Interrupts: IRQ Lines and Vectors

PIC 2

IRQ0
IRQ1
IRQ2- IRQ7

PIC 1
IRQ0
IRQ1
IRQ2

IRQ3
IRQ4
IRQ5
IRQ6
IRQ7

Device
Timer
Keyboard
PIC2
Real Time Clock
Replace IRQ2
Reserved
Serial port COM2
Serial port COM1
Reserved/Sound card
Floppy disk
Parallel port

Vector
0x08
0x09
0x0A
0x70
0x71
0x72-0x77
0x0B
0x0C
0x0D
0x0E
0x0F

IRQ line Determined by the HW designer (IBM)

Vector Specified also by IBM, but can be configured at boot

time. All that is needed is:
1. Configure the PIC
2. Configure the IDT (Interrupt Descriptor Table)

6/20

Interrupt Handlers (IH)

▶ IHs are executed by the HW upon an interrupt
▶ They run asynchronously wrt other code
▶ They take no arguments
▶ They return no values

▶ IHs used to be written in assembly
▶ Need to perform I/O operations

isr_name:

push ..
...
mov al, EOI
out PIC1_CMD, al
pop ...
iretd

; save all registers used
; IH instructions
; signal EOI
to PIC1
;
; restore all registers used

▶ But nowadays, they are usually written in C (for reasons of

portability)

Terminology Interrupt handlers are also called interrupt service
routines (ISR) and are part of the respective device driver

7/20

Issue How do you do interrupt handling?

▶ Interrupt handling requires performing operations that

usually require special privileges

Solution

1. Perform only the bare minimum in the kernel: this is

done by the generic interrupt handler (GIH)

2. Device specific operations are performed by the device

drivers themselves at user level

▶ Using kernel calls to perform privileged operations

Interrupt Handling in Minix 3

▶ In Minix, device drivers are implemented as user-level

processes, rather than at the kernel-level

▶ This was an important design decision in Minix 3

8/20

Solution

1. Perform only the bare minimum in the kernel: this is

done by the generic interrupt handler (GIH)

2. Device specific operations are performed by the device

drivers themselves at user level

▶ Using kernel calls to perform privileged operations

Interrupt Handling in Minix 3

▶ In Minix, device drivers are implemented as user-level

processes, rather than at the kernel-level

▶ This was an important design decision in Minix 3

Issue How do you do interrupt handling?

▶ Interrupt handling requires performing operations that

usually require special privileges

8/20

Interrupt Handling in Minix 3

▶ In Minix, device drivers are implemented as user-level

processes, rather than at the kernel-level

▶ This was an important design decision in Minix 3

Issue How do you do interrupt handling?

▶ Interrupt handling requires performing operations that

usually require special privileges

Solution

1. Perform only the bare minimum in the kernel: this is

done by the generic interrupt handler (GIH)

2. Device specific operations are performed by the device

drivers themselves at user level

▶ Using kernel calls to perform privileged operations

8/20

Minix 3: The Generic Interrupt Handler (GIH)

▶ Upon an interrupt, the GIH:

1. Masks, in the PIC, the respective IRQ line.
2. Notifies all the device drivers (DD) interested in that

interrupt

3. If possible, unmasks, in the PIC, the respective IRQ line.
4. Acknowledges the interrupt by issuing the EOI command to

the PIC.

5. Issues the IRETD instruction

Issue 1 How does the GIH know that a DD is interested in an

interrupt?

Issue 2 How does the GIH notify a DD?

Issue 3 How does a DD receive the notification of the GIH?

Issue 4 How does the GIH know if it can unmask the IRQ line

in the PIC?

Issue 5 If the GIH does not unmask the IRQ line in the PIC,

when, how and whom does it?

9/20

Answer The DD tells it, using kernel call:

int sys_irqsetpolicy(int irq_line, int policy, int *hook_id);

where

irq_line is the IRQ line of the device

policy use IRQ_REENABLE to inform the GIH that it can

unmask the IRQ line in the PIC.

▶ This answers Issue 4: How does the GIH know if it

can unmask the IRQ line in the PIC?

hook_id is both:

this interrupt

input an id to be used by the kernel on interrupt notification

output an id to be used by the DD in other kernel calls on

▶ sys_irqsetpolicy() can be viewed as an interrupt

notification subscription

Issue 1

How does the GIH know that a DD is interested in an
interrupt?

10/20

Issue 1

How does the GIH know that a DD is interested in an
interrupt?
Answer The DD tells it, using kernel call:

int sys_irqsetpolicy(int irq_line, int policy, int *hook_id);
where
irq_line is the IRQ line of the device
policy use IRQ_REENABLE to inform the GIH that it can

unmask the IRQ line in the PIC.

▶ This answers Issue 4: How does the GIH know if it

can unmask the IRQ line in the PIC?

hook_id is both:

input an id to be used by the kernel on interrupt notification
output an id to be used by the DD in other kernel calls on

this interrupt

▶ sys_irqsetpolicy() can be viewed as an interrupt

notification subscription

10/20

Minix 3: Other Interrupt Related Kernel Calls

sys_irqrmpolicy(int *hook_id) Cancels a previous

interrupt notification subscription, by specifying a pointer to
the hook_id returned by the kernel in
sys_irqsetpolicy()

sys_irqenable(int *hook_id) Unmasks at the PIC an

interrupt line associated with a previously subscribed
interrupt notification, by specifying a pointer to the hook_id
returned by the kernel in sys_irqsetpolicy()

sys_irqdisable(int *hook_id) Masks at the PIC an
interrupt line associated with a previously subscribed
interrupt notification, by specifying a pointer to the hook_id
returned by the kernel in sys_irqsetpolicy()

11/20

Answer It uses the standard interprocess communication (IPC)

mechanism used for communication:

▶ between processes;

▶ between the (micro) kernel and a process

More specifically, it uses notifications

Minix 3 IPC This is essentially a message based mechanism

▶ Processes send and receive messages to communicate

with one another, and with the kernel.

▶ A notification is a special kind of message, used by the

kernel to unsolicited communication with a user-level

process.

Issue 2

How does the GIH notify the DD of the occurrence of an
interrupt?

12/20

Issue 2

How does the GIH notify the DD of the occurrence of an
interrupt?

Answer It uses the standard interprocess communication (IPC)

mechanism used for communication:

▶ between processes;
▶ between the (micro) kernel and a process

More specifically, it uses notifications

Minix 3 IPC This is essentially a message based mechanism

▶ Processes send and receive messages to communicate

with one another, and with the kernel.

▶ A notification is a special kind of message, used by the
kernel to unsolicited communication with a user-level
process.

12/20

Short Answer Just use the IPC mechanism.

Useful Answer Use some library calls provided by the

libdrivers library

Issue 3 (1/2)

How does the DD receive the notification of the GIH?

13/20

Issue 3 (1/2)

How does the DD receive the notification of the GIH?
Short Answer Just use the IPC mechanism.

Useful Answer Use some library calls provided by the

libdrivers library

13/20

}
if (is_ipc_notify(ipc_status)) { /* received notification */

printf("driver_receive failed with: %d", r);
continue;

/* Get a request message. */
if( (r = driver_receive(ANY, &msg, &ipc_status)) != 0 ) {

1: #include <lcom/lcf.h>
2: int ipc_status;
3: message msg;
4: while( 1 ) { /* You may want to use a different condition */
5:
6:
7:
8:
9:
10:
11:
12:
13:
14:
15:
16:
17:
18:
19:
20:
21:
22:
23: }

switch (_ENDPOINT_P(msg.m_source)) {
case HARDWARE: /* hardware interrupt notification */

/* no standard messages expected: do nothing */

... /* process it */

} else { /* received a standard message, not a notification */

}
break;

break; /* no other notifications expected: do nothing */

default:

}

}

if (msg.m_notify.interrupts & irq_set) { /* subscribed interrupt */

14/20

Why: msg.m_notify.interrupts?

▶ Interrupt handlers take no arguments (and return no

values)

Answer True, but usually an IH knows which interrupt request it

is handling

▶ Minix 3 allows a DD to subscribe notifications on several

interrupt lines

What is its value?
Answer It is based on the input value of hook_id passed by
the DD in the corresponding sys_irqsetpolicy().

▶ If a given interrupt is pending then the corresponding
hook_id bit of msg.m_notify.interrupts is set.

▶ Why not just the hook_id?
What should irq_set value be?

▶ irq_set is used as a mask to test which interrupts are

pending

15/20

Issue 3 (2/2)

Key Observation In Minix 3, a DD is an event driven service

that receives and processes messages

▶ either interrupt notifications from the kernel (GIH)
▶ or service requests from other processes

However, the programs in LCOM are not DD: they do not
receive requests from other processes

16/20

Lab 2: timer_test_int()

What to do? Print one message per second, for a time interval

whose duration is specified in its argument.

1. Subscribe Timer 0 interrupts
2. Print message at 1 second intervals, by calling the LCF

function:
void timer_print_elapsed_time()

3. Unsubscribe Timer 0 at the end

How to design it? It is not easy to come up with an API that can

be used in the project

▶ Implement int timer_subscribe_int() to hide

from other code i8254 related details, such as the IRQ
line used

▶ It returns, via its argumens, the bit number, that will be
set in msg.m_notify.interrupts upon a TIMER 0
interrupt

▶ Implement the interrupt handler also in timer.c
▶ Implement the “interrupt loop” in timer_test_int()

17/20

▶ I.e., if a DD does not set the IRQ_REENABLE policy in its

interrupt subscription request (sys_irqsetpolicy())

Answer The DD will have to do it, as soon as possible

▶ In most cases, you’ll want to set the IRQ_REENABLE

policy

▶ In Lab 2, certainly

How can a DD unmask the IRQ line in the PIC??

▶ By calling sys_irqenable(int *hook_id)

▶ Note that here hook_id should point to a variable with

the value returned by the kernel in

sys_irqsetpolicy()

That is, the kernel will unmask the IRQ line, upon request of

the DD.

Issue 5 (and Last)

What if the GIH does not unmask the IRQ line in the PIC?

18/20

Issue 5 (and Last)

What if the GIH does not unmask the IRQ line in the PIC?
▶ I.e., if a DD does not set the IRQ_REENABLE policy in its
interrupt subscription request (sys_irqsetpolicy())

Answer The DD will have to do it, as soon as possible

▶ In most cases, you’ll want to set the IRQ_REENABLE

policy

▶ In Lab 2, certainly

How can a DD unmask the IRQ line in the PIC??

▶ By calling sys_irqenable(int *hook_id)

▶ Note that here hook_id should point to a variable with

the value returned by the kernel in
sys_irqsetpolicy()

That is, the kernel will unmask the IRQ line, upon request of
the DD.

18/20

Minix 3: Interrupt Sharing

▶ Minix 3 already includes its own Timer 0 IH
▶ By subscribing interrupts on IRQ line 0, the IH of your

driver will not replace the IH of the kernel

▶ Upon an interrupt generated by Timer 0, the kernel:

1. executes its own IH, and
2. notifies your driver

▶ This behavior stems from the need to share the interrupt

lines among devices

▶ In systems with the PIC (i8259), there are only 15 interrupt

lines available

▶ And many of them are actually hardwired, e.g. IRQ 0, which

means that they cannot be shared among devices

IMP Using two IH for the same device is seldom what you want

▶ But is just what we need for Lab 2.

19/20

Further Reading

▶ Lab 2 Handout, Section 4, The PC’s Interrupt Hardware
▶ 8259A- Interrupt Priority Controller- Data Sheet, by Intel
▶ Using Interrupts
▶ Lab 2 Handout, Subsection 5.2 (Minix 3) Interrupt Handling

20/20



---
# Document: 4kbd.pdf
---

Computer Lab: The PC’s Keyboard
2º L.EIC

Pedro F. Souto (pfs@fe.up.pt)

March 4, 2025

1/25

Contents

Lab 3 Overview

PC Keyboard Operation: Data Input

Lab3: kbd_test_scan()

The KBC Commands

Keyboard Programming/Configuration

Lab 3: kbd_test_poll()

Lab 3: kbd_test_timed_scan()

2/25

Lab 3: The PC’s Keyboard - Part 1

▶ Write functions:

int kbd_test_scan()
int kbd_test_poll()

that require programming the PC’s keyboard controller

▶ Compare interrupt driven-I/O with poll-based I/O
▶ Compare the number of sys_inb() kernel calls

▶ These functions are not the kind of functions that you can reuse

later in your project

▶ The idea is that you design the lower level functions (with the final

project in mind).

▶ Reusable code should be in different files from non-reusable code.

▶ What’s new?

▶ Interface with the KBC controller (i8042)
▶ In part 2:

▶ Handle interrupts from more than one device

3/25

Contents

Lab 3 Overview

PC Keyboard Operation: Data Input

Lab3: kbd_test_scan()

The KBC Commands

Keyboard Programming/Configuration

Lab 3: kbd_test_poll()

Lab 3: kbd_test_timed_scan()

4/25

PC Keyboard Operation: Data Input (1/2)

▶ The keyboard has its own controller chip (not shown): the

controller@KBD (C@KBD)

▶ When a key is pressed the C@KBD generates a scancode
(make code) and puts it in a buffer for sending to the PC

▶ Usually, a scancode is one byte long
▶ The same happens when a key is released

▶ Usually, the scancode when a key is released (break code)

is the make code of that key with the MSB set to 1
▶ The communication between the C@KBD and the PC is

via a serial line

▶ I.e. the bits in a byte are sent one after the other over a pair

of wires

5/25

IRQ10x640x60OUT_PORTOUT_BUFIN_PORTSTAT_REGI/Obusi8042(KBC)KeyboardIN_BUFPC Keyboard Operation: Data Input (2/2)

▶ On the PC side this communication is managed by the

keyboard controller (KBC)

▶ In modern PCs, the KBC is integrated in the motherboard’s

chipset

▶ When OUT_BUF (@ port 0x60) is empty:
1. The KBC signals that via the serial bus
2. The C@KBD sends the byte at the head of its buffer to the

KBC

3. The KBC puts it in the OUT_BUF
4. The KBC generates an interrupt by raising IRQ1

6/25

IRQ10x640x60OUT_PORTOUT_BUFIN_PORTSTAT_REGI/Obusi8042(KBC)KeyboardIN_BUFThe KBC Registers

▶ The KBC has two registers at port 0x60:

Input Buffer (IN_BUF) used for sending commands to the

keyboard (KBD commands)

▶ Not used in LCOM

Output Buffer used for receiving scancodes and ...

▶ And two registers at port 0x64

Status Register for reading the KBC state
Not named for writing KBC commands

▶ Apparently, this is not different from the IN_BUF at port 0x60
▶ The value of input line A2 is used by the KBC to distinguish

KBC commands from KBD commands the IN_BUF

7/25

IRQ10x640x60OUT_PORTOUT_BUFIN_PORTSTAT_REGI/Obusi8042(KBC)KeyboardIN_BUFStatus Register

▶ Both KBC’s input and output require reading the status register

Meaning (if set)
Parity error - invalid data

Bit Name
Parity
7
Timeout Timeout error - invalid data
6
Aux
5
INH
4
A2
3
SYS
2
IBF
1

Mouse data
Inhibit flag: 0 if keyboard is inhibited
A2 input line: irrelevant for LCOM
System flag: irrelevant for LCOM
Input buffer full
don’t write commands or arguments
Output buffer full - data available for reading

0

OBF

▶ Bits 7 and 6 signal an error in the (serial) communication

between the keyboard and the KBC
▶ Should check them in the IH
▶ Should always read the OUT_BUF, but discard in case of error
▶ If bit 1, the IBF, is set, do not write to the IN_BUF, i.e. to both

both ports 0x60 and 0x64.

8/25

Contents

Lab 3 Overview

PC Keyboard Operation: Data Input

Lab3: kbd_test_scan()

The KBC Commands

Keyboard Programming/Configuration

Lab 3: kbd_test_poll()

Lab 3: kbd_test_timed_scan()

9/25

Lab 3: kbd_test_scan() (1/2)

What Print the scancodes, both the makecode and the breakcode,

read from the KBC

▶ Should terminate when it reads the breakcode of the ESC key:

0x81

▶ The first byte of two byte scancodes is usually 0xE0

▶ This applies to both make and break codes

How Need to subscribe the KBC interrupts

▶ Upon an interrupt, read the scancode from the OUT_BUF

Note There is no need to configure the KBC

▶ It is already initialized by Minix
Issue Minix already has an IH installed

▶ Must be disabled to prevent it from reading the OUT_BUF

before your handler does it

Solution Use not only the IRQ_REENABLE but also the

IRQ_EXCLUSIVE policy in sys_irqsetpolicy(), i.e. use
IRQ_REENABLE|IRQ_EXCLUSIVE

10/25

Lab 3: kbd_test_scan() (2/2)
KBC interrupt subscription in exclusive mode;
driver_receive() loop (similar to that of lab 2)
Interrupt handler reads the bytes from the KBC’s OUT_BUF

▶ Should read only one byte per interrupt

▶ The communication between the keyboard and the KBC is too

slow

▶ Should check whether there was some error

▶ Need to read the status register

▶ Should not print the scancodes (not reusable)
▶ In the project, you may think about including the code that

maps the scancodes to a character code

▶ IH in Minix are usually out of the critical path
▶ They are executed with interrupts enabled and after issuing the EOI

command to the PIC

▶ In many systems this may not be appropriate. For example, in

Linux some DD break interrupt handling in two:
Top half which is in the critical path
Bottom half which is not in the critical path

11/25

Lab 3: Counting the number of sys_inb() calls

Why? To compare interrupt-driven I/O with poll-based I/O

Issue You do not want this feature in the project
Solution Use #ifdef for conditional compilation. Alternatives:

Use #ifdef before/after every sys_inb()/util_sys_inb()

call
#define LAB3
sys_inb(...);
#ifdef LAB3
cnt++;
#endif

Use wrapper function util_sys_inb()

▶ You already call it instead of sys_inb()
▶ Need only to increment counter, if LAB3 is defined

In both cases add line to Lab3’s Makefile

CPPFLAGS += -D LAB3

12/25

Contents

Lab 3 Overview

PC Keyboard Operation: Data Input

Lab3: kbd_test_scan()

The KBC Commands

Keyboard Programming/Configuration

Lab 3: kbd_test_poll()

Lab 3: kbd_test_timed_scan()

13/25

Keyboard-Related KBC Commands for PC-AT/PS2
▶ These commands must be written using address 0x64
▶ Arguments, if any, must be passed using address 0x60
▶ Return values, if any, are passed in the OUT_BUF

Command Meaning
0x20
0x60
0xAA

Read Command Byte
Write Command Byte
Check KBC (Self-test)

Args (A)/ Return (R)
Returns Command Byte
Takes A: Command Byte
Returns 0x55, if OK
Returns 0xFC, if error

0xAB
0xAD
0xAE

Check Keyboard Interface Returns 0, if OK
Disable KBD Interface
Enable KBD Interface

KBD Interface is the serial interface between the keyboard and

the KBC

▶ Disabling of the KBD interface is achieved by driving the

clock line low.

▶ There are several other KBC-commands related to the

mouse (and also to the keyboard)

14/25

(KBC “Command Byte”)

2
–

3
–

7
–

6
–

0
INT

1
INT2

5
DIS2

4
DIS
DIS2 1: disable mouse interface
DIS 1: disable keyboard interface
INT2 1: enable interrupt on OBF, from mouse;
INT 1: enable interrupt on OBF, from keyboard
- : Either not used or not relevant for Lab

Read Use KBC command 0x20, which must be written to 0x64
▶ But the value of the “command byte” must be read from

0x60

Write Use KBC command 0x60, which must be written to 0x64
▶ But the new value of the “command byte” must be

written to 0x60

15/25

Contents

Lab 3 Overview

PC Keyboard Operation: Data Input

Lab3: kbd_test_scan()

The KBC Commands

Keyboard Programming/Configuration

Lab 3: kbd_test_poll()

Lab 3: kbd_test_timed_scan()

16/25

KBC Registers: Summary

Status Register @ address 0x64
▶ Read the KBC state

Input Buffer @ either address 0x64 or address 0x60. Can be used

to write:
Commands to the KBC access via address 0x64;
Arguments of KBC commands access via address 0x60

Output Buffer @ address 0x60. Can be used to read:

Scandcodes both make and break, received from the keyboard;
Return values from KBC commands;

Note These addresses belong to the I/O address space

▶ Need to use IN/OUT assembly instructions or the library
functions sys_inb()/sys_outb() of the kernel API

17/25

Issuing a Command to the KBC

#define KBC_ST_REG
0x64
#define KBC_CMD_REG 0x64

while( 1 ) {

sys_inb(KBC_ST_REG, &stat); /* assuming it returns OK */
/* loop while 8042 input buffer is not empty */
if( (stat & KBC_ST_IBF) == 0 ) {

sys_outb(KBC_CMD_REG, cmd); /* no args command */
return 0;

}
delay(WAIT_KBC); // e.g. tickdelay()

}

Note 1 Cannot output to the 0x64 while the input buffer is full
Note 2 Code leaves the loop only when it succeeds to output

the data to the 0x64

▶ To make your code resilient to failures in the

KBC/keyboard, it should give up after “enough time” for
the KBC to send a previous command/data to the KBD.

18/25

Reading Return Value/Data from the KBC

#define KBC_OUT_BUF 0x60

while( 1 ) {

sys_inb(KBC_ST_REG, &stat); /* assuming it returns OK */
/* loop while 8042 output buffer is empty */
if( stat & KBC_OBF ) {

sys_inb(KBC_OUT_BUF, &data); /* ass. it returns OK */

if ( (stat &(KBC_PAR_ERR | KBC_TO_ERR)) == 0 )

return data;

else

return -1;

}
delay(WAIT_KBC); // e.g. tickdelay()

}

Note 1 Code leaves the loop only upon some input from the

KBC_OUT_BUF.

▶ It is not robust against failures in the KBC/keyboard
Note 2 Must mask IRQ1, otherwise the keyboard IH may run

before we are able to read the KBC_OUT_BUF

19/25

KBC Programming Issues

Interrupts If the command has a response, and interrupts are

enabled, the IH will “steal” them away from other code
▶ The simplest approach is to disable interrupts.

Timing KBD/KBC responses are not immediate.

▶ Code needs to wait for long enough, but not indefinitely

Concurrent Execution The C@KBD continuously scans the
KBD and may send scancodes, while your code is writing
commands to the KBC:

▶ How can you prevent accepting a scancode as a

response to a command?

▶ If all you need is to use KBC commands, then you can

disable the KBD interface

▶ If you also need to give KBD commands, then this is

harder

▶ But in Lab 3, we do not use KBD commands.

20/25

Contents

Lab 3 Overview

PC Keyboard Operation: Data Input

Lab3: kbd_test_scan()

The KBC Commands

Keyboard Programming/Configuration

Lab 3: kbd_test_poll()

Lab 3: kbd_test_timed_scan()

21/25

Lab 3: kbd_test_poll()
What? Read the scan codes by polling
How? Keep polling the status register (0x64), and, if OBF is set and

AUX is cleared, read the OB

▶ The function lcf_start() already disables keyboard

interrupts by the KBC (this also prevents Minix’s keyboard IH
from "stealing" the scan codes)

▶ Must enable interrupts by writing command byte before

exiting

▶ Should read the command byte before to restore it later

Hint Try to design a solution based on layers that allows you to issue

any KBC command, not just command 0x20/0x60
Bottom layer Functions that read/write the KBC registers. Deals

with the details of the KBC HW interface. E.g.:

▶ Checks the IBF flag before writing

Top layer Functions to issue either KBC commands

▶ Knows about the commands and the protocol, writing
parameters as necessary and waiting for responses

22/25

Contents

Lab 3 Overview

PC Keyboard Operation: Data Input

Lab3: kbd_test_scan()

The KBC Commands

Keyboard Programming/Configuration

Lab 3: kbd_test_poll()

Lab 3: kbd_test_timed_scan()

23/25

Lab 3: kbd_test_timed_scan(uint8_t idle)

What Similar to kbd_test_scan() except that process should

terminate, upon:
either release of the ESC key
or after idle seconds, during which no scancode is received

How Must subscribe interrupts both of the keyboard and the

timer/counter

12:
13:
14:
15:
16:
17:
18:
19:
20:
21:
22:
23:

▶ Must handle both interrupts in the "driver_receive() loop"

switch (_ENDPOINT_P(msg.m_source)) {
case HARDWARE: /* hardware interrupt notification */

if (msg.m_notify.interrupts & timer0_int_bit) { // Timer0 int?

... /* process Timer0 interrupt request

*/

}
if (msg.m_notify.interrupts & kbd_int_bit) { // KBD int?

... /* process KBD interrupt request

*/

}
break;

default:

break; /* no other notifications expected: do nothing */

}

▶ Must not change timer 0’s configuration

24/25

Further Reading

▶ IBM’s Functional Specification of the 8042 Keyboard
Controller (IBM PC Technical Reference Manual)

▶ W83C42 Data Sheet, Data sheet of an 8042-compatible

KBC

▶ Andries Brouwer’s The AT keyboard controller, Ch. 11 of

Keyboard scancodes

▶ Andries Brouwer’s Keyboard commands, Ch. 12 of

Keyboard scancodes (not relevant for Lab 3)

25/25



---
# Document: 5mouse.pdf
---

Computer Labs: The PS/2 Mouse
2º MIEIC

Pedro F. Souto (pfs@fe.up.pt)

March 13, 2025

1/17

Lab4: The PS/2’s Mouse

▶ Write functions:

int mouse_test_packet(uint32_t cnt);
int mouse_test_async(uint8_t idle_time)
int mouse_test_gesture(?????);

that require interfacing with the mouse, via the PC’s keyboard
controller

▶ These functions are not the kind of functions that you can reuse

later in your project

▶ The idea is that you design the lower level functions (with the final

project in mind).

▶ What’s new?

▶ Use the KBC controller (i8042) to interface with the mouse
▶ Process mouse interrupts
▶ (Handling multiple asynchronous interrupts)
▶ Use state machines

2/17

PS/2 Mouse Operation

▶ The mouse has its own controller chip, like the keyboard. It:

Detects events on the mouse

Pressing/releasing of the mouse buttons
Displacement of the mouse on the plane.
▶ It uses two 9-bit 2’s complement counters, one per direction
▶ That are reset every time the controller reports their value
▶ Some touchpads can be configured to report their absolute position
Reports these events to the KBC, by sending a 3-byte packet via

a serial line

▶ This protocol is the one also used in the communication

between the keyboard and the KBC

3/17

IRQ10x640x60OUT_PORTCTRL_REGIN_BUFOUT_BUFIN_PORTSTAT_REGI/Obusi8042(KBC)KeyboardMouseIRQ12PS/2 Mouse Data Packet
6
X Ovfl MSB Y Delta MSB X Delta

7
Y Ovfl

5

4

3
2
1 M.B.

1
R.B.

0
L.B.

Byte 1
Byte 2
Byte 3

X delta
Y delta

X MSB/Y MSB Relative displacement MSBit X/Y axis
X delta/Y delta Relative displacement 8 LS bits in the X/Y axis

since the previous packet

▶ X MSB and X delta form a 9-bit 2’s complement integer
X Ovfl/Y Ovfl Flag that the mouse displacement is too large to

be represented as a 9-bit 2-complement integer

M.B, R.B, L.B State of the middle, right and left buttons: 1 if

pressed.
▶ A scaling parameter in the mouse controller affects the value of

the counters reported by the mouse. There are 2 values:
1:1 In this case, the values reported are the counters values
2:1 In this case, the values reported are a function of the

counters values as determined by a table

4/17

PS/2 Mouse Operating Modes

Stream Mode The mouse sends the data packet at a (programmable)
maximum fixed rate to the KBC, as determined by “mouse events”,
i.e. mouse movements and changes in buttons state

Remote Mode The mouse sends data packets only upon request of

the KBC
▶ In either case, each of the bytes of the mouse data packet are put

in the KBC’s output buffer, and

▶ The KBC raises IRQ12 (i.e. IRQ4 of PIC 2)

▶ Once for each byte
▶ This can be enabled/disabled by writing in the command byte

▶ The mouse IH should read one byte per interrupt
▶ In remote mode it is easier not to use interrupts

5/17

Lab4: mouse_test_packet (1/2)
What Print the packets received from the mouse in stream mode

Details Should:

▶ Terminate after processing the given number of packets
▶ Display the packets contents in a human friendly way, by
LCF function (we provide it): mouse_print_packet()

How Need to subscribe the mouse interrupts

▶ Upon an interrupt, read the byte from the OUT_BUF

Note There is no need to configure the mouse

▶ It is already initialized by Minix

But Need to enable stream mode (see PS/2 Mouse commands)

▶ Minix disables stream mode in text mode
▶ Initially, can use mouse_enable_data_reporting() of

the LCF (i.e., provided by us)

Issue Minix already has an IH installed

▶ Disable it by subscribing the mouse interrupt with

IRQ_EXCLUSIVE policy

6/17

Lab4: mouse_test_packet (2/2)

KBC interrupt subscription in exclusive mode;
driver_receive() loop (similar to that of labs 2 and 3)
Interrupt handler reads the bytes from the KBC’s OUT_BUF

▶ Should read only one byte per interrupt

▶ Communication between the mouse and the KBC is too slow

▶ Must not call mouse_print_packet()

Packet Assembly Can use:

packet[] to store the packet bytes
counter to keep track of byte number

Synchronization Issues All 3 bytes must belong to the same packet

Challenge The bytes in a packet have no id
Hint Bit 3 of first byte of a packet is always set

▶ But this bit may also be set in other bytes of a packet

7/17

PS/2 Mouse-Related KBC Commands

Command Meaning
0x20
0x60
0xA7
0xA8
0xA9
0xD4

Read Command Byte
Write Command Byte
Disable Mouse
Enable Mouse
Check Mouse Interface Returns 0, if OK
Write Byte to Mouse

Args (A)/ Return (R)
Command byte (R)
Command byte (A)

Byte (A)

▶ 0xD4 commands the KBC to forward its argument to the mouse

without any interpretation

▶ These commands are for the KBC and must be written to port

0x64

▶ Arguments and return values are passed via port 0x60
▶ Do not forget to check the IBF bit in the STATUS_REG, before

writing to either port

8/17

(KBC “Command Byte”)

3
–

7
–

6
–

0
INT

4
DIS

1
INT2

5
DIS2

2
–
DIS2 1: disable mouse
DIS 1: disable keyboard
INT2 1: enable interrupt on OBF, from mouse;
INT 1: enable interrupt on OBF, from keyboard
- : Either not used or not relevant

Read Use KBC command 0x20, which must be written to port 0x64
Write Use KBC command 0x60, which must be written to port 0x64

9/17

Status Register

▶ Input from/output to KBC requires reading the status register

Meaning (if set)
Parity error - invalid data

Bit Name
Parity
7
Timeout Timeout error - invalid data
6
Aux
5
INH
4
A2
3

Mouse data
Inhibit flag: 0 if keyboard is inhibited
A2 input line: 0 data byte

1 command byte

2

1

0

SYS

IBF

OBF

System flag: 0 if system in power-on reset,
1 if system already initialized

Input buffer full
don’t write commands or arguments
Output buffer full - data available for reading

▶ Bits 5, Aux, indicates whether the data in the OUT_BUF is coming

from the Mouse (auxiliary device) or the keyboard

▶ Do not write to the IN_BUF (0x60) or the CTRL_REG (0x64),

if bit 1, i.e. the IBF, is set.

10/17

PS/2 Mouse Commands (1/4)

Commands passed as arguments of command 0xD4
Command
0xFF
0xFE
0xF6
0xF5

Function
Reset
Resend
Set Defaults
Disable (Data Reporting)

Description/Comments
Mouse reset
For serial communications errors
Set default values
In stream mode, should be sent
before any other command
In stream mode only
Sets state sampling rate
Send data on request only
Send data packet request
Send data on events
Get mouse configuration (3 bytes)

Acceleration mode
Linear mode

0xF4
0xF3
0xF0
0xEB
0xEA
0xE9
0xE8
0xE7
0xE6

Enable (Data Reporting)
Set Sample Rate
Set Remote Mode
Read Data
Set Stream Mode
Status Request
Set Resolution
Set Scaling 2:1
Set Scaling 1:1

Note 1 Arguments of these commands, if any, must also be passed

as arguments of command 0xD4

Note 2 Responses to these commands, if any, are put in the KBC’s

OUT_BUF and should be read via port 0x60

11/17

PS/2 Mouse Commands (2/4)

▶ Each of these commands is sent to the mouse, it is not

interpreted by the KBC

▶ The command is passed as argument of command 0xD4
▶ Arguments, if any, of a command must also be passed as

arguments of command 0xD4 of the KBC

▶ Command 0xD4 is: “Write Byte to Mouse”

▶ In response to all bytes it receives

either commands (except for the resend command, 0xFE) or their
arguments

the mouse controller sends an acknowledgment byte:
ACK (0xFA) if everything OK
NACK (0xFE) if invalid byte (may be because of a serial

communication error)

ERROR (0xFC) second consecutive invalid byte

▶ The acknowledgment byte for each byte written as argument of
command 0xD4 is put in the KBC’s OUT_BUF and should be
read via port 0x60

12/17

PS/2 Mouse Commands (3/4)

Not representing polling of STATUS_REG for IBF/OBF

13/17

CPUCTRLINBOUTBIN/OUTMOUSE0xD4CMDCMDACK0xD4Par1Par1ACKACKACKPS/2 Mouse Commands (4/4)

▶ Note that:

“When the host gets an 0xFE response, it should retry the
offending command. If an argument byte elicits an 0xFE response,
the host should retransmit the entire command, not just the
argument byte.”

Synaptics TouhcPad Interfacing Guide, pg. 31

IMPORTANT The acknowledgment byte is not the response to the

command.

▶ For commands that elicit one response, the mouse controller
will send it after the acknowledgment to the last byte of the
command (including the args, if any).

14/17

Lab 4: mouse_test_async()

▶ Similar to kbd_test_timed_scan(), of Lab 3
▶ Must subscribe also the Timer 0 interrupts

15/17

Mouse: Some Success Hints

▶ In the IH, read only one byte from the KBC
▶ No need to ckeck the OBF or the AUX bits
▶ The KBC uses different IRQ lines for the keyboard and the mouse

▶ Assemble packets using:

▶ A 3-byte array for the mouse packet
▶ The index of the current position of the array

▶ Make sure that when you display the 3-bytes, they all belong to

the same packet.

▶ Do not forget:

If the device is in Stream mode (the default) and has been enabled
with an Enable (0xF4) command, then the host should disable the
device with a Disable (0xF5) command before sending any other
command.

Synaptics TouchPad Interfacing Guide, pg. 33

▶ Finally:

▶ If a byte is left in the OUT_BUF, the KBC will not generate further

interrupts

16/17

Further Reading

▶ Synaptics Synaptics TouchPad Interfacing Guide, 2nd Ed. (Read

only Subsections 3.2.3 thru 3.7.1, except Section 3.5 and
Subsection 3.6.2.)

▶ Andries Brouwer’s The PS/2 Mouse, Ch. 13 of Keyboard

scancodes

▶ Adam Chapweske’s The PS/2 Mouse Interface

17/17



---
# Document: 6events.pdf
---

Computer Labs: Event Driven Design
2º MIEIC

Pedro F. Souto (pfs@fe.up.pt)

March 14, 2024

1/17

Contents

Event Driven Design

State Machines

Event Handling

2/17

Events and I/O

Event An event is a change in the state

▶ Virtually all I/O processing is driven by events

▶ Whether events are detected by interrupts or by polling
▶ Even video graphics output may depend on events

(synchronization with the vertical “movement” to avoid visual
artifacts)

▶ All labs so far, have been driven by I/O events
▶ Your project will also be event driven:

▶ Its execution will depend on events generated by the I/O devices

▶ Whether you use polling or interrupts for detecting these events.

3/17

Event Driven Design

▶ Event driven design is characterized by:

▶ A flow control that is determined by the environment rather than

the program itself

▶ Code that is executed reactively in response to events that may

occur asynchronously with program execution

▶ Event driven design is common in:
▶ Graphical user interfaces (GUI)
▶ Games
▶ Communications/network software
▶ Embedded systems

4/17

Simple Event Driven Design

Events The types of events that the different components of the

system have to handle

Event Queues That provide the necessary buffering so that handling

of an event may occur asynchronously to its occurrence

Event Handlers That process each type of event

Dispatchers That monitor the event queues and call the appropriate

event handlers

▶ May be implemented as a simple loop that checks for events

5/17

Event Driven Design and Minix 3 DD Design

▶ We can find these elements of event driven design in the pattern

used in the design of interrupt driven Minix 3 DDs

}
if (is_ipc_notify(ipc_status)) { /* received notification */

/* Get a request message. */
if ( driver_receive(ANY, &msg, &ipc_status) != 0 ) {
printf("driver_receive failed with: %d", r);
continue;

5: while( 1 ) { /* You may want to use a different condition */
6:
7:
8:
9:
10:
11:
12:
13:
14:
15:
16:
17:
18:
19:
20:
21:

switch (_ENDPOINT_P(msg.m_source)) {
case HARDWARE: /* hardware interrupt notification */

} else { /* received a standard message, not a notificatio

... /* process it */

}
break;

default:

}

break; /* no other notifications expected: do nothing */

if (msg.m_notify.interrupts & irq_set) { /* subscribed interrupt */

6/17

Contents

Event Driven Design

State Machines

Event Handling

7/17

Event Driven Design and State Machines

▶ For other than simple designs, it is very helpful to use state

machines in combination with event driven design

▶ A state machine is useful when event handling depends on the

state of a process

▶ A state machine is itself event driven

▶ The transition from one state to another depends on the

occurrence of an input event

8/17

Lab 4: test_gesture() (2015/2016 version)

▶ The program should exit when the user "draws" a vertical line ,

while pressing down the right button

▶ Need some "tolerance" to make it easy to test

▶ You can ignore some events, namely those related to other

buttons.

▶ This year the gesture to detect will be different:

∧

9/17

Lab 4 (15/16): test_gesture() State Machine (1/2)

Cur. State
I(nitial)
D(rawing)
D(rawing)
D(rawing)

Input
RDOWN
VERT_LINE
RUP
HOR_TOLERANCE

Next State
D(rawing)
C(omplete)
I(nitial)
D(rawing)

Output

Exit

Reset length

RDOWN Right button has been pressed
RUP Right button has been released
VERT_LINE Vertical line with desired length drawn
HOR_TOLERANCE Horizontal tolerance exceeded

▶ This is somewhat high-level

▶ You need to detect the events from the packets received from

the mouse

▶ You can use other state machines

10/17

RDOWNRUPVERTLINE/EXITIDCHORTOLERANCE/RESETLENLab 4 (15/16) test_gesture() - State Machine (2/2)

typedef enum {INIT, DRAW, COMP} state_t;
typedef enum {RDOW, RUP, MOVE} ev_type_t;
void check_hor_line(event_t *evt) {

static state_t st = INIT; // initial state; keep state
switch (st) {
case INIT:

if( evt->type == RDOWN )

state = DRAW;

break;
case DRAW:

if( evt->type == MOVE ) {

[...] // need to check if events VERT_LINE

or HOR_TOLERANCE occur

} else if( evt->type == RUP )

state = INIT;

break;

default:

break;

}

}

▶ This is rather high-level

▶ You need to add code to detect the events

▶ This can be done with other state machines

11/17

(State Machines)

▶ This state machine is an example of a Mealy Machine, drawn “a

la DFA”:

▶ A state machine where the output depends not only on the state

but also on the input event

▶ An alternative state machine is the Moore Machine:

▶ A state machine where the output depends only on the state.
▶ This usually leads to extra states

▶ In this (simple) case the two machines are structurally equal
▶ They are essentially equivalent, but in an event-driven design the
implementation of a Mealy machine is more straightforward:

▶ For each state, when a relevant event occurs, just produce the
output (if any) and change the state (this is a special output)
▶ A relevant event may not be a raw event generated by an input

device:

▶ “Raw” events generated by mice are the reception of packet bytes,

not the change in the state of mouse buttons

▶ This is the opposite of digital circuit design:

▶ In HW, it is easier to implement Moore machines than Measly

machines

12/17

Contents

Event Driven Design

State Machines

Event Handling

13/17

Event Processing

▶ I/O devices’ events are processed by the corresponding interrupt

handlers

▶ The IHs may be

Application Dependent For example, the mouse IH not only

receives the mouse packets, but also detects the exit sequence

Application Independent The mouse IH just receives the mouse

packets. The exit sequence is detected by application
dependent code.

▶ Need to define an application dependent event handler
▶ Need to specify how the IH “communicates” with this event

handler

▶ How the data received from the mouse is passed to the event

handler?

▶ When is the event handler executed?

14/17

Application Independent vs Application Dependent IH

In General

▶ Can be reused

▶ Operating systems IH is independent of applications

▶ Introduces a level of indirection

▶ May add flexibility
▶ May be more responsive (app. indep. IHs are shorter)
▶ Requires more code (overall)
▶ Has higher overhead

In Minix 3 Labs and Project
driver_receive() is a blocking call

▶ Application dependent processing must be done in the same

iteration loop as application independent processing

▶ It is not possible to delay application dependent processing until

there are no interrupts to handle

▶ It does not afford as much flexibility as in the general case

▶ This is not an issue for ordinary Minix 3 DDs

15/17

Minix 3 and Application Independent IHs

if (msg.NOTIFY_ARG & irq_set) { /* subscribed interrupt */

}
if (is_ipc_notify(ipc_status)) { /* received notification */

switch (_ENDPOINT_P(msg.m_source)) {
case HARDWARE: /* hardware interrupt notification */

/* Get a request message. */
if ( driver_receive(ANY, &msg, &ipc_status) != 0 ) {
printf("driver_receive failed with: %d", r);
continue;

5: while( 1 ) { /* You may want to use a different condition */
6:
7:
8:
9:
10:
11:
12:
13:
14:
15:
16:
17:
18:
19:
20:
21:
22:
23:
24:
25:
26:

} else { /* received a standard message, not a notificatio
...
}
/* Now, do application dependent event handling */
if ( event & MOUSE_EVT ) {

}
if ( event &

... /* process it */

handle_mouse();

...
}

}

16/17

Further Reading

▶ Máquinas de Estado em C

17/17



---
# Document: 6fptr.pdf
---

Computer Labs: C Function Pointers
2º MIEIC

Pedro F. Souto (pfs@fe.up.pt)

March 14, 2024

1/11

Function Pointers

▶ C supports pointers to functions, which can be:

▶ assigned;
▶ placed in arrays;
▶ members of structs or unions;
▶ passed to functions;
▶ returned by functions

▶ int (*fp)(int); declares fp as a pointer to a function that

takes an integer as argument and returns an integer

▶ Let int foo(int); be such a function
▶ Then:

fp = foo;
initializes fp to point to foo()

▶ And:

n = (*fp)(i);
invokes the function pointed to by fp, foo, with argument i and
assigns the return value to variable n

2/11

Function Pointers Application: Event Dispatching

▶ One simple implementation of event dispatching is:
▶ to use a switch instruction on the event type;
▶ to call, in each case clause, the corresponding event handler

switch(ev) { // identify event
case EV0:

ev0_handler(); // call handler
break;

...

▶ An alternative implementation is similar to vectored interrupts:
▶ use a table (array) of (pointers to) event handlers (functions);
▶ index that table to jump to the handler;

void (*eht[])(void) = {ev0_handler, ev1_handler, ...};
...
(*eht[ev])();

// index into table and call handler

▶ Of course, the event handlers may take arguments

3/11

Function Pointers Application:

Event Dispatching in State Machines

▶ We can use the state as an argument to the event handler:

typedef enum {ST0, ST1, ST2, ..} state_t;
void (*eht[])(state_t) = {ev0_handler, ev1_handler, ...};
state_t st;
...
(*eht[ev])(st);

// index into table and call handler

▶ Alternatively, we can use as a table a two-dimensional array,
which is indexed not only by the event but also by the state
void (*eht[][])(void) = {{s0e0_handler, ...},

{s1e0_handler, ...},...};

...
(*eht[st][ev])();

// index into table and call handler

4/11

Further Reading

▶ Máquinas de Estado em C

5/11

Function Pointers Application: Menus

6/11

Class Menu: A class for building menus

#include "menu.h"
#include <stdio.h>

void e1() {printf("-e1-\n");
void se1() {printf("-se1-\n");
void sse1() {printf("-sse1-\n");

void e2() {printf("-e2-\n");
void se2() {printf("-se2-\n");
void sse2() {printf("-sse2-\n");

int main() {

Menu *ssm1 = newMenu("Sub Sub Menu 1");
menuAddFunction(ssm1, "Sub Sub Entry 1", sse1);
menuAddFunction(ssm1, "Sub Sub Entry 2", sse2);

Menu *sm1 = newMenu("Sub Menu 1");
menuAddFunction(sm1, "Sub Entry 1", se1);
menuAddFunction(sm1, "Sub Entry 2", se2);
menuAddMenu(sm1, "Sub Sub Menu 1", ssm1);

Menu *m1 = newMenu("Main Menu");
menuAddFunction(m1, "Entry 1", e1);
menuAddFunction(m1, "Entry 2", e2);
menuAddMenu(m1, "Sub Menu 1", sm1);

menuPost(m1);
menuDelete(m1); menuDelete(sm1); menuDelete(ssm1);
return 0;

}

7/11

Class Menu: menu.h

struct menu;
struct menu_entry;
// handy typedefs
typedef struct menu Menu;
typedef struct menu_entry MenuEntry;
struct menu {

char *title;
MenuEntry **entries;
int num
int size;

// menu title
// pointer to array of menu entries
// number of menu entries
// array capacity

};
struct menu_entry {
char *desc;
Menu *subMenu;
void (*func)();

// menu entry descriptive text
// non-NULL if entry is submenu
// non-NULL if entry selection calls a function

};
Menu * newMenu(char *title); // the "constructor"
void menuDelete(Menu *m);
// Other "methods"
void menuAddFunction(Menu *m, char *desc, void (*f)(void));
void menuAddMenu(Menu *m, char *desc, Menu *sm);
void menuPost(Menu *m);

// activate the menu

// destructor

8/11

Class Menu: menu.c (1/2)

Menu *newMenu(char *title) {

menu *m = malloc(sizeof(Menu)); // missing error checking
m->title;
m->num = m->size = 0;
menuAdjust(m); // if needed increase entries[] size
return m;

}
void menuAddFunction(Menu *m, char desc, void (*func)()) {

MenuEntry *me = malloc(sizeof(MenuEntry));
me->desc = desc;
me->func = func; me->subMenu = NULL;
m->entries[m->num++] = me;
menuAdjust(m);

}
void menuAddMenu(Menu *m, char *desc, Menu *sm) {
MenuEntry *me = malloc(sizeof(MenuEntry));
me->desc = desc;
me->subMenu = sm ; me->func = NULL;
m->entries[m->num++] = me;
menuAdjust(m);

}

9/11

Class Menu: menu.c (2/2)

void menuPost(Menu *m) {

int choice;
char *su = saveUnder(m); // save area under new menu
while(1) {

// draw menu and accept user choice
choice = selectEntry(m);
if( choice == 0 ) {

restoreUnder(m, su);
return;

}
if( m->entries[choice-1]->fun != NULL )

(*(m->entries[choice-1]->fun))(); // call handler

else // if( m->entries[choice-1]->subMenu != NULL )

menuPost(m->entries[choice-1]->subMenu); // activate sub-menu

}

}
//draw menu, accept user choice
// return index of selected entry (
static int selectEntry(Menu *m) {

...

}

10/11

Thanks to:

I.e. shamelessly translated material on menus by:
▶ João Cardoso (jcard@fe.up.pt)

11/11



---
# Document: 7C4lab5.pdf
---

Computer Lab: C for Lab 5
2º L.EIC

Pedro F. Souto (pfs@fe.up.pt)

April 4, 2024

1/13

Contents

More on C Pointers

Lab5 functions

Anonymous structs/unions

2/13

C Pointers

▶ A C pointer is a data type whose value is a memory address.

▶ Program variables are stored in memory
▶ Other C entities are also memory addresses
▶ C provides two basic operators to support pointers:
& to obtain the address of a variable. E.g.

p = &n; /* Initialize pointer p with

the address of variable n */

* to dereference the pointer, i.e. to read/write the memory

positions it refers to.

*p = 8; /* Assign the value 8 to memory position

▶ To declare a pointer (variable), use the * operator:

whose address is
the value of p (variable n) */

int *p; /* Variable/pointer p points to integers or

the value pointed to by p is of type int */

▶ Use of pointers in C is similar to the use of indirect addressing

in assembly code, and as prone to errors.

3/13

C Pointers and Arrays

▶ The elements of an array are stored in consecutive memory

positions

▶ In C, the name of an array is the address of the first element

of that array:

int a[5];
p = a;
p = & (a[0]); /* same as above */

/* set p to point to the first element */

▶ C supports pointer arithmetic – meaningful only when used
with arrays. E.g. to iterate through the elements of an array
using a pointer:

for( i = 0, p = a; i < 5; i++, p++) {

...

}

or, without using variable i:

for( p = a; p-a < 5; p++) {

...

}

IMP: Pointer p must be declared to point to variables of the
type of the elements of array a.

4/13

C Pointers and Pointer Arithmetic: vg_fill()

▶ Actually, pointer arithmetic may be used when we want to
access a collection of data items of the same type that are
layed consecutively in memory. E.g., the pixels in VRAM in
graphics mode.

static void *video_mem; /* Address to which VRAM is mapped */
static unsigned hres;
static unsigned vres;

/* Frame horizontal resolution */
/* Frame vertical resolution */

void vg_fill(uint32_t color) {

int i;
uint32_t *ptr;
ptr = video_mem;

/* Assuming 4 byte per pixel */

for(i = 0; i< hres*vres; i++, ptr++) {

*ptr = color;

/* Handle a pixel at a time */

▶ Variables video_mem, etc. are global, but static
▶ ptr++ takes advantage of pointer arithmetic (here adds 4,

because each uint32_t takes 4 bytes)

5/13

Contents

More on C Pointers

Lab5 functions

Anonymous structs/unions

6/13

video_test_rectangle()

▶ Draw a rectangle on the screen in the desired mode

int video_test_rectangle(uint16_t mode, uint16_t x, uint16_t y,

uint16_t width, uint16_t height, uint32_t color)

▶ Need to handle different graphical modes, i.e. different:

Resolution both horizontal and vertical
Bits per pixel And color models

Indexed color modes also called packed-pixel by VBE, appear

to have only 8 bits per pixel

Direct color modes with a different number of bits per pixel
▶ And sometimes, the number of bits per component may be
different, even if the number of bits per pixel is the same.
▶ These affect the offset of 1) the memory location of a pixel, wrt
the frame-buffer base address, or of 2) the RGB components.

▶ The goal is that your code be parameterizable so that it can

easily handle these differences

▶ To facilitate testing, we suggest you use (see handout):

vg_draw_hline(uint16_t x, uint16_t y, uint16_t len, uint32_t color)

vg_draw_rectangle(uint16_t x, uint16_t y, uint16_t width, uint16_t height, uint32_t color)

7/13

Changing Pixel Values in Video RAM (1/2)

▶ Modes that use 4 bytes per pixel, are easy to handle
▶ Check the code for vg_fill(), two slides before

▶ So are modes that use 2 or 1 byte per pixel

▶ Can use uint16_t or uint8_t, respectively

Challenge what about modes that use 3 bytes?

▶ Compilers available in Minix do not have uint24_t

Solutions

Use memcpy() "copy memory area"

#include <string.h>

void *memcpy(void *dest, const void *src, size_t n);

Use a struct

typedef struct{

uint8_t comp[3];

} rgb_8_8_8_t;

8/13

Padding and Alignment

Issue C compilers layout data types in memory with the goal of

making accesses faster

▶ Most ISA require data types to be aligned for faster access.

uint16_t values start on even addresses;
uint32_t values on addresses that are divisible by 4
But, sometimes, memory is at a premium, and you want to pack
data as tight as possible. E.g.

▶ In VBE most data structures are packed to save memory
Thus, simply defining a C struct with one member per parameter
with an appropriate type may not be enough.

Solution Use #pragma pack

▶ Must also reset to the default by adding after the structure:

#pragma options align=reset

▶ Alternatively you can also use GCC’s

__attribute__((packed)) , which is also supported by
clang

9/13

Packing in vbe_mode_info_t

#pragma pack(1)
typedef struct {

uint16_t ModeAttributes;
[...]
uint16_t XResolution;
uint16_t YResolution;
[...]
uint8_t BitsPerPixel;
[...]
uint8_t RedMaskSize;
uint8_t RedFieldPosition;
[...]
uint8_t RsvdMaskSize;
uint8_t RsvdFieldPosition;
[...]
uint32_t
[...]

PhysBasePtr;

} vbe_mode_info_t;
#pragma options align = reset

For more info: The Lost Art of Structure Packing, Eric S. Raymond

10/13

Packing in video_test_pattern()

Purpose to learn how to change the
color components in the different
modes

Indexed modes instead of color use

the color pallette index:

index(row,col) = (first + (row * no_rectangles + col) * step) % (1 << BitsPerPixel)

In mode 0x105, when you pick the arguments remember that all
colors in the pallette with an index larger than 63 are black

Direct modes in this case you have to set each of the color

components using:
R(row, col) = (R(first) + col * step) % (1 << RedScreeMask)
G(row, col) = (G(first) + row * step) % (1 << GreenScreeMask)

B(row, col) = (B(first) + (col + row) * step) % (1 << BlueScreeMask)

Hint Call function that you should implement for

video_test_rectangle():
int vg_draw_rectangle(uint16_t x, uint16_t y, uint16_t width,

uint16_t height, uint32_t color)

11/13

color(0,0)color(0,1)color(0,2)color(0,3)color(1,0)color(1,1)color(1,2)color(1,3)color(2,0)color(2,1)color(2,2)color(2,3)color(3,0)color(3,1)color(3,2)color(3,3)Contents

More on C Pointers

Lab5 functions

Anonymous structs/unions

12/13

(Anonymous) Unions with Anonymous Structs
typedef struct reg86 {

union {

struct { /* 32-bit (double word) access*/

[...]

};
struct { /* 16-bit (word) access */

[...]

};
struct { /* 8-bit (byte) access */

/* Interrupt number (input only) */
/* unused */
/* unused */
/* unused */

u8_t intno;
u8_t : 8;
u16_t : 16;
[...]
u8_t al, ah; /* 8-bit general registers */
u16_t : 16;
u8_t bl, bh; /* 8-bit general registers */
u16_t : 16;
u8_t cl, ch; /* 8-bit general registers */
u16_t : 16;
u8_t dl, dh; /* 8-bit general registers */
[...]

/* unused */

/* unused */

/* unused */

/* unused */

};

};

} reg86_t;

Why the outer struct? "Better for forward declarations" (Kees J.Bot)

13/13



---
# Document: 7video.pdf
---

Computer Labs: Lab5
Video Card in Graphics Mode
2º LEIC

Pedro F. Souto (pfs@fe.up.pt)

March 22, 2024

1/34

Contents

Graphics Adapter/Video Card

Video Card in Graphics Mode

Lab 5 (Part 1)

BIOS and VBE

Accessing VRAM

2/34

Graphics Adapter/Video Card

GPU Earlier known as the Graphics Controller:

▶ Controls the display hardware (CRT vs. LCD)
▶ Performs 2D and 3D rendering algorithms, offloading the

CPU and accelerating graphics applications

BIOS ROM/Flash ROM/Flash Memory with firmware. Includes

code that performs some standardized basic video I/O
operations, such as the Video BIOS Extension (VBE)

Video RAM Stores the data that is rendered on the screen.
▶ It is acessible also by the CPU (at least part of it)

3/34

GraphicsProcessingUnit(GPU)BIOSROM/FlashVideoRAMBusAdapterVideo Modes

Text Mode

▶ Mode used by Minix 3 by default

Graphics Mode

▶ Mode you will use in Lab 5

4/34

PC’s Graphics Adapter Text Modes

▶ Used to render mostly text
▶ Abstracts the screen as a matrix of characters (row x cols)

▶ E.g. 25x80, 25x40, 50x80, 25x132
▶ Black and white vs color (16 colors)

5/34

80columns25linesHello,World!Contents

Graphics Adapter/Video Card

Video Card in Graphics Mode

Lab 5 (Part 1)

BIOS and VBE

Accessing VRAM

6/34

Video Card in Graphics Mode

▶ The screen is abstracted as a matrix of points, or pixels

▶ With HRES pixels per line
▶ With VRES pixels per column

▶ For each pixel, the VRAM holds its color

7/34

HRESpixelsVRESpixelsVRAMHow Are Colors Encoded? (1/2)

▶ Most electronic display devices use the RGB color model

▶ A color is obtained by adding 3 primary colors – red, green, blue –

each of which with its own intensity

▶ This model is related to the physiology of the human eye
▶ One way to represent a color is to use a triple, with a given

intensity per primary color

▶ Depending on the number of bits used to represent the intensity of

each primary color, we have a different number of colors

▶ E.g., if we use 8 bits per primary color, we are able to represent

224 = 16777216 colors

8/34

How Are Colors Encoded? (2/2)

Direct-color mode Store the color of each pixel in the VRAM
▶ For 8 bits per primary color, if we use a resolution of

1024 × 768 we need 3 MB (assuming 4 bytes per pixel)

Indexed color Rather than storing the color per pixel, it stores an

index into a table – the palette/color map – with the definition, i.e.
the intensity of the 3 primary colors, of each color

▶ With an 8 bit index we can represent 256 colors, each of which

may have 8 bits per primary color

▶ By changing the palette it is possible to render more than 256

colors

▶ In the lab you’ll use a palette with up to 256 colors, whose default

initialization uses only 64 colors

9/34

Memory Models

▶ The memory model determines how video memory is

organized, i.e., where the value of each pixel is stored in
VRAM

▶ Different graphics modes use different memory models
▶ The simplest mode, and the one that will be used in the

lab, is linear mode:

All we need to know is:

▶ The base address of the frame buffer
▶ The coordinates of the pixel
▶ The number of bytes used to encode the color

10/34

HRESpixelsVRESpixelscolor(0,0)color(1,0)color(Hres-1,0)color(0,1)Contents

Graphics Adapter/Video Card

Video Card in Graphics Mode

Lab 5 (Part 1)

BIOS and VBE

Accessing VRAM

11/34

Lab5: Video Card in Graphics Mode - Part 1

▶ Write a set of functions:

void video_test_init(unsigned short mode,

unsigned short delay)

int video_test_rectangle(uint16_t mode, uint16_t x,

uint16_t y, ...)
int video_test_pattern(uint16_t mode, uint16_t no_rectangles,

uint32_t first)

to set the screen to graphics mode and to display on the screen
what is requested
▶ Essentially you have to:

1. Configure the video card for the desired graphics mode
▶ Minix 3 boots in text mode, not in graphics mode

2. Write to VRAM to display on the screen what is requested

▶ Map VRAM to the process’ address space

3. Reset the video card to the text mode used by Minix
▶ You need only to call a function that we provide you

12/34

Video Card Configuration (video_test_init())

Problem How do you configure the desired graphics mode?

NO Solution Read/write directly the GPU registers

▶ GPU manufacturers usually do not provide the details

necessary for that level of programming

Solution Use the VESA Video Bios Extension (VBE)

13/34

Contents

Graphics Adapter/Video Card

Video Card in Graphics Mode

Lab 5 (Part 1)

BIOS and VBE

Accessing VRAM

14/34

PC BIOS

▶ Basic Input-Output System is:

1. A firmware interface for accessing PC HW resources
2. The implementation of this interface
3. The non-volatile memory (ROM, more recently flash-RAM)

containing that implementation
▶ It is used mostly when a PC starts up

▶ It is 16-bits: even IA-32 processors start in real-mode
▶ It is used essentially to load the OS (or part of it)
▶ Once the OS is loaded, it usually uses its own code to

access the HW not the BIOS

▶ Nowadays, most PCs use the "Unified Extensible Firmware

Interface" (UEFI)

15/34

BIOS Calls

▶ Access to BIOS services is via the SW interrupt instruction

INT xx

▶ The xx is 8 bit and specifies the service.
▶ Any arguments required are passed via the processor

registers

▶ Standard BIOS services:

Interrupt vector (xx) Service

10h
11h
12h
16h

video card
PC configuration
memory configuration
keyboard

16/34

BIOS Call: Example

▶ Set Video Mode: INT 10h, function 00h

; set video mode

MOV AH, 0
MOV AL, 3
INT 10h

; function (set video mode)
; text, 25 lines X 80 columns, 16 colors

17/34

How to make a BIOS Call in Minix 3.1.x?

Problem

▶ The previous example is in real address mode
▶ Minix 3 uses protected mode with 32-bit

Solution

▶ Use Minix 3 kernel call SYS_INT86

“Make a real-mode BIOS call on behalf of a user-space
device driver. This temporarily switches from 32-bit
protected mode to 16-bit real-mode to access the BIOS
calls.”

18/34

How to make a BIOS Call in Minix 3.4.x?

Problem

▶ Kernel call SYS_INT86 was droped in Minix 3.2

Solution

▶ Pedro Silva has added this kernel call to Minix 3.4.0rc6, by
porting libx86emu, a small library that emulates some
key x86 instructions.

▶ Essentially, we can use sys_int86 in Minix 3.4.x, as we

did in Minix 3.1.8.

▶ The implementation though is at user level.

19/34

BIOS Call in Minix 3: Example

#include <machine/int86.h> // /usr/src/include/arch/i386
int vg_exit() {

reg86_t reg86;

reg86.intno = 0x10;
reg86.ah = 0x00;
reg86.al = 0x03;

if( sys_int86(&reg86) != OK ) {

printf("vg_exit(): sys_int86() failed \n");
return 1;

}
return 0;

}

▶ reg86_t is a struct with a union of anonymous structs that

allow access the IA32 registers as

▶ 8-bit registers
▶ 16-bit registers
▶ 32-bit registers

▶ The names of the members of the structs are the standard

names of IA-32 registers.

20/34

Video BIOS Extension (VBE)

▶ The BIOS specification supports only VGA graphics modes

▶ VGA stands for Video Graphics Adapter
▶ Specifies very low resolution: 640x480 @ 16 colors and

320x240 @ 256 colors

▶ The Video Electronics Standards Association (VESA)

developed the Video BIOS Extension (VBE) standards in
order to make programming with higher resolutions
portable

▶ Early VBE versions specify only a real-mode interface
▶ Later versions added a protected-mode interface, but:
▶ In version 2, only for some time-critical functions;
▶ In version 3, supports more functions, but they are optional.

▶ Unfortunately, VirtualBox does not support the protected

mode interface

21/34

VBE INT 0x10 Interface

▶ VBE still uses INT 0x10, but to distinguish it from basic

video BIOS services

▶ AH = 4Fh - BIOS uses AH for the function
▶ AL = function

▶ VBE graphics mode 105h, 1024x768@256, linear mode:

reg86_t r;
r.ax = 0x4F02; // VBE call, function 02 -- set VBE mode
r.bx = 1<<14|0x105; // set bit 14: linear framebuffer
r.intno = 0x10;
if( sys_int86(&r) != OK ) {

printf("set_vbe_mode: sys_int86() failed \n");
return 1;

}

You should use symbolic constants.

22/34

video_test_rectangle()

▶ Draw a rectangle on the screen in the desired mode

int video_test_rectangle(uint16_t mode, uint16_t x, uint16_t y,

uint16_t width, uint16_t height, uint32_t color)

▶ The LCF can test your code for different graphical modes, i.e.

different:
Resolution both horizontal and vertical
Bits per pixel and color models

Indexed color modes also called packed-pixel by VBE,

appear to have only 8 bits per pixel

Direct color modes May use a different number of bits per

pixel

▶ And sometimes, the number of bits per component may be
different, even if the number of bits per pixel is the same.

▶ These affect the offset, with respect to the frame-buffer base

address, of the memory location with the color value of a pixel,
or of one of its RGB components.

▶ The goal is that your code be parametric, so that it can easily

handle these differences

23/34

Contents

Graphics Adapter/Video Card

Video Card in Graphics Mode

Lab 5 (Part 1)

BIOS and VBE

Accessing VRAM

24/34

Mapping the Linear Frame Buffer

▶ Before you can write to the frame buffer.

1. Obtain the physical memory address

1.1 Use vbe_get_mode_info() that we provide as part of

the LCF

▶ This function retrieves information about the input VBE
mode, including the physical address of the frame buffer

1.2 Should provide your own implementation, using VBE

function 0x01 Return VBE Mode Information, once
everything else has been completed.

2. Map the physical memory region into the process’ (virtual)

address space

25/34

HRESpixelsVRESpixelscolor(0,0)color(1,0)color(Hres-1,0)color(0,1)int vbe_get_mode_info(uint16_t mode, vbe_mode_info_t *vmi_p)

▶ Returns information on the input VBE mode, including screen

dimensions, color depth and VRAM physical address.

▶ Initializes packed vbe_mode_info_t structure passed as an

address with the VBE information on the input mode, by
calling VBE function 0x01, Return VBE Mode Information, and
copying the ModeInfoBlock struct returned by that function.

Arguments

mode VBE mode whose information should be returned, e.g.

0x105

vmi_p address of a vbe_mode_info_t struct that will be

initialized by vbe_get_mode_info(). All you need is just:

▶ Declare a variable of that type
▶ Use its address as argument

Return Value 0 on success, non-zero, otherwise

26/34

vbe_mode_info_t

#pragma pack(1)

typedef struct {

uint16_t ModeAttributes;
[...]
uint16_t XResolution;
uint16_t YResolution;
[...]
uint8_t BitsPerPixel;
[...]
uint8_t RedMaskSize;
uint8_t RedFieldPosition;
[...]
uint8_t RsvdMaskSize;
uint8_t RsvdFieldPosition;
[...]
uint32_t
[...]

PhysBasePtr;

} vbe_mode_info_t;

#pragma options align = reset

27/34

Implementation Notes

▶ You should call vbe_get_mode_info() only once and store

its information somewhere

▶ It must allocate a struct in the first 1 Mbyte of the physical

address space every time it is invoked, and this piece of Minix
code does not appear very reliable

▶ If vbe_get_mode_info() fails, you can retry a couple of times
▶ But sometimes, just rebooting Minix is faster

Always use the shell command poweroff

▶ As suggested in the handout, you can use static global

variables:

static uint16_t hres; /* XResolution */
static uint16_t vres; /* YResolution */

▶ Although you should avoid global variables, this use is akin to

the use of static member variables in C++

▶ You can define get() methods, if you want to access these
variables from outside of the file where they are declared.

▶ For example, get_hres()

28/34

Mapping the Linear Frame Buffer

▶ Before you can write to the frame buffer.

1. Obtain the physical memory address

1.1 Use vbe_get_mode_info() that we provide as part of

the LCF

▶ This function retrieves information about the input VBE
mode, including the physical address of the frame buffer

1.2 Should provide your own implementation, using VBE

function 0x01 Return VBE Mode Information, once
everything else has been completed.

2. Map the physical memory region into the process’ (virtual)

address space

29/34

HRESpixelsVRESpixelscolor(0,0)color(1,0)color(Hres-1,0)color(0,1)Virtual and Physical Address Spaces

Issue Most computer architectures
support a virtual address space
that is decoupled from the
physical address space

▶ Processes can access

(physical) memory using a
logical address that is
independent of the physical
address (determined by the
address bus decoding
circuitry)

▶ Most modern operating

systems, including Minix,
take advantage of this feature
to simplify memory
management.

30/34

Process(Virtual)AddressSpacePhysicalAddressSpace0x0Process(Virtual)AddressSpace0x0Mapping Physical Memory to Virtual Address Space

▶ Each process has its own

virtual address space, whose
size is usually determined by
the processor architecture
(32-bit for IA-32)

▶ The operating system maps

regions of the physical memory
in the computer to the virtual
address spaces of the different
processes

▶ The details of how this is

done were presented in the
Operating Systems course.
▶ In Lab 5, you have to map the
Video RAM to the virtual
address space

31/34

Process(Virtual)AddressSpacePhysicalAddressSpace0x0VideoRAMMapping VRAM in Minix (1/2)

int r;
struct minix_mem_range mr; /* physical memory range */
unsigned int vram_base; /* VRAM’s physical addresss */
unsigned int vram_size; /* VRAM’s size, but you can use

void *video_mem;

/* frame-buffer VM address */

the frame-buffer size, instead */

/* Allow memory mapping */

mr.mr_base = (phys_bytes) vram_base;
mr.mr_limit = mr.mr_base + vram_size;

if( OK != (r = sys_privctl(SELF, SYS_PRIV_ADD_MEM, &mr)))

panic("sys_privctl (ADD_MEM) failed: %d\n", r);

/* Map memory */

video_mem = vm_map_phys(SELF, (void *)mr.mr_base, vram_size);

if(video_mem == MAP_FAILED)

panic("couldn’t map video memory");

32/34

Mapping VRAM in Minix (2/2)

Question What is the following code about?

/* Allow memory mapping */

mr.mr_base = (phys_bytes) vram_base;
mr.mr_limit = mr.mr_base + vram_size;

if( OK != (r = sys_privctl(SELF, SYS_PRIV_ADD_MEM, &mr)))

panic("sys_privctl (ADD_MEM) failed: %d\n", r);

Answer In modern operating systems, user-level processes
cannot access directly HW resources, including physical
memory and VRAM

▶ Minix 3 handles this by allowing to grant privileged
user-level processes the permissions they require to
perform their tasks

33/34

Lab 5 - Part 1: Key Programming Issue

Issue Given a virtual address, how can a program access
the physical memory mapped to that virtual address?

Solution Use C pointers

▶ Pay attention to the size of a pixel.

34/34



---
# Document: 8xpm.pdf
---

Computer Labs: Lab 5 - Part 2
XPMs & VBE Function 0x00
2º LEIC

Pedro F. Souto (pfs@fe.up.pt)

April 5, 2024

1/13

Lab5: Video Card in Graphics Mode - 2nd Lab Class

▶ Write a set of functions:

int video_test_xpm(const char *xpm, uint16_t xi, uint16_t yi)
int video_test_move(const char *xpm, uint_t xi,

uint_t yi, ...)

int video_test_controller()

▶ Develop your own implementation of vbe_get_mode_info(),

which must call VBE function 0x01, Return VBE Mode
Information.

2/13

Lab 5: video_test_xpm()

int video_test_xpm(const char *xpm, uint16_t xi,

uint16_t yi)

What Display at the screen coordinates (xi,yi) the pixmap in

XPM format passed in xpm array

▶ Use VBE mode 0x105

3/13

Pixmaps and XPM
pixmap is a short term for “pixel map”, the representation of a digital

image as an array of pixel color values

▶ I.e. it is a map of screen coordinates to color values
▶ bitmap is a more generic term used in other fields of computer
science to denote the mapping from one domain to a bit string

XPM X Pixmap is an image format where each color value of a
pixmap is represented by character sequences/strings

▶ An XPM for a given pixmap can be stored:

▶ either in a text file,
▶ or as an array in a C source file

▶ In Lab 5, we use a simplified version of the XPM format:

▶ It uses only one character per color value

Terminology we will use:

(pix)map to refer to a pixmap that uses the color encodings of a

given graphical mode

xpm to refer to the XPM representation of a pixmap

▶ In Lab 5, we use an array of strings to store an XPM

4/13

Example: Using C Arrays to Store XPMs ("legacy")

static char *pic1[] = {
"32 13 4", /* number of columns and rows, in pixels, and colors */
". 0", /* ’.’ denotes color value 0 */
"x 2", /* ’x’ denotes color value 2 */
"o 14", /* .. and so on */
"+ 4",
"................................", /* the map
"..............xxx...............",
"............xxxxxxx.............",
".........xxxxxx+xxxxxx..........",
"......xxxxxxx+++++xxxxxxx.......",
"....xxxxxxx+++++++++xxxxxxx.....",
"....xxxxxxx+++++++++xxxxxxx.....",
"......xxxxxxx+++++xxxxxxx.......",
".........xxxxxx+xxxxxx..........",
"..........ooxxxxxxxoo...........",
".......ooo...........ooo........",
".....ooo...............ooo......",
"...ooo...................ooo...."
};

*/

Question How many elements does an XPM array have?

5/13

Example: Using C Arrays to Store XPMs

static xpm_row_t const minix3_xpm[] = {

c None",
c #C1C1C1",
c #323232",
c #090909",
c #010101",
c #161616",
c #9C9C9C",

"196 196 950 2",
"
".
"+
"@
"#
"$
"%
[...]
"
"

, ’ )

! ~ { ] ^ / ( _ : <

"
| | | 1 2 3 4 5

6 7 8 9

0 a / | | b c d e f ] g h @ g i i i j k

[...]

}

+ @ # $ %

& * = - ;

[ } | |

",

",

",

6/13

Lab 5: video_test_xpm()

int video_test_xpm(char *xpm, uint16_t xi, uint16_t yi)

What Display at the screen coordinates (xi,yi) the pixmap in

XPM format passed in xpm array

▶ Use VBE mode 0x105

Issue How to convert the xmp to a pixmap?
Answer Use the xpm_load() function

Note In the following pages, about the xpm_load() function,

most functions and types start with the substring xpm_
because they are defined in module XPM. Thus we use:
map to refer to pixmap in XPM format
image to refer to the image pixmap, i.e. with the colors

encoded for a specific graphics mode

7/13

Reading a Pixmap from its XPM: xpm_load() (1/2)

#define TRANSPARENCY_COLOR_1_5_5_5 0x8000
#define TRANSPARENCY_COLOR_8_8_8_8 0xFF000000
#define CHROMA_KEY_GREEN_888 0x00b140
#define CHROMA_KEY_GREEN_565 0x0588
enum xpm_image_type {

XPM_INDEXED, // for Minix def. pallette in VBE mode
XPM_1_5_5_5,
XPM_5_6_5,
XPM_8_8_8,
XPM_8_8_8_8,
INVALID_XPM

0x105

};
typedef struct {

enum xpm_image_type type;
uint16_t width;
uint16_t height;
size_t size;
uint8_t *bytes;

// size of the pixmap in bytes
// pointer to memory with pixmap

} xpm_image_t;
uint8_t *(xpm_load)(xpm_map_t map, enum xpm_image_type type,

xpm_image_t *img);

8/13

Reading a Pixmap from its XPM: xpm_load() (2/2)

xpm_map_t xmap;
xpm_image_t img;
uint8_t *map;
// get the pixmap from the XPM
map =
// copy it to graphics memory

// XPM
// pixmap and metadata
// pixmap itself

xpm_load(xmap, XPM_INDEXED, &img);

uint8_t *xpm_load(xpm_map_t xmap,

enum xpm_image_type type,
xpm_image_t *img); reads an XPM pixmap xmap,
and returns the pixmap as a two-dimensional uint8_t array. The
color encoding of the (output) pixmap is the one specified in type.
It assumes that the XPM uses:

▶ Either one char per color and one byte per color – only for

Minix default pallette in VBE-mode 0x105

▶ Or 3 bytes per color, with no restriction on the number of chars

per color (this is the format generated by GIMP)

9/13

Lab 5: video_test_move() (1/4)

int video_test_move( xpm_map_t *xpm[],,

uint16_t xi, uint16_t yi,
uint16_t xf, uint16_t yf
int8_t speed, uint8_t frame_rate)

What? Move an image on the screen (only along the x or y axes)

xpm XPM for the sprite
(xi,yi) initial coordinates (of the upper left corner (ULC))
(xf,yf) final coordinates (of ULC)
speed speed

If non-negative number of pixels between consecutive frames
If negative number of frames required for a 1 pixel movement
frame_rate number of frames per second. This is crucial for a

smooth movement of images on the screen

▶ Again, this has to do with the human vision
▶ But it also depends on how fast this movement is
▶ Use the Timer 0 interrupts for setting the frame-rate

10/13

Lab 5: video_test_move() (2/4)

Question? How can we give the illusion of movement of an image

on the screen?

Answer Just draw it repeatedly, in successive positions, starting

from its initial position until its final position.

11/13

Lab 5: video_test_move() (2/4)

Question? How can we give the illusion of movement of an image

on the screen?

Answer Just draw it repeatedly, in successive positions, starting

from its initial position until its final position.

11/13

Lab 5: video_test_move() (2/4)

Question? How can we give the illusion of movement of an image

on the screen?

Answer Just draw it repeatedly, in successive positions, starting

from its initial position until its final position.

11/13

Lab 5: video_test_move() (2/4)

Question? How can we give the illusion of movement of an image

on the screen?

Answer Just draw it repeatedly, in successive positions, starting

from its initial position until its final position.

11/13

Lab 5: video_test_move() (2/4)

Question? How can we give the illusion of movement of an image

on the screen?

Answer Just draw it repeatedly, in successive positions, starting

from its initial position until its final position.

11/13

Answer 600/60 = 10 s

▶ We need 600 Timer 0 interrupts to move the image by

▶ By default, the Timer 0 generates 60 interrupts per

the 600 pixels

second

Question How can you reduce this time?

Answer Two alternatives:

Using a higher interrupt rate need to configure Timer 0 (bad)

Moving the image by more than 1 pixel between frames

speed video_text_move()’s argument is used for that

▶ Using negative values for specifying the number of

frames required for a 1 pixel movement, we can make

ultra-slow movements

Lab 5: video_test_move() (3/4)

Example Consider an horizontal movement from column 200 to

column 800, i.e. of 600 pixels
Question If we move the image by 1 pixel on every Timer 0

interrupt, how long does it take?

12/13

Answer Two alternatives:

Using a higher interrupt rate need to configure Timer 0 (bad)

Moving the image by more than 1 pixel between frames

speed video_text_move()’s argument is used for that

▶ Using negative values for specifying the number of

frames required for a 1 pixel movement, we can make

ultra-slow movements

Lab 5: video_test_move() (3/4)

Example Consider an horizontal movement from column 200 to

column 800, i.e. of 600 pixels
Question If we move the image by 1 pixel on every Timer 0

interrupt, how long does it take?

Answer 600/60 = 10 s

▶ We need 600 Timer 0 interrupts to move the image by

the 600 pixels

▶ By default, the Timer 0 generates 60 interrupts per

second

Question How can you reduce this time?

12/13

Lab 5: video_test_move() (3/4)

Example Consider an horizontal movement from column 200 to

column 800, i.e. of 600 pixels
Question If we move the image by 1 pixel on every Timer 0

interrupt, how long does it take?

Answer 600/60 = 10 s

▶ We need 600 Timer 0 interrupts to move the image by

the 600 pixels

▶ By default, the Timer 0 generates 60 interrupts per

second

Question How can you reduce this time?
Answer Two alternatives:

Using a higher interrupt rate need to configure Timer 0 (bad)
Moving the image by more than 1 pixel between frames
speed video_text_move()’s argument is used for that
▶ Using negative values for specifying the number of

frames required for a 1 pixel movement, we can make
ultra-slow movements

12/13

Alternative 1 Every time we move an image:

1. Delete the image, i.e. reset the color of the screen pixels in its

current position

2. Redraw the image in its next position

Optimization only reset those screen pixels that are not overlapped

in the new position

Alternative 2 Redraw the entire screen at the desired frame-rate

1. On a second buffer, create a frame, a complete screen, with

the image in its position in the next frame

2. Copy the contents of the second buffer to the frame-buffer

Optimization You can omit these steps, if the position of the image

on the next frame is the same as in the current frame

Lab 5: video_test_move() (4/4)

Issue If you just redraw the image in its successive positions, every

movement will lead to a trail

Fix Ensure that the screen’s pixels occupied in a position but not
occupied in the next position are reset to their previous value

How can we do this?

13/13

Lab 5: video_test_move() (4/4)

Issue If you just redraw the image in its successive positions, every

movement will lead to a trail

Fix Ensure that the screen’s pixels occupied in a position but not
occupied in the next position are reset to their previous value

How can we do this?

Alternative 1 Every time we move an image:

1. Delete the image, i.e. reset the color of the screen pixels in its

current position

2. Redraw the image in its next position

Optimization only reset those screen pixels that are not overlapped

in the new position

Alternative 2 Redraw the entire screen at the desired frame-rate

1. On a second buffer, create a frame, a complete screen, with

the image in its position in the next frame

2. Copy the contents of the second buffer to the frame-buffer

Optimization You can omit these steps, if the position of the image

on the next frame is the same as in the current frame

13/13



---
# Document: 9graphics.pdf
---

Computer Labs: Buffering in Computer
Graphics
2º LEIC

Pedro F. Souto (pfs@fe.up.pt)

April 12, 2024

1/11

Raster graphics vs. Vector Graphics

Raster graphics An image is represented as "a rectangular matrix

or grid of square pixels".

▶ Each pixel has a numeric value, usually a color
▶ The position of the pixel in the grid, is determined implicitly
▶ The size of an image depends on the resolution
▶ Formats often use compression to reduce size
▶ File formats: XPM, BMP, PNG, TIFF

Vector graphics Images are created from geometric shapes such

as points, lines, curves, on a Cartesian plane.

▶ It allows a higher degree of geometric precision than rasters

graphics

▶ Its size is independent of the resolution
▶ File formats: SVG, EPS, PDF

2/11

Computer Display Hardware

Raster displays Virtually all displays nowadays, are raster

displays, i.e. they have a matrix of pixels
▶ The image is stored in a frame buffer
▶ The hardware is simpler
▶ Takes a constant time to redraw a screen, independently of

the number of graphical objects

▶ Images have jagged edges and geometric shapes are

approximated

Vector displays Were the first technology (early 60s), and

generate images from paths

▶ Are able to draw continuous and smooth lines
▶ Hardware is more complex and expensive
▶ Refresh rate depends on the number of "paths" in the

image

▶ May flicker, if the image becomes too large.

3/11

Cathode Ray Tube (CRT) Raster Display Operation

CRT Hardware

Raster Scan

src: Theresa Knott

▶ The color of each pixel depends on the respective value in VRAM
▶ The controller refreshes the screen with a frequency ≥ 50/60 Hz

src: Ian Harvey

LCD Panels

Introduction to graphics and LCD, NXP

4/11

Outputing of the Frame Buffer on the Display

To change the frame displayed we need to change the contents of

the frame buffer, in VRAM

There are several alternatives

1. Upon change of a sprite position, change the contents of

the frame buffer

2. · · ·

5/11

videocontrollerframebufferinvideoRAMdisplayline0line1lineVRES-1Modify frame buffer, upon change of sprite position

Issue if we modify the frame buffer contents of the region that is
being scanned, the picture on the display may show visual
artifacts:

▶ A piece of the display will show what was there before the
change, and another piece will show the new contents
▶ It there is no new change, the problem will be fixed the

next time the screen is refreshed, i.e. within 16.67 or 20 ms
(depending on the vertical refresh frequency)

▶ How bad is this?

▶ It depends on how frequently it occurs (the more dynamic

the frames, the worse).

▶ The number and size of the sprites also matter, and the

colors too

6/11

How to avoid these visual artifacts?

No solution Synchronize the application with display refreshment
▶ If the application modified the frame buffer in the wake of
the video controller, there would be no visual artifacts

Double buffering I.e. use a second buffer, the back buffer in RAM

1. Create the new frame in the back buffer
2. Copy the new frame from the back buffer to the frame buffer

in video RAM (VRAM)

Page Flipping The two buffers are in VRAM

▶ The video controller has a register that points to the buffer

being displayed on the screen, the front buffer

▶ Rather than copying, just flip the two buffers, i.e. change
the contents of that register to point to the back buffer

▶ and swap the role of the buffers: the back buffer becomes

the front buffer, and vice-versa

▶ Use VBE function 0x07 (Set/Get Start of Display), of VBE

2.0 Specification

7/11

Vertical Synchronization

Issue Double buffering, regardless of implementation, may not

completely eliminate visual artifacts, although it reduces them
▶ If copy or flip occur in the middle of a scan, the screen will

display tearing

Solution Use the vertical retrace interval, i.e. the interval between
rendering the right most pixel of the bottom line of one frame,
and the rendering of the left most pixel of the top line of the next
frame

▶ For CRTs it is in the order of 500 µs
▶ For LCDs it is much shorter (Some years ago xvidtune

reported about 100 µs in my laptop at the time.)

Issue How to synchronize with vertical retrace?

VGA has some registers to configure interrupt generation on

vertical retrace

VBE function 0x07 Set/Get Display Start, sub-function 0x80,

Set Display Start during Vertical Retrace, allows to swap the
frame buffer in the following vertical retrace

8/11

Triple Buffering

Issue Vertical synchronization with double buffering may slow

down the frame rate

▶ Assume the video controller is displaying frame n
▶ The application cannot start the following frame (n + 2) as

soon as it completes the next frame (n + 1)

▶ It must wait until the vertical retrace
▶ The back buffer cannot be modified, otherwise one may loose the

next frame (n + 1)

Triple Buffering I.e. use a second back buffer

▶ After generating frame n + 1 on the first back buffer, start
generating frame n + 2 on the second back buffer without
delay

▶ Upon a vertical retrace, the back buffer with the most recent
completed frame becomes the front buffer, and the previous
front buffer a back buffer

9/11

Triple Buffering and VBE 2.0

Question Can we use VBE 2.0 function 0x07, sub-function 0x80,
Set Display Start during Vertical Retrace, to implement triple
buffering?

Answer Depends on the implementation

▶ In some implementations, Set Display Start during Vertical
Retrace is a blocking call, in that case, there is no need for
a third buffer

▶ When it returns, there is always one free back-buffer, even if

there are only two buffers.

For maximum frame rate Many games allow disabling vertical

(retrace) synchronization

▶ Vertical synchronization eliminates visual artifacts
▶ But introduces a delay between the frame generation and

its display on the screen

10/11

Further Reading

▶ John T. Bell, Vector vs Raster Displays, Computer Graphics

Course Notes

11/11



---
# Document: 9sprites.pdf
---

Computer Labs: Lab 5 & Sprites
2º MIEIC

Pedro F. Souto (pfs@fe.up.pt)

April 12, 2024

The “Class” Sprite: sprite.h (by jcard@fe.up.pt)

Sprite “Two-dimensional image that is integrated into a larger

scene” (Wikipedia)

▶ Allows the integration of independent pixmaps into a

scene

▶ Allows image animation without altering the background
– thus a sprite can be considered an overlay image

typedef struct {

int x, y; // current position
int width, height;
int xspeed, yspeed; // current speed
char *map;

// the pixmap

// dimensions

} Sprite;

The pixmap uses black (or some unused color) for the
background, which is assumed to be transparent

The “Class” Sprite: sprite.c (1/2)

/** Creates a new sprite from XPM "pic", with specified
position (within the screen limits) and speed;

*
* Does not draw the sprite on the screen
* Returns NULL on invalid pixmap.
*/

Sprite *create_sprite(const char *pic[], int x, int y,

int xspeed, int yspeed) {

//allocate space for the "object"
Sprite *sp = (Sprite *) malloc ( sizeof(Sprite));
xpm_image_t img;
if( sp == NULL )
return NULL;

// read the sprite pixmap
sp->map = xpm_load(pic, XPM_INDEXED, &img);
if( sp->map == NULL ) {

free(sp);
return NULL;

}
sp->width = img.width; sp->height=img.height;
...
return sp;

}

The “Class” Sprite: sprite.c (2/2)
void destroy_sprite(Sprite *sp) {

if( sp == NULL )
return;
if( sp ->map )

free(sp->map);

free(sp);
sp = NULL;

}

// XXX: pointer is passed by value
//

should do this @ the caller

// XXX: move_sprite would be a more appropriate name
int animate_sprite(Sprite *sp) {

...

}

/* Some useful non-visible functions */
static int draw_sprite(Sprite *sp, char *base) {

...

}
static int check_collision(Sprite *sp, char *base) {

...

}

Lab 5: test_move() (again)

int video_test_move( const char *xpm[],,

uint16_t xi, uint16_t yi,
uint16_t xf, uint16_t yf
int8_t speed, uint8_t frame_rate)

What? Move a sprite on the screen (only along the x or y axes)

xpm XPM for the sprite
(xi,yi) initial coordinates (of ULC)
(xf,yf) final coordinates (of ULC)
speed speed

If non-negative number of pixels between consecutive frames
If negative number of frames required for a 1 pixel movement

frame_rate number of frames per second

How? Should use the sprite "class"

▶ But you can change it slightly (I did).
▶ Need not implement all functions.

Sprite Animation

▶ Animation of a sprite can be achieved by presenting a

sequence of pixmaps

▶ Each pixmap (but the first) in this sequence differs slightly from

the previous pixmap

▶ To create an animated sprite we need to specify several

pixmaps

▶ This can be done in different ways

▶ E.g. using an array of pixmaps

▶ We’ll use a C function with a variable number of arguments:

AnimSprite *create_animSprite(uint8_t no_pic, char *pic1[], ...);
printf() is the most common C function of this type

(Functions with a Variable Number of Arguments (1/2))

▶ Must have at least one named argument

▶ The unnamed arguments are passed in a list

▶ But, needs to know

▶ How many arguments in the list
▶ The type of each of these arguments

both of which can vary from one invocation to the next

▶ Uses a kind of an iterator, of type va_list, to traverse the list
▶ Relies on a set of macros defined in <stdarg.h>, whose first

parameter is the "iterator":
va_start initializes the iterator to the first argument of the list
▶ va_start second argument is the last known function

argument

va_arg to get the next argument of the list, i.e. to iterate through

the list

▶ va_arg second argument is the type of that unnamed argument
▶ On first invocation, returns the first argument after the last
known argument, i.e. the first unnamed argument in the list

va_end to finalize the access

(Functions with a Variable Number of Arguments (2/2))

#include <stdarg.h> // va_* macros are defined here
int foo(int required, ...) {

va_list ap; // "pointer" to next argument
va_start(ap, required); // initializes ap to point to

// first (unnamed) argument of the list ;
// the 2nd argument of va_start is the last named argument

int i = va_arg(ap, int); // accesses the next list argument

// the second argument of va_arg() is the type
// on first call, returns the value of the first
// argument after the
float i = va_arg(ap, float);
char *s = va_arg(ap, char *);
va_end(ap); // must be called to finalize the access

last fixed

argument

}

Question How do you know the type of each argument of the list?

Answer There are several possibilities:
printf() uses the format string
create_animSprite() all arguments have the same known

type

▶ What changes is the number of arguments

The “Class” Animated Sprite: AnimSprite.h

#include <stdarg.h> // va_* macros are defined here
#include "sprite.h"
typedef struct {

// standard sprite
// no. frames per pixmap

Sprite *sp;
int aspeed;
int cur_aspeed; // no. frames left to next change
int num_fig;
int cur_fig;
char **map;

// number of pixmaps
// current pixmap
// array of pointers to pixmaps

} AnimSprite;

create_animSprite(uint8_t no_pic, char *pic1[], ...);
int animate_animSprite(AnimSprite *sp,);
void destroy_animSprite(AnimSprite *sp);

Animation speed is measured as number of “frames” per pixmap,
i.e. the number of frames each pixmap is displayed in an
animation.

▶ The smaller this value, the faster the animation

The “Class” Animated Sprite: AnimSprite.c (1/2)

AnimSprite *create_animSprite(uint8_t no_pic,

char *pic1[], ...) {

AnimSprite *asp = malloc(sizeof(AnimSprite));
// create a standard sprite with first pixmap
asp->sp = create_sprite(pic1,0,0,0,0);
// allocate array of pointers to pixmaps
asp->map = malloc((no_pic) * sizeof(char *));
// initialize the first pixmap
asp->map[0] = asp->sp->map;
// continues in next transparency

The “Class” Animated Sprite: AnimSprite.c (2/2)

// initialize the remainder with the variable arguments
// iterate over the list of arguments
va_list ap;
va_start(ap, pic1);
for( i = 1; i <no_pic; i++ ) {

char **tmp = va_arg(ap, char **);
xpm_image_t img;
asp->map[i] = xpm_load(tmp, XPM_INDEXED, &img);
if( asp->map[i] == NULL

|| img.width != asp->sp->width || img.height != asp->sp->height) {
// failure: release allocated memory
for(j = 1; j<i;j ++)

free(asp->map[i]);

free(asp->map);
destroy_sprite(asp->sp);
free(asp);
va_end(ap);
return NULL;

}

}
va_end(ap);
...

}

Thanks to:

Based on material by:
▶ João Cardoso (jcard@fe.up.pt)

Further Reading

▶ João Cardoso, Notas sobre Sprites

