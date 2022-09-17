## [운영체제] Process

#### 프로세스의 개념

>  ***"Process is a program in execution"***



##### 프로세스의 문맥(context)

- CPU 수행 상태를 나타내는 하드웨어 문맥
  - Program Counter
  - 각종 register
- 프로세스의 주소 공간
  - code, data, stack
- 프로세스 관련 커널 자료 구조
  - PCB(Process Control Block)
  - kernel stack



#### 프로세스의 상태(Process State)

- 프로세스는 상태가 변경되며 수행된다

  - **Running**
    - CPU를 잡고 instruction을 수행중인 상태
  - **Ready**
    - CPU를 기다리는 상태(메모리 등 다른 조건을 모두 만족하고)
    - CPU만 얻으면 바로  instruction을 수행 가능한 상태
    - 레디상태를 왔다 갔다하며 타임 쉐어링을 구현
  - **Blocked(wait, sleep)**
    - CPU를 주어도 당장 instruction을 수행할 수 없는 상태
    - Process 자신이 요청한 event(ex I/O)가 즉시 만족되지 않아 이를 기다리는 상태
    - ex) 디스크에서 file을 읽어와야 하는 경우(오래 걸리기 때문에 CPU를 받아봤자 바로 X)
  - **Suspended(stopped)**
    - 외부적인 이유로 프로세스의 수행이 정지된 상태(외부에서 강제로 stop)
    - 프로세스는 통째로 디스크에 swap out 된다
    - ex) 사용자가 프로그램을 일시 정지시킨 경우(break key) 시스템이 여러 이유로 프로세스를 잠시 중단시킴(메모리에 너무 많은 프로세스가 올라와 있을 때)
    - 중기 스케줄러로 인해 뺏긴 상태
  - New: 프로세스가 생성중인 상태
  - Terminated: 수행이 끝난 상태

  > Blocked: 자신이 요청한 event가 만족되면 Ready
  >
  > Suspended: 외부에서 resume해 주어야 Active

  

![image-20220917171709702](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220917171709702.png)



#### 프로세스 상태도

![image-20220917171557854](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220917171557854.png)



#### Process Control Block (PCB)

##### PCB

- 운영체제가 각 프로세슷를 관리하기 위해 프로세스당 유지하는 정보
- 다음의 구성 요소를 가진다 (구조체로 유지)
  1. OS가 관리상 사용하는 정보
     - Process State, Process ID
     - scheduling information, priority
  2. CPU 수행 관련 하드웨어 값
     - Program counter, registers
  3. 메모리 관련
     - Code, data, stack의 위치 정보
  4. 파일 관련
     - Open file descriptors...



#### 문맥 교환(Context Switch)

- CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 과정
  - 뺏기는 시점을 기억했다가 다시 실행하는 느낌
- CPU가 다른 프로세스에게 넘어갈 때 운영체제는 담을 수행
  - CPU를 내어주는 프로세스의 상태를 그 프로세스의 PCB(커널)에 저장
  - CPU를 새롭게 얻는 프로세스의 상태를 PCB(커널)에서 읽어옴

- System call이나 Interrupt 발생 시 반드시 context switch가 일어나는 것은 아님

![image-20220917172851923](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220917172851923.png)

-> (1)의 경우에도 CPU 수행 정보 등 context의 일부를 PCB에 save해야 하지만 문맥교환을 하는 (2)의 경우 그 부담이 훨씬 큼(eg.cache memory flush)



#### 프로세스를 스케줄링하기 위한 큐

##### Job queue

- 현재 시스템 내에 있는 모든 프로세스의 집합

##### Ready queue

- 현재 메모리 내에 있으면서 CPU를 잡아서 실행되기를 기다리는 프로세스의 집합

##### Device queues

- I/O device

> 프로세스들은 각 큐들을 오가며 수행된다.



##### Ready Queue와 다양한 Device Queue

![image-20220917173648634](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220917173648634.png)



#### 프로세스 스케줄링 큐의 모습

![image-20220917173729886](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220917173729886.png)

- 인터럽트랑 I/O랑 다를거 없음



#### 스케줄러(scheduler)

##### Long-term scheduler (장기 스케줄러 or job scheduler)

- 시작 프로세스 중 어떤 것들을 ready queue로 보낼지 결정
- 프로세스에 memory(및 각종 자원)을 주는 문제
- degree of Multiprogramming을 제어
- time sharing system에는 보통 장기 스케줄러가 없음 (무조건 ready)
  - 보통 무조건 메모리에 올려 줌(결정하는 타임이 없음)



##### Short-term scheduler (단기 스케줄러 or CPU scheduler)

- 어떤 프로세스를 다음번에 running시킬지 결정
- 프로세스에 CPU를 주는 문제
- 충분히 빨라야 함(millisecond 단위)



##### Medium-term scheduler (중기 스케줄러 or Swapper)

- 여유 공간 마련을 위해 프로세스를 통째로 메모리에서 디스크로 쫓아냄
- 프로세스에게서 memory를 뺏는 문제
- degree of Multiprogrammin을 제어
- 요즘은 일단 다 올려놓고 중기에서 빼는 것을 주로 사용



#### 프로세스 상태도

![image-20220917175218928](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20220917175218928.png)



#### Thread

![image-20220917175940035](C:\Users\SSAFY\Desktop\HJ\TIL\CS\운영체제\assets\image-20220917175940035.png)

> ***"A thread (or lightweight process) is a basic unit of CPU utilization"***

- Thread의 구성
  - program counter
  - register set
  - stack space
- Thread가 동료 thread와 공유하는 부분(=task)
  - code section
  - data section
  - OS resources
- 전통적인 개념의 heavyweight process는 하나의 thread를 가지고 있는 task로 볼 수 있다
- 다중 스레드로 구성된 태스크 구조에서는 하나의 서버 스레드가 blocked(waiting) 상태인 동안에도 동일한 태스크 내의 다른 스레드가 실행(running)되어 빠른 처리를 할 수 있다.
- 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율을(throughtput)과 성는 향상을 얻을 수 있다
- 스레드를 사용하면 병렬성을 높일 수 있다.



#### Benefits of Threads

##### Responsiveness(빠른거)

- eg) multi-threaded-web 
  - if one thread is blocked(eg network) another thead continues(eg display)

##### Resource Sharing(자원 공유)

- n threads can share binary code, data, resource of the process
- 똑같은 일을 하는 여러개의 프로그램 하나의 프로세스를 만들고 CPU 수행 단위만 여러 개 만들면 더 효율적으로 가능

##### Economy(경제성)

- creating & CPU switching thread (rather than a process)
- Solaris의 경우 위 두 가지 overhead가 각각 30배, 5배
- 스레드 하나 늘리는게 더 싸고 오버헤드도 적음

##### Utilization of MP Architectures

- each thread may be running in parallel on a different processor



#### Implementation of Threads

- Some are supported by kernel
  - Windows 95/98/NT
  - Solaris
  - Digital Unix, Mach

-> Kernel Threads

- Others are supported by library
  - Posix Pthreads
  - Mach C-threads
  - Solaris threads

-> User Threads

- Some are real-time threads