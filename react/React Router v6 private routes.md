## React Router v6: private routes

##### 경로 설정과 경로로 갈 수 있는 링크

```react
// App.js
import { Routes, Route, Link } from 'react-router-dom';

 const App = () => {
  return (
    <>
      <h1>React Router</h1>

      <Navigation />

      <Routes>
        <Route index element={<Landing />} />
        <Route path="landing" element={<Landing />} />
        <Route path="home" element={<Home />} />
        <Route path="dashboard" element={<Dashboard />} />
        <Route path="analytics" element={<Analytics />} />
        <Route path="admin" element={<Admin />} />
        <Route path="*" element={<p>404 NOT FOUND</p>} />
      </Routes>
    </>
  );
};

const Navigation = () => (
  <nav>
    <Link to="/landing">Landing</Link>
    <Link to="/home">Home</Link>
    <Link to="/dashboard">Dashboard</Link>
    <Link to="/analytics">Analytics</Link>
    <Link to="/admin">Admin</Link>
  </nav>
);
```



##### 간단한 컴포넌트 구성

Landing을 제외한 모든 경로는 무단 접근으로부터 보호하고 각 페이지마다 다른 인증 매커니즘을 가집니다.

```react
const Landing = () => {
  return <h2>Landing (Public: 누구나 사용할 수 있는 페이지)</h2>;
};

const Home = () => {
  return <h2>Home (Protected: 로그인 필요)</h2>;
};

const Dashboard = () => {
  return <h2>Dashboard (Protected: 로그인 필요)</h2>;
};

const Analytics = () => {
  return (
    <h2>
      Analytics (Protected: 로그인과 'analyze'권한 필요)
    </h2>
  );
};

const Admin = () => {
  return (
    <h2>
      Admin (Protected: 로그인과 'admin'권한 필요)
    </h2>
  );
};
```



##### 로그인/로그아웃 매커니즘 시뮬레이션

조건부로 렌더링된 두 개의 버튼을 사용하여 사용자의 인증 상태에 때라 로그인 또는 로그아웃 버튼을 렌더링합니다.

```react
const App = () => {
  const [user, setUser] = React.useState(null);

  const handleLogin = () => setUser({ id: '1', name: 'robin' });
  const handleLogout = () => setUser(null);

  return (
    <>
      <h1>React Router</h1>

      <Navigation />

      {user ? (
        <button onClick={handleLogout}>Sign Out</button>
      ) : (
        <button onClick={handleLogin}>Sign In</button>
      )}

      <Routes>
        <Route index element={<Landing />} />
        <Route path="landing" element={<Landing />} />
        <Route path="home" element={<Home user={user} />} />
        ...
      </Routes>
    </>
  );
};
```



##### Home 경로 Private 설정

로그인한 정보를 prop해주는데 만약 정보가 없다면 다시 Navigate 해준다.

```react
import { Routes, Route, Link, Navigate } from 'react-router-dom';

...

const Home = ({ user }) => {
  if (!user) {
    return <Navigate to="/landing" replace />;
  }

  return <h2>Home (Protected: authenticated user required)</h2>;
};
```



##### pivate 확장

위의 방법대로 하면 모든 페이지마다 써주어야하기 때문에 확장을 하기 위해서 ProtectedRoute를 만들고 필요한 페이지에 씌워준다.

```react
// protectedRoute
const ProtectedRoute = ({ user, children }) => {
  if (!user) {
    return <Navigate to="/landing" replace />;
  }

  return children;
};

// App.js
const App = () => {
  ...

  return (
    <>
      ...

      <Routes>
        <Route index element={<Landing />} />
        <Route path="landing" element={<Landing />} />
        <Route
          path="home"
          element={
            <ProtectedRoute user={user}>
              <Home />
            </ProtectedRoute>
          }
        />
        ...
      </Routes>
    </>
  );
};

const Home = () => {
  return <h2>Home (Protected: authenticated user required)</h2>;
};
```



##### 각 페이지마다 다른 페이지로 redirect를 하고 싶을 때

```react
const ProtectedRoute = ({
  user,
  redirectPath = '/landing',
  children,
}) => {
  if (!user) {
    return <Navigate to={redirectPath} replace />;
  }

  return children;
};
```



##### 각 페이지마다 ProtectedRoute 설정

경로마다 ProtectedRoute를 씌워주면 각 페이지마다 권한 여부를 따질 수 있다.

```react
const App = () => {
  ...

  return (
    <>
      ...

      <Routes>
        <Route index element={<Landing />} />
        <Route path="landing" element={<Landing />} />
        <Route
          path="home"
          element={
            <ProtectedRoute user={user}>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route
          path="dashboard"
          element={
            <ProtectedRoute user={user}>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        <Route path="analytics" element={<Analytics />} />
        <Route path="admin" element={<Admin />} />
        <Route path="*" element={<p>There's nothing here: 404!</p>} />
      </Routes>
    </>
  );
};
```



##### ProtectedRoute 확장

Outlet을 사용하영

```react
import {
  Routes,
  Route,
  Link,
  Navigate,
  Outlet,
} from 'react-router-dom';

const ProtectedRoute = ({ user, redirectPath = '/landing' }) => {
  if (!user) {
    return <Navigate to={redirectPath} replace />;
  }

  return <Outlet />;
};

const App = () => {
  ...

  return (
    <>
      ...

      <Routes>
        <Route index element={<Landing />} />
        <Route path="landing" element={<Landing />} />
        <Route element={<ProtectedRoute user={user} />}>
          <Route path="home" element={<Home />} />
          <Route path="dashboard" element={<Dashboard />} />
        </Route>
        <Route path="analytics" element={<Analytics />} />
        <Route path="admin" element={<Admin />} />
        <Route path="*" element={<p>There's nothing here: 404!</p>} />
      </Routes>
    </>
  );
};
```



##### 