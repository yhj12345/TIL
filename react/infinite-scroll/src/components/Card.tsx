import React from "react";
import { styled } from "styled-components";

const Card = ({ name }: { name: string }) => {
  return (
    <CardContainer>
      <p>{name}</p>
    </CardContainer>
  );
};

const CardContainer = styled.div`
  height: 200px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
`;

export default Card;
