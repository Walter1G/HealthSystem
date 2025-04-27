import { createBrowserRouter } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import PatientsPage from "./pages/PatientsPage";
import PatientFormPage from "./pages/PatientFormPage";
import HealthProgramsPage from "./pages/HealthProgramsPage";
import HealthProgramFormPage from "./pages/HealthProgramFormPage";
import SeverityPage from "./pages/SeverityPage";
import SeverityFormPage from "./pages/SeverityFormPage";
import DashboardLayout from "./components/layout/DashboardLayout";
import HomePage from "./pages/HomePage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <HomePage />,
  },
  {
    path: "/login",
    element: <LoginPage />,
  },
  {
    path: "/register",
    element: <RegisterPage />,
  },
  {
    path: "/dashboard",
    element: <DashboardLayout />,
    children: [
      {
        path: "patients",
        element: <PatientsPage />,
      },
      {
        path: "patients/new",
        element: <PatientFormPage />,
      },
      {
        path: "patients/:id/edit",
        element: <PatientFormPage />,
      },
      {
        path: "health-programs",
        element: <HealthProgramsPage />,
      },
      {
        path: "health-programs/new",
        element: <HealthProgramFormPage />,
      },
      {
        path: "health-programs/:id/edit",
        element: <HealthProgramFormPage />,
      },
      {
        path: "severity",
        element: <SeverityPage />,
      },
      {
        path: "severity/new",
        element: <SeverityFormPage />,
      },
      {
        path: "severity/:id/edit",
        element: <SeverityFormPage />,
      },
    ],
  },
]);

export default router;
