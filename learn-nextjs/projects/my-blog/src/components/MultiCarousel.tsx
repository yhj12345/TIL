"use client";
import React from "react";

import Carousel from "react-multi-carousel";
import "react-multi-carousel/lib/styles.css";

type Props = {
  children: React.ReactNode;
};

const responsive = {
  desktop: {
    breakpoint: { max: 3000, min: 1024 },
    items: 4,
  },
  tablet: {
    breakpoint: { max: 1024, min: 464 },
    items: 3,
  },
  mobile: {
    breakpoint: { max: 464, min: 0 },
    items: 2,
  },
};

const MultiCarousel = ({ children }: Props) => {
  return (
    <Carousel infinite autoPlay itemClass="m-2" responsive={responsive}>
      {children}
    </Carousel>
  );
};

export default MultiCarousel;
