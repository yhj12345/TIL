import ContactForm from "@/components/ContactForm";
import React from "react";
import { AiFillGithub, AiFillYoutube } from "react-icons/ai";

const LINKS = [
  { icon: <AiFillGithub />, url: "" },
  { icon: <AiFillYoutube />, url: "" },
];

const ContactPage = () => {
  return (
    <section className="flex flex-col items-center">
      <h2 className="text-3xl font-bold my-2">Contact Me</h2>
      <p>ghwnsdl999@naver.com</p>
      <ul className="flex gap-4 my-2">
        {LINKS.map((link, index) => (
          <a className="text-5xl" key={index} href={link.url}>
            {link.icon}
          </a>
        ))}
      </ul>
      <h2 className="text-3xl font-bold my-8">Or Send me an Email</h2>
      <ContactForm />
    </section>
  );
};

export default ContactPage;
