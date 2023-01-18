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

#### Props 참조가 렌더링 최적화에 미치는 영향

기본적으로 리액트는 props가 변경되지 않은 경우에도 중첩된 모든 컴포넌트를 리렌더링한다는 것을 앞서 확인했습니다. 또한 이는 하위 컴포넌트에 새로운 참조를 props로 전달하는 것이 중요하지 않다는 것을 의미하는데, 동일한 props를 전달하는지와 관계 없이 렌더링될 것이기 때문입니다.           그래서 다음과 같은 경우도 아무 문제 없습니다.

```react
function ParentComponent() {
  const onClick = () => {
    console.log('Button clicked');
  };

  const data = { a: 1, b: 2 };

  return <NormalChildComponent onClick={onClick} data={data} />;
}
```

`ParentComponent`는 렌더링할 때마다 새 `onClick` 함수 참조와 새 `data` 객체 참조를 만들어 `NormalChildComponent`의 props로 전달합니다. 

또한 이는 `<div>`나 `<button>`과 같은 "호스트 컴포넌트(host components)"를 `React.memo()`로 래핑해 렌더링을 최적화하려는 것이 의미 없음을 뜻합니다. 이러한 기본 컴포넌트는 어차피 하위 컴포넌트가 없기 때문에 렌더링 프로세스는 여기서 중단됩니다.

그러나 하위 컴포넌트가 props가 변경되었는지 확인해 렌더링을 최적화하려고 하는 경우 새 참조를 props로 전달하면 하위 컴포넌트의 렌더링을 유발할 수 있습니다. 새 props 참조가 실제로 새 데이터인 경우는 괜찮습니다. 그러나 상위 컴포넌트가 콜백 함수를 전달하는 경우는 어떨까요?

```react
const MemoizedChildComponent = React.memo(ChildComponent);

function ParentComponent() {
  const onClick = () => {
    console.log('Button clicked');
  };

  const data = { a: 1, b: 2 };

  return <MemoizedChildComponent onClick={onClick} data={data} />;
}
```

`ParentComponent`가 렌더링할 때마다 새 참조로 인해 `MemoizedChildComponent`가 props가 변경되었다고 보고 리렌더링하게됩니다. 비록 `onClick` 함수와 `data` 객체가 기본적으로 매번 같더라도 말입니다!

이는 다음을 의미합니다.

- 대부분의 경우 렌더링을 건너뛰길 원했지만 `MemoizedChildComponent`는 항상 리렌더링됩니다.
- 이전 props와 새 props를 비교하기 위해 하는 작업은 의미가 없어졌습니다.

마찬가지로 `<MemoizedChild><OtherComponent /></MemoizedChild>`를 렌더링하면 항상 하위 컴포넌트 *또한* 렌더링하게 됩니다. 왜냐하면 `prop.children`은 항상 새로운 참조이기 때문입니다.

#### Props 참조 최적화

클래스 컴포넌트는 항상 동일 참조인 인스턴스 메서드를 가질 수 있기 때문에 실수로 새 콜백 함수 참조를 만드는 것을 크게 걱정할 필요가 없습니다. 그러나 개별 하위 리스트 아이템에 대해 고유한 콜백을 생성하거나 익명 함수에서 값을 캡처해 하위 컴포넌트에 전달해야 할 수 있습니다. 그러면 새 참조를 생성하고 렌더링중 하위 컴포넌트의 props로 새 객체를 생성하게 됩니다. 리액트에는 이러한 경우를 최적화하는데 도움이 되는 것을 제공하지 않습니다.

함수 컴포넌트의 경우 리액트는 동일한 참조를 재사용할 수 있도록 두개의 훅을 제공합니다. 즉, 객체를 만들거나 복잡한 계산을 수행하는 것과 같은 모든 종류의 일반적인 데이터를 위한 `useMemo`와 콜백 함수를 만드는데 사용할 수 있는 `useCallback`입니다.

#### 전부 메모이제이션할까요?

앞서 언급한 바와 같이 props로 내려주는 모든 함수나 객체에 대해 `useMemo`와 `useCallback`을 사용하지 않아도 됩니다. 단지 그것이 하위 컴포넌트를 다르게 동작하게 만드는 경우에 한합니다.(즉, `useEffect`의 종속성 배열 비교는 하위 컴포넌트가 일관된 props 참조를 받을 필요가 있게 하는 또 다른 상황을 추가하므로 상황을 더욱 복잡하게 만듭니다.)

항상 등장하는 또 다른 질문은 "왜 리액트는 기본적으로 모든 컴포넌트를 `React.memo()`로 래핑하지 않나요?"입니다.

Dan Abramov는 메모이제이션 하더라도 props를 비교하는 비용이 발생하며, 컴포넌트는 항상 새로운 props를 받기 때문에 메모이제이션 체크로는 리렌더링을 막을 수 없는 경우가 많다고 거듭 지적했습니다. 

#### 불변성(Immutability)과 리렌더링

리액트의 상태 업데이트는 항상 불변하게 수행되어야 합니다. 그 이유는 크게 두가지가 있습니다. 	 

- 변경한 내용과 위치에 따라 렌더링할 것으로 예상한 컴포넌트가 렌더링되지 않을 수 있습니다.
- 데이터가 실제로 업데이트된 시기와 원인에 대해 혼란을 일으킵니다.

몇 가지 구체적인 예를 살펴보겠습니다.

지금까지 살펴본 바와 같이 `React.mem / PureComponent / shouldComponentUpdate`는 모두 현재 props와 이전 `props`의 얕은 비교에 의존합니다. 따라서 props가 새로운 값인지 아닌지는 `props.someValue !== prevProps.someValue`를 통해 알 것으로 예상할 수 있습니다.

