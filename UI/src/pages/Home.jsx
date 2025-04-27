import {
  FaClinicMedical,
  FaUserMd,
  FaCalendarAlt,
  FaAmbulance,
  FaPhoneAlt,
  FaMapMarkerAlt,
} from "react-icons/fa";
import { MdHealthAndSafety } from "react-icons/md";
import { NavLink } from "react-router-dom";

const Home = () => {
  return (
    <div className="min-h-screen bg-base-100">
      {/* Hero Section */}
      <div
        className="hero min-h-screen"
        style={{
          backgroundImage:
            "url(https://images.unsplash.com/photo-1579684385127-1ef15d508118?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)",
        }}
      >
        <div className="hero-overlay bg-opacity-60"></div>
        <div className="hero-content text-center text-neutral-content">
          <div className="max-w-2xl">
            <MdHealthAndSafety className="text-6xl mx-auto mb-4 text-primary" />
            <h1 className="mb-5 text-5xl font-bold">Welcome to HealthSystem</h1>
            <p className="mb-5 text-xl">
              Comprehensive healthcare solutions for you and your family.
              Quality care from trusted professionals.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
             
              <NavLink to="/register" className="btn btn-primary">Register</NavLink>
              <NavLink to="/login" className="btn btn-outline btn-accent">Login</NavLink>
              
            </div>
          </div>
        </div>
      </div>

      {/* Services Section */}
      <div className="py-20 px-4 sm:px-6 lg:px-8 bg-base-100">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16">Our Services</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <div className="card bg-base-200 shadow-xl">
              <div className="card-body items-center text-center">
                <FaUserMd className="text-4xl text-primary mb-4" />
                <h3 className="card-title">Expert Physicians</h3>
                <p>Board-certified doctors providing personalized care</p>
                <div className="card-actions mt-4">
                  <button className="btn btn-sm btn-link">Learn more</button>
                </div>
              </div>
            </div>
            <div className="card bg-base-200 shadow-xl">
              <div className="card-body items-center text-center">
                <FaClinicMedical className="text-4xl text-primary mb-4" />
                <h3 className="card-title">Modern Facilities</h3>
                <p>State-of-the-art equipment for accurate diagnostics</p>
                <div className="card-actions mt-4">
                  <button className="btn btn-sm btn-link">Learn more</button>
                </div>
              </div>
            </div>
            <div className="card bg-base-200 shadow-xl">
              <div className="card-body items-center text-center">
                <FaCalendarAlt className="text-4xl text-primary mb-4" />
                <h3 className="card-title">Easy Scheduling</h3>
                <p>Convenient online appointment booking</p>
                <div className="card-actions mt-4">
                  <button className="btn btn-sm btn-link">Learn more</button>
                </div>
              </div>
            </div>
            <div className="card bg-base-200 shadow-xl">
              <div className="card-body items-center text-center">
                <FaAmbulance className="text-4xl text-primary mb-4" />
                <h3 className="card-title">Emergency Care</h3>
                <p>24/7 emergency services when you need them most</p>
                <div className="card-actions mt-4">
                  <button className="btn btn-sm btn-link">Learn more</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="py-20 bg-primary text-primary-content">
        <div className="max-w-4xl mx-auto text-center px-4">
          <h2 className="text-4xl font-bold mb-6">
            Ready to take control of your health?
          </h2>
          <p className="text-xl mb-8">
            Join thousands of satisfied patients who trust HealthSystem for
            their healthcare needs.
          </p>
          <button className="btn btn-accent btn-lg">Get Started Today</button>
          
        </div>
      </div>

      {/* Contact Section */}
      <div className="py-20 px-4 sm:px-6 lg:px-8 bg-base-100">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16">Contact Us</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="card bg-base-200 shadow-lg">
              <div className="card-body items-center text-center">
                <FaPhoneAlt className="text-3xl text-primary mb-4" />
                <h3 className="card-title">By Phone</h3>
                <p className="text-lg">(123) 456-7890</p>
                <p>24/7 Emergency: (123) 456-7891</p>
              </div>
            </div>
            <div className="card bg-base-200 shadow-lg">
              <div className="card-body items-center text-center">
                <FaMapMarkerAlt className="text-3xl text-primary mb-4" />
                <h3 className="card-title">Our Location</h3>
                <p className="text-lg">123 Healthcare Ave</p>
                <p>Medical City, MC 12345</p>
              </div>
            </div>
            <div className="card bg-base-200 shadow-lg">
              <div className="card-body items-center text-center">
                <FaCalendarAlt className="text-3xl text-primary mb-4" />
                <h3 className="card-title">Hours</h3>
                <p className="text-lg">Monday-Friday: 8am-8pm</p>
                <p>Saturday: 9am-5pm</p>
                <p>Sunday: Emergency only</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="footer p-10 bg-neutral text-neutral-content flex flex-col md:flex-row justify-between items-center">
        <div>
          <MdHealthAndSafety className="text-4xl" />
          <p>
            HealthSystem
            <br />
            Providing quality healthcare since 2005
          </p>
        </div>
        <div>
          <span className="footer-title">Services</span>
          <a className="link link-hover">Primary Care</a>
          <a className="link link-hover">Specialty Care</a>
          <a className="link link-hover">Emergency Services</a>
          <a className="link link-hover">Diagnostics</a>
        </div>
        <div>
          <span className="footer-title">Company</span>
          <a className="link link-hover">About us</a>
          <a className="link link-hover">Careers</a>
          <a className="link link-hover">Press kit</a>
        </div>
        <div>
          <span className="footer-title">Legal</span>
          <a className="link link-hover">Terms of use</a>
          <a className="link link-hover">Privacy policy</a>
          <a className="link link-hover">Cookie policy</a>
        </div>
      </footer>
    </div>
  );
};

export default Home;
