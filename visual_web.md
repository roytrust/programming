## JavaScript
* Tryout: http://jsbin.com/
* onClick, onChange, event.target.value
* Spread operator {...userInput} 
* Prevent default submit: `event.preventDefault()`
* template literal: ``` `${}` ```
* `'use strict'`
* `localStorage.setItem('key', 'value'); localStorage.getItem('key'); removeItem()`
* `id=setTimeout((), 500) // milliseconds; clearTimeout(id)`
* [Destructing](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment): `const {a: aa, b: bb} = obj`

## React
* [Example](https://github.com/roytrust/React/tree/main/Section%208/code/08-finished)
* Pass state data via props. Lifting state up
* props.children, 
* sate: `const [var, setVar] = useState(var)`. state scheduling and batching.
* states depend on the previous states, use function: `setUser((prevState) => {return {...prevState, title: event.target.value}})`
* Two-way binding (gather, change): `value={var}`
* Alway have a key when mapping array
* React DevTools
* React.Fragment or <>.
* Render backdrop/modal/overlay: `{ReactDOM.createPortal(<Backdrop onConfirm={props.onConfirm} />, document.getElementById('backdrop-root'))}`
* Refs: `useRef(); ref.current; createRef()`
* [Side effects](https://github.com/roytrust/React/blob/main/Section%2011/code/12-finished/src/components/Layout/HeaderCartButton.js): when dependencies change, response to sth: `useEffect(() => {...}, [ dependencies ]);`. Cleanup function: before next run or remove: return ().
* Update-state depdends on other states: `const [state, dispatchFn] = userReducer(reducerFn, initialState, initFn);`. reducerFn: (prevState, action)=>newState
* [Context](https://github.com/roytrust/React/tree/main/Section%2010/code/13-finished). `React.createContext({}); ctx=useContext(); <Provider value={}; <Consumer>{(ctx)=>{return ()}}`; 
* Forward refs (rare, focus input): `useImperativeHandle(, ()); React.forwardRef()`
* handler bind ()
* Component re-evaluate/re-execute, virtual comparison. Prevent unnecessary re-eval: `export default React.memo(funcComp); useCallback(func, [deps]); useMemo(func, [deps] // memo data`


* Class-based component: `constructor() {this.state={};}; this.setState({}) // will merge; `. componentDidMount(), componentDidUpdate(), componentWillUnmount(). `static contextType=usersContext; this.context.users`.



## CSS
* `@media`
* 

## VScode
* Extensions: ESLint, Prettier
* 

## References
* [Modal](https://github.com/roytrust/React/blob/main/Section%2011/code/12-finished/src/components/UI/Modal.js)
* 
