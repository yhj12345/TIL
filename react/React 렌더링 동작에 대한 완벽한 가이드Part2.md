# React 렌더링 동작에 대한 완벽한 가이드

### 렌더링 성능 개선

렌더링은 리액트 동작 방식에서 일반적으로 요구되는 부분이지만 렌더링 작업이 때로는 "낭비"될 수 있다는 것도 사실입니다. 만약 컴포넌트의 렌더링 출력이 변경되지 않았고, DOM의 해당 부분을 업데이트할 필요가 없다면 해당 컴포넌트를 렌더링하는 작업은 정말 시간 낭비입니다.

리액트 컴포넌트의 렌더링 출력은 항상 현재 props 및 상태가 변경되지 않았다는 것을 미리 알고 있다면 렌더링 출력이 동일하고 이 컴포넌트에 대한 변경이 필요하지 않으며 렌더링 작업을 안전하게 건너뛸 수 있다는 것도 알 수 있습니다.

일반적으로 소프트웨어 성능을 향상시키려 할 때, 두 가지 기본 접근 방식이 있습니다. 1) 동일한 작업을 더 빨리 수행하는 것, 그리고 2) 더 적게 수행하는 것입니다. 리액트 렌더링을 최적화 하는 것은 주로 컴포넌트 렌더링을 적절히 건너뛰어 작업량을 줄이는 것입니다.

#### 컴포넌트 렌더링 최적화 기법

리액트는 컴포넌트 렌더링을 생략할 수 있는 세가지 주요한 API를 제공합니다.

주된 메서드는 `"higher order component"` 형태로 내장된 `React.memo()`입니다. 사용자의 컴포넌트 타입을 인자로 전달받고 래핑된 새 컴포넌트를 반환합니다. 래퍼 컴포넌트의 기본 동작은 props가 변경되었는지 확인하고 변경되지 않은 경우 리렌더링되지 않도록 하는 것입니다. 함수 컴포넌트와 클래스 컴포넌트 둘 다 `React.memo()`를 사용해 래핑할 수 있습니다. (커스텀 비교 콜백을 전달할 수 있지만, 오직 이전 props와 새 props의 비교만 할 수 있으므로, 커스텀 비교 콜백은 주로 모든 props 대신 특정 props만 비교하기 우해 사용됩니다.)

이외 다른 API는 다음과 같습니다.

- `React.Componet.shouldComponentUpdate`: 렌더링 프로세스 초기에 호출되는 선택적 클래스 컴포넌트 생명 주기 메서드입니다. `false`를 반환하면 리액트는 컴포넌트 렌더링을 건너뜁니다. 렌더링 여부를 결정하는 boolean 결과값을 계산하는데 사용할 로직을 포함할 수 있고 가장 일반적인 방법은 컴포넌트의 props 및 상태가 이전과 달라졌는지 확인하고 변경되지 않았으면 `false`를 반환하는 것입니다.
- `React.PureComponent`: 이러한 props 및 상태 비교는 `shoulComponentUpdate`를 구현하는 가장 일반적인 방법이기 때문에 `PureComponent` 기반 클래스는 기본적으로 해당 동작을 구현하며 `Component` + `shoulComponentUpdate` 대신 사용할 수 있습니다.

이 모든 접근 방식은 "얕은 비교"라고 불리는 비교 기법을 사용합니다. 이는 두 개의 서로 다른 객체의 모든 개별 필드를 확인하고 객체의 내용이 서로 다른 값인지 확인하는 것을 의미합니다. 달리 표현하면 `obj1.a === obj2.a && obj1.b === obj2.b && .......`입니다. `===`비교 연산은 JS 엔진이 처리하기에 매우 간단하기 때문에 이는 일반적으로 빠른 프로세스입니다. 따라서 위 세 가지 접근 방식은 `const shouldRender = !shallowEqual(newProps, prevProps)`와 같습니다.

조금 덜 알려진 기법도 있습니다. 리액트 컴포넌트가 이전과 정확히 동일한 요소 참조를 반환하면 리액트는 해당하는 특정 하위 컴포넌트의 리렌더링을 건너뜁니다. 이 기법을 구현하는 두 가지 방법이 있습니다.

- 출력에 `props.children`을 포함하는 경우 컴포넌트가 상태를 업데이트해도 해당 요소는 동일합니다.
- `useMemo()`로 요소를 감싸면 종속성이 변경될 때까지 동일하게 유지됩니다.

예시

```react
// `props.children`는 상태를 업데이트 하더라도 리렌더링되지 않습니다.
function SomeProvider({ children }) {
  const [counter, setCounter] = useState(0);

  return (
    <div>
      <button onClick={() => setCounter(counter + 1)}>Count: {counter}</button>
      <OtherChildComponent />
      {children}
    </div>
  );
}

function OptimizedParent() {
  const [counter1, setCounter1] = useState(0);
  const [counter2, setCounter2] = useState(0);

  const memoizedElement = useMemo(() => {
    // 카운터 2가 업데이트되면 이 요소는 동일한 참조를 유지합니다.
    // 따라서 카운터 1이 변경되지 않는 한 다시 렌더링되지 않습니다.
    return <ExpensiveChildComponent />;
  }, [counter1]);

  return (
    <div>
      <button onClick={() => setCounter1(counter1 + 1)}>
        Counter 1: {counter1}
      </button>
      <button onClick={() => setCounter1(counter2 + 1)}>
        Counter 2: {counter2}
      </button>
      {memoizedElement}
    </div>
  );
}
```

개념적으로 이 두 접근 방식의 차이는 다음과 같습니다.

- `React.memo()`: 하위 컴포넌트에 의해 제어됨
- 동일 요소 참조(Same-element references): 부모 컴포넌트에 의해 제어됨

이러한 모든 기법에서 컴포넌트 렌더링을 건너뛰는 것은 리액트가 해당 하위 트리 전체의 렌더링을 건너 뛰는 것을 의미합니다. 이는 리액트가 "재귀적으로 하위을 렌더링"하는 기본 동작을 중단하기 위해 정지 표시를 효과적으로 설정하기 때문입니다.