import React from "react";
import { Routes, Route } from "react-router-dom";
import Articles from "./pages/Articles";
import Article from "./pages/Article";
import About from "./pages/About";
import Home from "./pages/Home";
import Profile from "./pages/profile";
import NotFound from "./pages/NotFound";
import Layout from "./Layout";
import Login from "./pages/Login";
import MyPage from "./pages/MyPage";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/profiles/:username" element={<Profile />} />
      </Route>
      <Route path="/articles" element={<Articles />}>
        <Route path=":id" element={<Article />} />
      </Route>
      <Route path="/login" element={<Login />} />
      <Route path="/mypage" element={<MyPage />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
};

export default App;
