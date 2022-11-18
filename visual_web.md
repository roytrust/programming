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
* fetch returns promise: `fetch('https://swapi.dev/api/people/1/').then((response) => response.json()).then((data) => console.log(data));`. `method: 'POST', body: JSON.stringify({}), headers: {'Content-Type': 'application/json'}`
* async, await
* `for (const key in data) {}`
* check if set: `obj.a ? 'set': 'not-set'`
* 

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
* Custom hooks: useName(). 
* [Send http request, api, hook](https://github.com/roytrust/React/blob/main/Section%2020/code/21-finished/src/hooks/use-http.js)
* [Lazy loading, optimize, Suspense](https://github.com/roytrust/React/tree/main/Section%2021): `NewQuote = React.lazy(() => import('./pages/NewQuote'));`
* [Authentication](https://github.com/roytrust/React/tree/main/Section%2022)
* 


* Class-based component: `constructor() {this.state={};}; this.setState({}) // will merge; `. componentDidMount(), componentDidUpdate(), componentWillUnmount(). `static contextType=usersContext; this.context.users`. 
* [Error boundary](https://github.com/roytrust/React/blob/main/Section%2013/code/08-finished/src/components/ErrorBoundary.js): `componentDidCatch(); return this.props.children`

### Tips
* Reducer must be pure, side-effect free, synchronous functions.
* Never mutate Redux state directly.
* UseEffect can't be async, but it can create an async func inside.

### [Redux](https://github.com/roytrust/React/tree/main/Section%2018/code/12-finished/src/store)
* redux, react-redux, `import { useSelector, useDispatch } from 'react-redux'`
* [Class based component](https://github.com/roytrust/React/blob/main/Section%2018/code/05-redux-with-class-based-cmp/src/components/Counter.js): `export default connect(mapStateToProps, mapDispatchToProps)(class-component)`
* [Side effect, async tasks, Redux](https://github.com/roytrust/React/tree/main/Section%2019):`import { createSlice, configureStore } from '@reduxjs/toolkit';`
* 

### [React router](https://github.com/roytrust/React/tree/main/Section%2020)
* react-router-dom, Route, BrowserRouter, Link, NavLink, Switch exact, Redirect, useParams, useRouteMatch 
* `<NavLink activeClassName={classes.active} to='/welcome'>Welcome</NavLink>`. 
* Programmatic navigation: `history=useHistory(); history.push('/')`
* [Prompt unwanted route or lost form data](https://github.com/roytrust/React/blob/main/Section%2020/code/21-finished/src/components/quotes/QuoteForm.js#L35)
* [Working with query parameters](https://github.com/roytrust/React/blob/main/Section%2020/code/21-finished/src/components/quotes/QuoteList.js): ```location = useLocation(); queryParams = new URLSearchParams(location.search); queryParams.get('sort'); history.push({pathname: location.pathname, search: `sort=${(isSortingAscending ? 'desc' : 'asc')}`});```
* [Nested routes feature to conditionally render differrent content based on the URL](https://github.com/roytrust/React/blob/main/Section%2020/code/21-finished/src/pages/QuoteDetail.js): `<Route path={match.path} exact>; ` 
* V6: Switch->Routes, element, best path, Nest route (wrap, relative, Outlet), useHistory->useNavigate  
  * activeClassName: `className={navData => navData.isActive ? classes.active : '' }`
  * Redirect->Navigate: `<Route path='/' element={<Navigate replace to='/quotes' />} />`
* V6.4 (data load/fetch): loader, useLoaderData, RouterProvider, createBrowserRouter, createRoutesFromElements, userActionData, useNavigation().state
  * [Better fetching, defer, wait](https://github.com/roytrust/React/blob/main/Section%2020/react-router-6.4-intro-react-router-6.4-adv/src/pages/DeferredBlogPosts.jsx)
  * [useFetcher](https://github.com/roytrust/React/blob/main/Section%2020/react-router-6.4-intro-react-router-6.4-adv/src/components/NewsletterSignup.jsx)

### [Next.js](https://github.com/roytrust/React/tree/main/Section%2023)


## CSS
* `@media`
* [Spinner](https://github.com/roytrust/React/blob/main/Section%2020/code/21-finished/src/components/UI/LoadingSpinner.module.css)
* 

## VScode
* Extensions: ESLint, Prettier
* 

## References
* [Modal](https://github.com/roytrust/React/blob/main/Section%2011/code/12-finished/src/components/UI/Modal.js)
* Form lib: formik
* Experiment: firebase - google
* 
