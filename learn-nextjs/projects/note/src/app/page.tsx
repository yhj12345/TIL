import Counter from "@/components/Counter";
import os from "os"; // 노드 APIS

export default function Home() {
  console.log(os.hostname());

  return (
    <>
      <Counter />
      <h1>홈페이지다!</h1>
    </>
  );
}
