import Hero from "@/components/Hero";
import React from "react";

const TITLE_CLASS = "text-2xl font-bold text-gray-800 my-2";

const AboutPage = () => {
  return (
    <>
      <Hero />
      <section className="bg-gray-100 shadow-lg p-8 m-8 text-center">
        <h2 className={TITLE_CLASS}>Who am I?</h2>
        <p>
          개발을 사랑하는 프론트엔드 개발자 <br />
          사람과 디자인을 담는 웹앱을 만들고 있음
        </p>
        <h2 className={TITLE_CLASS}>Skills</h2>
        <p>
          React, Vue, Next <br />
          Git, Vscode
        </p>
      </section>
    </>
  );
};

export default AboutPage;
