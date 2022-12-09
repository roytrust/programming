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
* [Jest - JavaScript test](https://jestjs.io/)

## React
* [Basic Example](https://github.com/roytrust/React/tree/main/Section%208/code/08-finished). [Redux, Context, Custom hooks](https://github.com/roytrust/React/tree/main/Section%2025)
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
* [Animation: react-transition-group](https://github.com/roytrust/React/tree/main/Section%2024). React motion

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

### [Test](https://github.com/roytrust/React/tree/main/Section%2026)
* Arrange, act, assert: `test(desc, func); screen.getByText(); expect(Elem).toBeInTheDocument(); screen.queryByText(); expect().toBeNull()`. Test Suites: `describe()`
* Test Asynchronous: `async, await; expect().not.toHaveLength(0)`
* Mocks: `windows.fetch = jest.fn(); window.fetch.mockResolvedValueOnce({json: async ()=> []})`
* https://jestjs.io/
* [React testing libs](https://testing-library.com/docs/react-testing-library/intro/)

## CSS
* [CSS CheatSheet](https://htmlcheatsheet.com/css/)
* `@media`
* [Spinner](https://github.com/roytrust/React/blob/main/Section%2020/code/21-finished/src/components/UI/LoadingSpinner.module.css)
* `import classes from "./ex.module.css"; <div className={classes.div}>`
* React inline: `<div style={{margin: "10px"}}>`
* [classnames for React](https://www.npmjs.com/package/classnames)
* Make shape: `border-radius:10px`
* Display: block, inline, inline-block: `display: inline`
* Box shadows (x y blur inset color): `box-shadow: 2px 2px 15px red`. Inside: `ox-shadow: 2px 2px 15px inset red`
* Padding - inside (top right bottom left)
* Margin - outside. To center: `margin: auto` 
* max-width - work with inline
* Opacity: `opacity: 0.5`. `rgba(0, 0, 0, 0.5)`
* External css: `<link rel="stylesheet" href=""/>
* Float elements
* Box model: `box-sizing: border-box`. content-box. 
* Outlines: `outline: 6px solid black`; outline-offset: 10px`
* Text Shadows (x y blur color): `text-shadow: 2px 2px 5px red` 

### Position: relative, absolute, fixed, sticky
* Relative - move off from usual position
* Absolute - relative position to the parent
* Fixed - position to viewpoint, stays when page scrolling
* Sticky - as fixed but position to parent, needs top e.g. to tell where to position.
* top, right, bottom, left 

## Tools
### yarn
* Check installed package version: `yarn why pkg`
* Check the latest version of a package: `yarn outdated pkg`
* Check a package (even not installed): `yarn info pkg`


### VScode
* Extensions: ESLint, Prettier
* 

## [TypeScript](https://github.com/roytrust/React/tree/main/Section%2027)
* type aliases, type union, inference, 
* Generics: `func<T>(array: T[], value: T){}`
* React comp: `const func: React.FC<{items: string[]}> = (props) => {}`. `React.FormEvent; useRef<HTMLInputElement>(null); ref.current?.value; ref.current!.value`
* `React.FC<{onAdd: (text: string) => void}>; useState<ToDo[]>([])`
* [Create react typescript](https://create-react-app.dev/docs/adding-typescript/)
* tsconfig.json

## References
* [Modal](https://github.com/roytrust/React/blob/main/Section%2011/code/12-finished/src/components/UI/Modal.js)
* Form lib: formik
* Experiment: firebase - google
* [{JSON} Placeholder: Free fake API for testing and prototyping](https://jsonplaceholder.typicode.com/)
* [React with TypeScript: Best Practices](https://www.sitepoint.com/react-with-typescript-best-practices/)
* [react-typescript-cheatsheet](https://github.com/typescript-cheatsheets/react-typescript-cheatsheet)
* 
