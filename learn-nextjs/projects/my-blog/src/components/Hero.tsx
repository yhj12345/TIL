import Image from "next/image";
import profileImgae from "../../public/images/profile.jpg";
import Link from "next/link";

const Hero = () => {
  return (
    <div className="text-center">
      <Image
        className="mx-auto rounded-full w-40 h-40"
        src={profileImgae}
        alt="Picture of the author"
        priority
      />
      <h2 className="text-3xl font-bold mt-2">{"Hi, I'm HJ"}</h2>
      <h3 className="text-xl font-semibold">Frontend Engineer</h3>
      <p>꿈을 코딩하는 사람</p>
      <Link href="/contact">
        <button className="bg-yellow-500 font-bold rounded-xl py-1 px-4 mt-2">
          Contact Me
        </button>
      </Link>
    </div>
  );
};

export default Hero;
