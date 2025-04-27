import { Outlet, Link, useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { logout } from "../../features/auth/authSlice";

function DashboardLayout() {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(logout());
    navigate("/login");
  };

  return (
    <div className="min-h-screen flex flex-col">
      {/* Navbar */}
      <div className="navbar bg-primary text-primary-content">
        <div className="flex-1">
          <Link to="/dashboard/patients" className="btn btn-ghost normal-case text-xl">
            HealthSys
          </Link>
        </div>
        <div className="flex-none">
          <button onClick={handleLogout} className="btn btn-secondary">
            Logout
          </button>
        </div>
      </div>

      {/* Sidebar + Main */}
      <div className="flex flex-1">
        {/* Sidebar */}
        <div className="w-60 bg-base-200 p-4">
          <ul className="menu">
            <li><Link to="/dashboard/patients">Patients</Link></li>
            <li><Link to="/dashboard/health-programs">Health Programs</Link></li>
            <li><Link to="/dashboard/severity">Severity Levels</Link></li>
          </ul>
        </div>

        {/* Main content */}
        <div className="flex-1 p-6 overflow-auto">
          <Outlet />
        </div>
      </div>
    </div>
  );
}

export default DashboardLayout;
