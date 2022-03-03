import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Sidebar from './Components/Sidebar/Sidebar';
import Home from './pages/Home';
import CommandInjection from './pages/CommandInjection';
import SqlInjection from './pages/SqlInjection';
import FileUpload from './pages/FileUpload';
import BruteForce from './pages/BruteForce';
import XSS from './pages/XSS';

function App() {
    return (
        <div className="bg-dvma4 h-screen flex flex-col items-center">
            <BrowserRouter>
                <h1 className="text-dvma2 text-5xl text-center pt-4 pb-4">
                    DVMA
                </h1>
                <div className="flex h-5/6 w-4/6 px-5">
                    <Sidebar />
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route
                            path="/command-inject"
                            element={<CommandInjection />}
                        />
                        <Route path="/sql-inject" element={<SqlInjection />} />
                        <Route path="/file-upload" element={<FileUpload />} />
                        <Route path="/brute-force" element={<BruteForce />} />
                        <Route path="/xss" element={<XSS />} />
                    </Routes>
                </div>
            </BrowserRouter>
        </div>
    );
}

export default App;
