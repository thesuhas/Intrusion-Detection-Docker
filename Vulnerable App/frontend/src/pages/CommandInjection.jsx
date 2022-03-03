import { useState } from 'react';
import axios from 'axios';

const CommandInjection = () => {
    const [command, setCommand] = useState('');
    const [result, setResult] = useState('');
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(command);
        axios
            .post('http://172.22.0.1:8081/api/ping', {
                IP: command,
            })
            .then((res) => {
                console.log(res);
                setResult(res.data);
            })
            .catch((err) => {
                console.log(err);
            });
        setCommand('');
    };
    return (
        <div>
            <div className="justify-around m-6">
                <h1 className="text-4xl">Command Injection</h1>
                <div className="my-3 bg-dvma5 py-2 px-4">
                    <h3 className="text-2xl">Ping a device</h3>
                    <form action="" className="my-4" onSubmit={handleSubmit}>
                        <label htmlFor="" className="mx-2">
                            Enter a IP address:
                        </label>
                        <input
                            type="text"
                            className="mx-2"
                            onChange={(e) => setCommand(e.target.value)}
                        />
                        <button className="btn">Submit</button>
                    </form>
                    {result ? (
                        <div>
                            <h3>Command Injection Result:</h3>
                            <p>{result}</p>
                        </div>
                    ) : (
                        ''
                    )}
                </div>
            </div>
        </div>
    );
};

export default CommandInjection;
