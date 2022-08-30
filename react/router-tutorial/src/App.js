import React from "react";
import { Routes, Route } from "react-router-dom";
import Articles from "./pages/Articles";
import Article from "./pages/Article";
import About from "./pages/About";
import Home from "./pages/Home";
import Profile from "./pages/profile";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/profiles/:username" element={<Profile />} />
      <Route path="/articles" element={<Articles />}>
        <Route path=":id" element={<Article />} />
      </Route>
    </Routes>
  );
};

export default App;
