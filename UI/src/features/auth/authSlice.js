import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import API from "../../utils/api";

// Login action
export const login = createAsyncThunk("auth/login", async (payload, { rejectWithValue }) => {
  try {
    const res = await API.post("/login", payload);
      localStorage.setItem("authToken", res.data.token);
      console.log(res.data.token);
    return res.data;
  } catch (err) {
    return rejectWithValue(err.response.data);
  }
});

// Register action 
export const register = createAsyncThunk("auth/register", async (payload, { rejectWithValue }) => {
  try {
    const res = await API.post("/register", payload);
    return res.data;
  } catch (err) {
    return rejectWithValue(err.response.data);
  }
});

const authSlice = createSlice({
  name: "auth",
  initialState: {
    user: null,
    token: localStorage.getItem("authToken") || null,
    loading: false,
    error: null,
  },
  reducers: {
    logout(state) {
      state.user = null;
      state.token = null;
      localStorage.removeItem("authToken");
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(login.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(login.fulfilled, (state, action) => {
        state.loading = false;
        state.token = action.payload.token;
      })
      .addCase(login.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(register.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(register.fulfilled, (state) => {
        state.loading = false;
      })
      .addCase(register.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const { logout } = authSlice.actions;
export default authSlice.reducer;
