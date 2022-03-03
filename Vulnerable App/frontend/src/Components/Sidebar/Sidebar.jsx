import { NavLink } from 'react-router-dom';

const Sidebar = () => {
    return (
        <div className="flex flex-col bg-dvma2 w-1/5 h-full text-dvma4 py-4">
            <NavLink to="/" className=" text-xl my-1 mx-4 active:bg-red-300 ">
                Home
            </NavLink>
            <NavLink to="/command-inject" className="text-xl my-1 mx-4">
                Command Injection
            </NavLink>
            <NavLink to="/sql-inject" className="text-xl my-1 mx-4">
                Sql Injection
            </NavLink>
            <NavLink to="/file-upload" className="text-xl my-1 mx-4">
                File Upload
            </NavLink>
            <NavLink to="/brute-force" className="text-xl my-1 mx-4">
                Brute Force
            </NavLink>
            <NavLink to="/xss" className="text-xl my-1 mx-4">
                XSS
            </NavLink>
        </div>
    );
};

export default Sidebar;
