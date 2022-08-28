### React. Hooks

#### useState 

- 상태관리
- setValue 비동기여서 조심

```react
const [value, setValue] = useState(0);
```



#### useEffect

- 컴포넌트가 렌더링될 때마다 특정 작업을 수행할 수 있도록 설정할 수 있는 Hook
- 클래스형 컴포넌트의 componentDidmount 와 componentDidUpdate를 합친 형태로 보아도 무방

```react
// 마운트 될때만 실행하고 싶을 때
useEffect(() => {
    console.log('마운트될 때만 실행됩니다')
}, []);

// 특정 값이 업데이트 될때만 실행하고 싶을 때
useEffect(() => {
    console.log(name);
}, [name]);

// 언마운트되기 전 업데이트 되기 직전에 수행
useEffect(() => {
    console.log('effect')
    console.log(name)
    return () => {
        console.log('cleanup')
        console.log(name)
    }
}, [name])
```



#### useMemo

- 함수 컴포넌트 내부에서 발생하는 연산을 최적화할 수 있다.
- 렌더링하는 과정에서 특정 값이 바뀌었을 때만 연산을 실행
- 원하는 값이 바뀌지 않았다면 이전에 연산했던 결과를 다시 사용

```react
const Average = () => {
	const [list, setList] = useState([]);
	const [number, setNumber]= useState('');
    
    const onChange = e => {
        setNumber(e.target.value);
    };
    const onInsert = () => {
        const nextList = list.concat(parseInt(number));
        setList(nextList);
        setNumber('');
    };
    // list가 바뀌었을때만 리렌더링 시 새로운 평균을 구함
    const avg = useMemo(() => getAverage(list), [list]);
};
```



#### useCallback

- useMemo와 상당히 비슷한 함수
- 렌더링 성능을 최적화해야 하는 상황에서 사용
- 만들어 놓았던 함수를 재사용

```react
// 컴포넌트가 처음 렌더링될 때만 함수 생성
const onChange = useCallback(e => {
    setNumber(e.target.value)
}, []);

// number 혹은 list가 바뀌었을때만 함수 생성
const onInsert = useCallback(() => {
    const nextList = list.concat(parseInt(number));
    setList(nextList);
    setNumber('');
}, [number, list])
```



#### useRef

- 함수 컴포넌트에서 ref를 쉽게 사용할 수 있도록 해줌

```react
const inputEl = useRef(null);

// number 혹은 list가 바뀌었을때만 함수 생성
const onInsert = useCallback(() => {
    const nextList = list.concat(parseInt(number));
    setList(nextList);
    setNumber('');
    inputEl.current.focus();
}, [number, list])
```

