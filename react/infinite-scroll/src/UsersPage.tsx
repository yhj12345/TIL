// import React, { useCallback, useEffect, useState } from "react";
// import { PaginationResponse, User } from "./models/user";
// import axios from "axios";
// import Loading from "./components/Loading";
// import Card from "./components/Card";
// import styled from "styled-components";

// const UserPage = () => {
//   const [page, setPage] = useState(0);
//   const [users, setUsers] = useState<User[]>([]);
//   const [isFetching, setFetching] = useState(false);
//   const [hasNextPage, setNextPage] = useState(true);

//   const fetchUsers = useCallback(async () => {
//     const { data } = await axios.get<PaginationResponse<User>>("/users", {
//       params: { page, size: 10 },
//     });
//     console.log(data);
//     setUsers(users.concat(data.contents));
//     setPage(data.pageNumber + 1);
//     setNextPage(!data.isLastPage);
//     setFetching(false);
//   }, [page]);

//   useEffect(() => {
//     const handleScroll = () => {
//       const { scrollTop, offsetHeight } = document.documentElement;
//       if (window.innerHeight + scrollTop >= offsetHeight) {
//         setFetching(true);
//       }
//     };
//     setFetching(true);
//     window.addEventListener("scroll", handleScroll);
//     return () => window.removeEventListener("scroll", handleScroll);
//   }, []);

//   useEffect(() => {
//     if (isFetching && hasNextPage) fetchUsers();
//     else if (!hasNextPage) setFetching(false);
//   }, [isFetching]);

//   return (
//     <Container>
//       {users.map((user) => (
//         <Card key={user.id} name={user.name} />
//       ))}
//       {isFetching && <Loading />}
//     </Container>
//   );
// };

// const Container = styled.div``;

// export default UserPage;

import { PaginationParams, PaginationResponse, User } from "./models/user";
import axios from "axios";
import Loading from "./components/Loading";
import Card from "./components/Card";
import styled from "styled-components";
import useDebounce from "./hooks/useDebounce";
import useThrottle from "./hooks/useThrottle";

const fetchUsers = (params: PaginationParams) =>
  axios.get<PaginationResponse<User>>("/users", { params });

const UsersPage = () => {
  // const { data: users, isFetching } = useDebounce(fetchUsers, { size: 10 });
  const { data: users, isFetching } = useThrottle(fetchUsers, { size: 10 });

  return (
    <Container>
      {users.map((user) => (
        <Card key={user.id} name={user.name} />
      ))}
      {isFetching && <Loading />}
    </Container>
  );
};

const Container = styled.div``;

export default UsersPage;
