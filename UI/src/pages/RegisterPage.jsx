import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { register } from "../features/auth/authSlice";
import { useNavigate } from "react-router-dom";

function RegisterPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { loading, error } = useSelector((state) => state.auth);
  const [formData, setFormData] = useState({
    fname: "",
    lname: "",
    email: "",
    phone: "",
    password: "",
    age: "",
    topCred: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await dispatch(register(formData));
    if (res.meta.requestStatus === "fulfilled") {
      navigate("/login"); // After registration, go to login
    }
  };

  return (
    <div className="min-h-screen flex justify-center items-center bg-base-200">
      <div className="card w-[30rem] bg-base-100 shadow-xl p-5">
        <h2 className="text-2xl font-bold text-center mb-4">Register</h2>
        {error && <div className="text-error text-center">{error.message || "Registration failed"}</div>}
        <form onSubmit={handleSubmit}>
          <div className="grid grid-cols-2 gap-4">
            <div className="form-control">
              <label className="label">
                <span className="label-text">First Name</span>
              </label>
              <input type="text" name="fname" className="input input-bordered" onChange={handleChange} required />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Last Name</span>
              </label>
              <input type="text" name="lname" className="input input-bordered" onChange={handleChange} required />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Email</span>
              </label>
              <input type="email" name="email" className="input input-bordered" onChange={handleChange} required />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Phone</span>
              </label>
              <input type="text" name="phone" className="input input-bordered" onChange={handleChange} required />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Password</span>
              </label>
              <input type="password" name="password" className="input input-bordered" onChange={handleChange} required />
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Age</span>
              </label>
              <input type="number" name="age" className="input input-bordered" onChange={handleChange} required />
            </div>
            <div className="form-control col-span-2">
              <label className="label">
                <span className="label-text">Top Credential</span>
              </label>
              <input type="text" name="topCred" className="input input-bordered" onChange={handleChange} required />
            </div>
          </div>
          <button className="btn btn-primary w-full mt-6" disabled={loading}>
            {loading ? "Registering..." : "Register"}
          </button>
        </form>
        <p className="mt-4 text-center">
          Already have an account?{" "}
          <button onClick={() => navigate("/login")} className="link link-primary">
            Login
          </button>
        </p>
      </div>
    </div>
  );
}

export default RegisterPage;
