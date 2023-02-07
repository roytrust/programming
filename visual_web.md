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
* Start: create react app.
* VS code: Prettier, 
* [Basic Example](https://github.com/roytrust/React/tree/main/Section%208/code/08-finished). [Redux, Context, Custom hooks](https://github.com/roytrust/React/tree/main/Section%2025)
* Pass state data via props. Lifting state up
* props.children, 
* Two-way binding (gather, change): `value={var}`
* Alway have a key when mapping array
* React DevTools
* React.Fragment or <>.
* Render backdrop/modal/overlay: `{ReactDOM.createPortal(<Backdrop onConfirm={props.onConfirm} />, document.getElementById('backdrop-root'))}`
* Get the value/state: `useRef(); ref.current; createRef()`
* [Update-state depdends on other states](https://github.com/roytrust/React/blob/main/Section%2028/code/14-finished/src/components/Ingredients/Ingredients.js): `const [state, dispatchFn] = userReducer(reducerFn, initialState, initFn);`. reducerFn: (prevState, action)=>newState
  * React will re-render the component whenever your reducer returns the new state.
* [Context](https://github.com/roytrust/React/tree/main/Section%2010/code/13-finished). `React.createContext({}); ctx=useContext(); <Provider value={}; <Consumer>{(ctx)=>{return ()}}`; 
* Forward refs (rare, focus input): `useImperativeHandle(, ()); React.forwardRef()`
* handler bind ()
*[Component re-evaluate/re-execute, virtual comparison](https://dmitripavlutin.com/use-react-memo-wisely/). Prevent unnecessary re-eval: `export default React.memo(funcComp); useCallback(func, [deps]); useMemo(func, [deps] // memo data`
* [Lazy loading, optimize, Suspense](https://github.com/roytrust/React/tree/main/Section%2021): `NewQuote = React.lazy(() => import('./pages/NewQuote'));`
* [Authentication](https://github.com/roytrust/React/tree/main/Section%2022)
* [Error Model](https://github.com/roytrust/React/blob/main/Section%2028/code/14-finished/src/components/UI/ErrorModal.js)


* Class-based component: `constructor() {this.state={};}; this.setState({}) // will merge; `. componentDidMount(), componentDidUpdate(), componentWillUnmount(). `static contextType=usersContext; this.context.users`. 
* [Error boundary](https://github.com/roytrust/React/blob/main/Section%2013/code/08-finished/src/components/ErrorBoundary.js): `componentDidCatch(); return this.props.children`
* [Animation: react-transition-group](https://github.com/roytrust/React/tree/main/Section%2024). React motion

### Hooks
* Hooks are special functions that can only be used in functional components (and custom hooks).

* State: `const [var, setVar] = useState(var)`. state scheduling and batching.
* states depend on the previous states, use function: `setUser((prevState) => {return {...prevState, title: event.target.value}})`

* useEffect: Manage anything besides render flow, executed after each render cycle. 
  * useEffect() acts like componentDidUpdate: It runs the function AFTER EVERY component update (re-render). 
  * with [] as a second argument, useEffect() acts like componentDidMount: It runs ONLY ONCE (after the first render).
  * [Side effects](https://github.com/roytrust/React/blob/main/Section%2011/code/12-finished/src/components/Layout/HeaderCartButton.js): when dependencies change, response to sth: `useEffect(() => {...}, [ dependencies ]);`. 
  * Cleanup function: before next run or remove: return (). If you have [] as dependencies (i.e. the effect only runs once), the cleanup function runs when the component gets unmounted.
  * [setTimer example](https://github.com/roytrust/React/blob/main/Section%2028/code/14-finished/src/components/Ingredients/Search.js)
* [Custom hooks](https://github.com/roytrust/React/blob/main/Section%2028/code/14-finished/src/hooks/http.js) - re-run in reder cycle - change component states: useName(). 
* [Send http request, api, hook](https://github.com/roytrust/React/blob/main/Section%2020/code/21-finished/src/hooks/use-http.js)


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
* [Selectors](https://www.w3schools.com/cssref/css_selectors.php)
* [Pseudo classes/selectors](https://www.w3schools.com/css/css_pseudo_classes.asp)
* [Pseudo elements](https://www.w3schools.com/css/css_pseudo_elements.asp)
* [Spinner](https://github.com/roytrust/React/blob/main/Section%2020/code/21-finished/src/components/UI/LoadingSpinner.module.css). [React example](https://github.com/roytrust/React/blob/main/Section%2028/code/14-finished/src/components/UI/LoadingIndicator.js)
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
* Make wrap around: `float: left`
* Box model: `box-sizing: border-box`. content-box. 
* Outlines: `outline: 6px solid black`; outline-offset: 10px`
* Text Shadows (x y blur color): `text-shadow: 2px 2px 5px red` 
* Move back/forth: `z-index: -1`
* [Transition triggered by events](https://www.w3schools.com/css/css3_transitions.asp) - Smooth transitions: `transition: background-color 2s, color 5s, padding 1s`
* __linear gradient__ goes from side to side: `background-image: linear-gradient(to right, black, yellow)`. 45deg. [gradient generator](https://cssgradient.io/) 
* [Web fonts](https://fonts.google.com/)
* [Transformations](https://www.w3schools.com/cssref/css3_pr_transform.php). Move: `transform: translate(100px, 100px)`. `transform: roteate(20deg); transform: sacle(2); transform: skew(20deg, 20deg)`
* [Animations - move without event](https://www.w3schools.com/css/css3_animations.asp): `position: absolute; animation-name: slideMe; animation-duration: 4s; animation-iteration-count: infinite; animation-direction: alternate;`. `@keyframes slideMe {from {top: 0; left: 0;} to {left: 100%;}}`
* [Layout Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) - flex-wrap, flex-grow, flex-shrink: `display: flex; flex-basis: 50%`
* [Layout grid](https://www.w3schools.com/css/css_grid.asp) - row, column, gutter/gap: `display: grid; grid-template-columns: auto auto auto;

### [Position: relative, absolute, fixed, sticky](https://www.w3schools.com/css/css_positioning.asp)
* Relative - move off from usual position
* Absolute - relative position to the parent
* Fixed - position to viewpoint, stays when page scrolling
* Sticky - as fixed but position to parent, needs top e.g. to tell where to position.
* top, right, bottom, left 
* Overflowing - hidden, visible, auto: `overflow: auto` 
* Centering block elements: `margin-left: auto; margin-right: auto`

### [Responsive Web Design](https://www.w3schools.com/css/css_rwd_intro.asp)
* `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
* Media query: `@media (max-width: 640px) {}`
* [Aspect Ratio Boxes](https://css-tricks.com/aspect-ratio-boxes/)


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
