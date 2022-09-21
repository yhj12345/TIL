## [운영체제] Process Management

#### 프로세스 생성(Process Creation)

##### Copy-on-write(COW)

- 부모 프로세스가 자식 프로세스 생성
- 프로세스의 트리(계층 구조) 형성
- 프로세스는 자원을 필요로 함
  - 운영체제로부터 받음
  - 부모와 공유
- 자원의 공유
  - 부모와 자식이 모든 자원을 공유하는 모델
  - 일부를 공유하는 모델
  - 전혀 공유하지 않는 모델 -> 일반적
- 수행(Execution)
  - 부모와 자식은 공존하며 수행되는 모델
  - 자식이 종료될 때까지 부무가 기다리는 모델

- 주소 공간(Address space)
  - 자식은 부모의 공간을 복사함 (binary and OS data)
  - 자식은 그 공간에 새로운 프로그램을 올림



#### 프로세스 종료(Process Termination)

- 프로세스가 마지막 명령을 수행한 후 운영체제에게 이를 알려줌
  - 자식이 부모에게 output data를 보냄
  - 프로세스의 각종 자원들이 운영체제에게 반납됨
- 부모 프로세스가 자식의 수행을 종료시킴
  - 자식이 할당 자원의 한계치를 넘어섬
  - 자식에게 할당된 태스크가 더 이상 필요하지 않음
  - 부모가 종료하는 경우
    - 운영체제는 부모 프로세스가 종료하는 경우 자식이 더 이상 수행되도록 두지 않는다.
    - 단계적인 종료



#### 프로세스와 관련한 시스템 콜

##### fork() 시스템 콜

##### exec() 시스템 콜

##### wait() 시스템 콜

##### exit() 시스템 콜



#### 프로세스 간 협력

##### 독립적 프로세스

- 프로세스는 각자의 주소 공간을 가지고 수행되므로 원칙적으로 하나의 프로세스는 다른 프로세스의 수행에 영향을 미치지 못함

##### 협력 프로세스

- 프로세스 협력 메커니즘을 통해 하나의 프로세스가 다른 프로세스의 수행에 영향을 미칠 수 있음

##### 프로세스 간 협력 메커니즘

- 메시지를 전달하는 방법

  - message passing : 커널을 통해 메세지 전달

- 주소 공간을 공유하는 방법

  - shared memory : 서로 다른 프로세스 간에도 일부 주소 공간을 공유하게 하는 shared memory 메커니즘이 있음

  - thread : thread는 사실상 하나의 프로세스이므로 프로세스 간 협력으로 보기는 어렵지만 동일한 process를 구성하는 thread들간에는 주소 공간을 공유하므로 협력이 가능



#### Message Passing

##### Message system

- 프로세스 사이에 공유 변수를 일체 사용하지 않고 통신하는 시스템

##### Direct Communication

- 통신하려는 프로세스의 이름을 명시적으로 표시

##### Indirect Communication

- mailbox(또는 port)를 통해 메시지를 간접 전달



#### 프로세스의 특성 분류

##### 프로세스는 그 특성에 따라 다음 두 가지로 나눔

- I/O-bound process
  - CPU를 잡고 계산하는 시간보다 I/O에 많은 시간이 필요한 job
  - (many short CPU bursts)
- CPU-bound process
  - 계산 위주의 job
  - (few very long CPU burts)



#### CPU Scheduler & Dispatcher

##### CPU Scheduler

- ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다

##### Dispatcher

- CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘긴다
- 이 과정을 context switch(문맥 교환)이라고 한다.

##### CPU 스케줄링이 필요한 경우는 프로세스에게 다음과 같은 상태 변화가 있는 경우이다.

- running -> blocked (예: I/O 요청하는 시스템 콜)
- running -> ready (예: 할당시간만료로 timer interrupt)
- blocked -> ready (예: I/O 완료 후 인터럽트)
- terminate

1,4 에서의 스케줄링은 nonpreemptive(=강제로 빼앗지 않고 자진 반납)

All other scheduling is preemptive(=강제로 빼앗음)