import { createBrowserRouter } from "react-router-dom";

const router = createBrowserRouter([
  {
    path: "/",
    element: <h1>Home</h1>,
    errorElement: <h1>404</h1>,
  },
  {
    path: "/login",
    element: <h1>Login</h1>,
  },
  {
    path: "/register",
    element: <h1>Register</h1>,
  },
  {
    path: "/healthPrograms",
    element: <h1>Health Programs</h1>,
    children: [
      {
        path: "new",
        element: <h1>New Health Program</h1>,
      },
      {
        path: ":id",
        element: <h1>Health Program</h1>,
      },
      {
        path: ":id/edit",
        element: <h1>Edit Health Program</h1>,
      },
    ],
  },
  {
    path: "/patients",
    element: <h1>Patients</h1>,
    children: [
      {
        path: "new",
        element: <h1>New Patient</h1>,
      },
      {
        path: ":id",
        element: <h1>Patient</h1>,
      },
      {
        path: ":id/edit",
        element: <h1>Edit Patient</h1>,
      },
      {
        path: ":id/healthPrograms",
        element: <h1>Patient Health Programs</h1>,
      },
    ],
  },
]);

export default router;
