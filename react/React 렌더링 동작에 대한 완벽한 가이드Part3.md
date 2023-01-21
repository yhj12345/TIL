# React 렌더링 동작에 대한 완벽한 가이드

### 컨텍스트(Context)와 렌더링 동작

리액트의 Context API는 단일 사용자 제공 값을 컴포넌트의 하위 트리에서 사용할 수 있도록 하는 매커니즘입니다. 주어진 `<MyContext.Provider>` 내부의 모든 컴포넌트는 사이의 모든 컴포넌트를 통해 해당 값을 명시적으로 전달할 필요 없이 해당 컨텍스트 인스턴스에서 값을 읽을 수 있습니다.

컨텍스트는 "상태 관리" 도구가 아닙니다. 컨텍스트에 전달되는 값은 직접 관리해야 합니다. 이는 일반적으로 데이터를 리액트 컴포넌트 상태로 유지하고 해당 데이터를 기반으로 컨텍스트 값을 구성함으로써 수행됩니다.

#### 컨텍스트 기초

컨텍스트 공급자는 `<MyContext.Provider value={42}>`와 같이 하나의 `value` prop을 받습니다.    하위 컴포넌트는 컨텍스트 소비자 컴포넌트를 렌더링하고 다음과 같이 렌더 prop을 제공해 컨텍스트를 소비할 수 있습니다.

`<MyContext.Consumer>{(value) => <div>{value}</div>}</Mycontext.Consumer>`

또는 함수 컴포넌트에서 `useContext` 훅을 호출합니다.

`const value = useContext(MyContext)`

#### 컨텍스트 값 업데이트

리액트는 공급자를 감싸고 있는 컴포넌트가 공급자를 렌더링할 때 컨텍스트 공급자에 새 값이 제공되었는지 확인합니다. 공급자의 값이 새 참조인 경우 리액트는 값이 변경되었으며 해당 컨텍스트를 사용하는 컴포넌트를 업데이트 해야한다는 것을 알게됩니다.

다음과 같이 컨텍스트 공급자에 새 객체를 전달하면 업데이트를 유발합니다.

```react
function GrandchildComponent() {
  const value = useContext(MyContext);
  return <div>{value.a}</div>;
}

function ChildComponent() {
  return <GrandchildComponent />;
}

function ParentComponent() {
  const [a, setA] = useState(0);
  const [b, setB] = useState('text');

  const contextValue = { a, b };

  return (
    <MyContext.Provider value={contextValue}>
    <ChildComponent />
    </MyContext.Provider>
  );
}
```

이 예제에서 `ParentComponent`가 렌더링될 때마다 리액트는 `MyContext.Provider`에 새 값이  	    주어졌는지 확인하고, 아래로 순회하며 `MyContext`를 소비하는 컴포넌트를 찾습니다. 컨텍스트 공급자에 새 값이 있으면 해당 컨텍스트를 사용하는 모든 중첩된 컴포넌트가 강제로 리렌더링됩니다.

리액트의 관점에서 볼 때 각 컨텍스트 공급자는 단일 값만 가집니다. 즉, 객체, 배열 또는 원시값인 상관 없이 하나의 컨텍스트 값일 뿐입니다. 현재 컨텍스트를 소비하는 컴포넌트가 새 값의 일부만 관련되었더라도 새 컨텍스트 값으로 인한 업데이트를 건너뛸 수 있는 방법은 없습니다.

만약 컴포넌트가 오직 `value.a`만 필요하고 새로운 `value.b` 참조를 위해 업데이트가 이루어진 경우 불변하게 업데이트하는 규칙 및 컨텍스트 렌더링 규칙에 따라 해당 값도 새 참조가 되어야하므로 `value.a`를 읽는 컴포넌트도 렌더링됩니다.

#### 상태 업데이트, 컨텍스트 그리고 리렌더링

이제 이것들을 한데 모을 시간이 됐습니다. 우리는 다음을 알고 있습니다.

- `setState()` 호출은 해당 컴포넌트의 렌더링을 큐에 추가합니다.
- 리액트는 기본적으로 중첩된 컴포넌트를 순회하며 렌더링합니다.
- 컨텍스트 공급자는 이를 렌더링하는 컴포넌트에 의해 값이 지정됩니다.
- 이 값은 일반적으로 상위 컴포넌트의 상태로부터 가져옵니다.

즉, 기본적으로 컨텍스트 공급자를 렌더링하는 상위 컴포넌트에 대한 상태 업데이트는 컨텍스트 값을 읽는지 여부에 관계 없이 모든 하위 컴포넌트가 리렌더링되도록 합시다!

위의 `Parent/Child/Grandchild`의 예를 다시 살펴보면 `GrandchildComponent`가 리렌더링되지만 컨텍스트 업데이트 때문이 아니라 `ChildComponent`가 렌더링되었기 때문임을 알 수 있습니다.      이 예제에서는 "불필요한" 렌더링을 최적화하려는 작업이 없으므로 리액트는 `ParentComponent`가 렌더링될 때마다 기본적으로 `ChildComponent`와 `GrandchildComponent`를 렌더링합니다. 상위 컴포넌트가 새 컨텍스트 값을 `MyContext.Provider`에 넣는 경우 `GrandchildComponent`가 그 값을 알고 사용하게 되지만 컨텍스트 업데이트로 인해 `GrandchildComponent`가 리렌더링된 것은 아닙니다. 어쨌든 그렇게 됩니다.

#### 컨텍스트 업데이트와 렌더링 최적화

