## 📖 CPU Scheduling

### 📚 CPU-burst Time

여러 종류의 job(=process)이 섞여 있기 때문에 CPU 스케줄링이 필요하다.

- Interactive job에게 적절한 response 제공 요망
- CPU와 I/O 장치 등 시스템 자원을 골고루 효율적으로 사용
- CPU-burst가 굉장히 긴 것 하나와 짧은 거 여러 개가 있을 경우 긴 것 하나 때문에 나머지 짧은 것들이 모두 멈추기 때문에 CPU 스케줄링이 필요하다



### 📚 CPU Scheduler & Dispatcher

#### 📍 CPU Scheduler

- Ready 상태의 프로세스 중에서 이번에 CPU를 줄 프로세스를 고른다

#### 📍 Dispatcher

- CPU의 제어권을 CPU scheduler에 의해 선택된 프로세스에게 넘긴다
- 이 과정을 context switch(문맥 교환)라고 한다.

#### 📍 CPU 스케줄링이 필요한 경우는 프로세스에게 다음과 같은 상태 변화가 있는 경우이다.

1. Running => Blocked(예: I/O 요청하는 시스템 콜)
2. Running => Ready(예: 할당시간만료로 timer interrupt)
3. Blocked => Ready(예: I/O 완류 후 인터럽트)
4. Terminate

비선점형 nonpreemptive(=강제로 빼앗지 않음)

선점형 preemptive(=강제로 빼앗음)



### 📚 Scheduler Criteria

##### Performance Index ( = performance Measure, 성능 척도)

#### 📍 CPU utilization (이용률)

- keep the CPU as busy as possible
- 전체 시간 중에 놀지 않고 일한 시간의 비율

#### 📍 Throughput (처리량)

- \# of Process that complete their execution per time unit
- 주어진 시간동안 몇개의 일을 처리했는가

#### 📍 Turnaround time (소요시간, 반환시간)

- amout of time to execute a particular process
- CPU를 쓰러 들어와서 나가는데까지 걸린 시간

#### 📍 Waiting time (대기시간)

- amount of time a process has been waiting in the ready queue
- CPU를 쓰기까지 기다린 시간 

#### 📍 Response time (응답시간)

- amount of time it takes from when a request was submitted until the first response is produced, not output (for time-sharing environment)
- CPU를 쓰러와서 첫 번째로 받을때까지 걸린 시간



### 📚 FCFS (First-come First-Served)

- 먼저온 순서대로 처리함
- 비선점형 프로세스 (효율적이지 않다)
- convoy effect : short process behind long process

### 📚 SJF (Shortest-Job-First)

- 각 프로세스의 다음번 CPU burst time을 가지고 스케줄링에 활용
- CPU burst time이 가장 짧은 프로세스를 제일 먼저 스케줄
- TWO schemes
  - 비선점형 : 짧은게 와도 안비켜줌
  - 선점형 : 더 짧은거 오면 비켜줌

- SJF is optimal
  - 주어진 프로세스들에 대해 minimum average waiting time을 보장(선점형일 때)

- 문제점
  - starvation : 오래 걸리는 애들은 평생 못 할수도 있다.
  - 다음번 CPU burst time을 알 수가 없어 추정만 가능하다

### 📚 Priority Scheduling

- 우선순위가 가장 높은 애한테 먼저 줌
- SJF도 일종의 Priority Scheduling
- 문제점
  - starvation
- 해결책
  - Aging : 들어온 시간이 길수록 우선순위가 높아져감

### 📚 Round Robin (RR)

- 각 프로세스는 동일한 크기의 할당 시간을 가짐
- 할당 시간이 지나면 프로세스는 선점당하고 ready queue의 제일 뒤에 가서 다시 줄을 선다
- n개의 프로세스가 ready queue에 있고 할당 시간이 q time unit인 경우 각 프로세스는 최대 q time unit 단위로 CPU 시간의 1/n을 얻는다. 
- **어떤 프로세스도 (n-1)q time unit 이상 기다리지 않는다**
- Performance 
  - q large => FCFS
  - q small => context switch 오버헤드가 커진다.

### 📚 MultiLevel Queue

- 큐마다 우선순위가 있어 각 프로세스가 자기에게 맞는 큐에 섬
- 높은 우선순위가 있는 큐부터 처리(fixed priority scheduling)
- 각 큐는 독립적인 스케줄링 알고리즘을 가짐

### 📚 Multilevel Feedback Queue

- 큐마다 우선순위가 있어 각 프로세스가 자기에게 맞는 큐에 섬
- 프로세스가 시간에 지남에 따라 다른 줄에도 설 수 있음

### 📚 Multiple-Processor Scheduling

##### CPU가 여러 개인 경우

- ##### Homogeneous processor

  - Queue에 한줄로 세워서 각 프로세서가 알아서 꺼내가게 할 수 있다
  - 반드시 특정 프로세서에서 수행되어야 하는 프로세스가 있는 경우에는 문제가 더 복잡해짐

- ##### Load sharing

  - 일부 프로세서에 job이 몰리지 않도록 부하를 적절히 공유하는 메커니즘 필요
  - 별개의 큐를 두는 방법 vs 공동 큐를 사용하는 방법
  - 특정 CPU만 일하면 안되므로 Load sharing이 필요

- ##### Symmetric Multiprocessing (SMP)

  - 각 프로세서가 각자 알아서 스케줄링 결정 (프로세서별 스케줄링)

- ##### Asymmetric multiprocessing

  - 하나의 프로세서가 시스템 데이터의 접근과 공유를 책임지고 나머지 프로세서는 거기에 따름

### 📚 Real-Time Scheduling

- Hard real-time systems
  - 정해진 시간 안에 반드시 끝내도록 스케줄링
  - 반드시 데드라인 안에 해야함
- Soft real-time systems
  - 일반 프로세스에 비해 높은 prioirty를 갖도록 스케줄링

### 📚 Thread Scheduling

- Local Scheduling

  - User level thread의 경우 사용자 수준의 thread library에 의해 어떤 thread를 스케줄 할 지 결정
  - 프로세스 내부에서 결정

- Global Scheduling

  - Kernal level thread의 경우 일반 프로세스와 마찬가지로 커널의 단기 스케줄러가 어떤 thread를 스케줄 할 지 결정

  - 운영체제가 알고리즘에 근거해서 결정

    

### 📚 Algorithm Evaluation

- Queueing models
  - 확률 분포로 주어지는 arrival rate와 service rate 등을 통해 각종 performance index 값을 계산
- Implement(구현) & Measurement(성능 측정)
  - 실제 시스템에 알고리즘을 구현하여 실제 작업(workload)에 대해서 성능을 측정 비교
- Simulation (모의 실험)
  - 알고리즘을 모의 프로그램으로 작성 후 trace를 입력으로 하여 결과 비교