만약 변경한 `someValue`가 동일한 참조를 갖는다면 컴포넌트는 아무것도 변경되지 않았다고 가정할 것입니다.

이는 특히 불필요한 리렌더링을 방지해 성능을 최적화 하려는 경우 중요합니다. 렌더링은 props가 변경되지 않은 경우 "불필요"하거나 "낭비"됩니다. 변경(mutate)을 하면 컴포넌트가 아무것도 변경되지 않았다고 착각할 수 있고, 컴포넌트가 왜 리렌더링되지 않았는지 모르게될 수 있습니다.

다른 문제는 `useState`와 `useReducer` 훅입니다. `setCounter()`나 `dispatch()`를 호출할 때 마다 리액트는 리렌더링을 큐에 추가합니다. 그러나 리액트에서는 모든 훅의 상태 업데이트가 새 객체/배열 참조 또는 새 원시값(string, number 등)인지 여부에 관계 없이 새 참조로 새 상태 값으로	 전달/반환 되어야 합니다.

리액트는 렌더 단계에서 모든 상태 업데이트를 적용합니다. 리액트가 훅에서 상태 업데이트를 적용할 때 새 값이 동일한 참조인지 확인합니다. 리액트는 항상 업데이트를 큐에 넣은 컴포넌트 렌더링을 완료합니다. 그러나 값이 이전과 동일한 참조이고 렌더링을 계속할 다른 이유(예: 상위 컴포넌트가 렌더링한 경우)가 없는 경우 리액트는 컴포넌트에 대한 렌더링 결과를 버리고 렌더 패스에서 완전히 빠져나갑니다. 따라서 다음과 같이 배열을 변경하면 

```react
const [todos, setTodos] = useState(someTodosArray);

const onClick = () => {
  todos[3].completed = true;
  setTodos(todos);
};
```

컴포넌트가 리렌더링되지 않습니다.

(리액트는 실제로 [상태 업데이트를 큐에 추가*하기 전에* 새로운 값을 확인하려고 시도하는 "빠른 경로(fast path)" 구제 메커니즘](https://github.com/facebook/react/blob/v18.0.0/packages/react-reconciler/src/ReactFiberHooks.new.js#L2234-L2259)을 가지고 있습니다. 이 역시 직접 참조 검사에 의존하므로 불변하게 업데이트 해야하는 또 다른 예입니다.)

기술적으로 가장 바깥 참조만 불변하게 업데이트 하면 됩니다. 위 예제를 다음과 같이 바꿀 수 있습니다.

```react
const onClick = () => {
  const newTodos = todos.slice();
  newTodos[3].completed = true;
  setTodos(newTodos);
};
```

새로운 배열 참조를 만들어 전달하면 컴포넌트가 리렌더링됩니다.

클래스 컴포넌트의 `this.setState()`와 함수 컴포넌트의 `useState` 그리고 `useReducer` 훅 	                 사이에는 변경 및 리렌더링과 관련한 동작에 뚜렷한 차이가 있습니다. `this.setState()`는 변경과 관계없이 항상 리렌더링을 완료합니다. 따라서 다음의 경우 리렌더링됩니다.

```react
const { todos } = this.state;
todos[3].completed = true;
this.setState({ todos });
```

`this.setState({})`와 같이 빈 객체를 전달하는 것도 마찬가지 입니다.

모든 실제 렌더링 동작 외에도 뮤테이션(mutation)은 리액트의 표준 단방향 데이터 흐름에 혼란을 초래합니다. 뮤테이션은 다른 코드들이 전혀 변하지 않았을 때 다른 값을 보게 할 수 있습니다. 		    따라서 주어진 상태의 일부가 실제로 업데이트되어야 하는 시기와 이유, 변경 사항이 어디에서 발생했는지 알 수 없게 만듭니다.

결론: 리액트 및 리액트 생태계의 나머지 부분은 불변하게 업데이트 되는 것을 가정합니다.				                 뮤테이션을 할 때마다 버그가 발생할 위험이 있습니다. 하지 마세요.

### 리액트 컴포넌트 렌더링 성능 측정

[React DevTools Profiler](https://reactjs.org/blog/2018/09/10/introducing-the-react-profiler.html)를 사용해 각 커밋에서 렌더링되는 컴포넌트를 확인합니다. *예기치 않게 렌더링되는 컴포넌트를 찾고, 개발자 도구(DevTools)를 사용해 렌더링 원인*을 파악한 후 `React.memo()`로 감싸거나 상위 컴포넌트가 전달하는 props를 메모하도록 수정하세요.

또한 리액트는 개발 빌드에서 훨씬 더 느리게 실행된다는 것을 기억하세요. 개발 모드에서 앱을 프로파일링해 렌더링하는 컴포넌트를 *확인하고* 컴포넌트를 렌더링하는데 필요한 *상대적* 시간을 서로 비교할 수 있습니다.(이 커밋에서 "컴포넌트 B"는 "컴포넌트 A"보다 3배 더 오래걸렸습니다" 와 같이) 그러나 리액트 개발 빌드를 사용해 절대적인 렌더링 시간을 측정하지 마세요. 프로덕션 빌드를 사용해서만 절대 시간을 측정하세요!(그렇지 않으면 Dan Abramov가 정확하지 않은 측정값을 사용했다고 당신에게 호통칠 것입니다.) 실제로 프로파일러를 사용하여 프로덕션과 유사한 빌드에서 타이밍 데이터를 캡처하려면 리액트의 [특별한 "프로파일링" 빌드](https://kentcdodds.com/blog/profile-a-react-app-for-performance)를 사용해야 합니다.