위 예제를 수정해 실제로 최적화를 해 보겠습니다. 하지만 `GreatGrandchildComponent`를 최하단에 추가해 조금 꼬아보겠습니다.

```react
function GreatGrandchildComponent() {
  return <div>Hi</div>
}

function GrandchildComponent() {
  const value = useContext(MyContext);
  return (
    <div>
    {value.a}
    <GreatGrandchildComponent />
    </div>
  )
}

function ChildComponent() {
  return <GrandchildComponent />
}

const MemoizedChildComponent = React.memo(ChildComponent);

function ParentComponent() {
  const [a, setA] = useState(0);
  const [b, setB] = useState("text");

  const contextValue = {a, b};

  return (
    <MyContext.Provider value={contextValue}>
      <MemoizedChildComponent />
    </MyContext.Provider>
  )
}
```

이제 `setA(42)`를 호출해 보겠습니다.

- `ParentComponent`가 렌더링됩니다.
- 새로운 `contextValue` 참조가 생성됩니다.
- 리액트는 `MyContext.Provider`에 새 컨텍스트 값이 있음을 확인하고, 따라서 `MyContext`의 모든 소비자를 업데이트 해야합니다.
- 리액트는 `MemoizedChildComponent`를 렌더링하려고 하지만 `React.memo()`로 감싸져 있음을 확인합니다. 전달되는 props가 하나도 없기 때문에 props는 실제로 변경되지 않았습니다.             리액트는 `ChildComponent` 렌더링을 완전히 건너뜁니다.
- 그러나 `MyContext.Provider`에  대한 업데이트가 있었습니다. 따라서 더 아래쪽에 이에 대해 알아야 할 컴포넌트가 있을 수 있습니다.
- 리액트는 계속 아래로 내려가 `GrandchildComponent`에 도달합니다. `GrandchildComponent`가 `MyContext`를 읽고 있으므로 리렌더링 해야 합니다. 새로운 컨텍스트 값이 있기 때문입니다. 리액트는 컨텍스트 변경에 따라 `GrandchildComponent`를 리렌더링합니다.
- `GrandchildComponent`가 렌더링되었기 때문에 리액트는 계속 렌더링을 진행하며 모든 하위 컴포넌트를 리렌더링 합니다. 따라서 `GreatGrandchildComponent`도 리렌더링할 것입니다.

Sophie Alpert는 다음과 같이 말했습니다.

> 컨텍스트 공급자 바로 아래에 있는 리액트 컴포넌트는 `React.memo`를 사용해야합니다.

이렇게 하면 상위 컴포넌트의 상태 업데이트가 모든 컴포넌트를 강제로 리렌더링하지 않고, 			    컨텍스트를 읽는 부분만 리렌더링합니다.(기본적으로 `ParentComponent`가 `<MyContext.Provider>{props.children}</MyContext.Provider>`를 렌더링하도록 해 동일한 결과를 얻을수도 있습니다. "동일 요소 참조" 기법을 활용해 하위 컴포넌트를 리렌더링하지 않도록 하고, 한 수준 위에서 `<ParentComponent><ChildComponet /></ParentComponent>`를 렌더링합니다.)

그러나 일단 `GrandchildComponent`가 다음 컨텍스트 값을 기반으로 렌더링되면 리액트는 순회하며 모두 렌더링하는 기본 동작으로 돌아갑니다. 그래서 `GreatGrandchildComponent`가 렌더링되었고, 그 아래에 어떤 것이 있더라도 리렌더링 되었을 것입니다.

#### 컨텍스트와 렌더러 경계(Renderer Boundaries)

일반적으로 리액트 앱은 ReactDOM이나 React Native와 같은 단일 렌더러로 빌드됩니다. 그러나 코어 렌더링 및 재조정 로직은 `react-reconciler`라는 패키지로 배포되며 다른 환경을 대상으로 하는 자체적인 버전의 리액트를 빌드할 수 있습니다. 이것의 좋은 예로 리액트를 사용해 Three.js 모델과 WebGL 렌더링을 구동하는 `react-three-fiber`와 리액트를 사용해 터미널 텍스트 UI를 그리는 `ink`가 있습니다.

한가지 오래된 한계점은 ReactDOM 컨텐츠 내부에 React-Three-Fiber를 표시하는 것과 같이 여러 렌더러를 하나의 앱에 사용하는 경우 컨텍스트 공급자가 렌더러 경계를 통과하지 않는다는 것입니다. 따라서 컴포넌트 트리가 다음과 같은 경우

```react
function App() {
  return (
    <MyContext.Provider>
      <DomComponent>
        <ReactThreeFiberParent>
          <ReactThreeFiberChild />
        </ReactThreeFiberParent>
      </DomComponent>
    </MyContext.Provider>
  );
}
```

여기서 `ReactFiberParent`는 `React-Three-Fiber`로 렌더링된 콘텐츠를 생성하고 표시합니다. 그러면 `<ReactThreeFiberChild>`는 `<MyContext.Provider>`의 값을 알 수 없습니다.

이는 리액트의 알려진 한계이며 현재 이를 해결할 공식적인 방법은 없습니다.

React-Three-Fiber를 관리하는 Poimandres는 컨텍스트 브리징을 가능하게 하는 몇가지 내부적인 핵을 갖고 있으며, 최근 유효한 해결 방법인 [`useContextBridge`훅](https://github.com/pmndrs/its-fine#useContextBridge)을 포함하는 [`its-fine`](https://github.com/pmndrs/its-fine)이라는 라이브러리를 출시했습니다.