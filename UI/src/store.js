import { configureStore } from "@reduxjs/toolkit";
import authReducer from "../features/auth/authSlice";
import patientReducer from "../features/patients/patientSlice";
import healthProgramReducer from "../features/healthPrograms/healthProgramSlice";

export const store = configureStore({
  reducer: {
    auth: authReducer,
    patients: patientReducer,
    healthPrograms: healthProgramReducer,
  },
});
