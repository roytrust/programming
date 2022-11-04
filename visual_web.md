## JavaScript
* Tryout: http://jsbin.com/
* onClick, onChange, event.target.value
* Spread operator {...userInput} 
* Prevent default submit: `event.preventDefault()`
* template literal: ``` `${}` ```
* `'use strict'`
* 

## React
* [Example](https://github.com/roytrust/React/tree/main/Section%208/code/08-finished)
* Pass state data via props. Lifting state up
* props.children, 
* sate: `const [var, setVar] = useState(var)`
* states depend on the previous states: `setUser((prevState) => {return {...prevState, title: event.target.value}})`
* Two-way binding (gather, change): `value={var}`
* Alway have a key when mapping array
* React DevTools
* React.Fragment or <>.
* Render backdrop/modal/overlay: `{ReactDOM.createPortal(<Backdrop onConfirm={props.onConfirm} />, document.getElementById('backdrop-root'))}`
* Refs: `useRef(); ref.current; createRef()`
* Side effects: `useEffect(() => {...}, [ dependencies ]);`
* 

## CSS
* `@media`
* 

## VScode
* Extensions: ESLint, Prettier
* 
