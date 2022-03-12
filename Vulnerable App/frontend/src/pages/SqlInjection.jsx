import { useState } from 'react';
import axios from 'axios';

const SqlInjection = () => {
    const [user, setuser] = useState('');
    const [result, setResult] = useState([]);
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(user);
        axios
            .post('http://127.0.0.1:8082/api/sqlquery', {
                user_id: user,
            })
            .then((res) => {
                console.log(res);
                setResult(res.data.res);
            })
            .catch((err) => {
                console.log(err);
            });
        setuser('');
    };
    return (
        <div>
            <div className="justify-around m-6">
                <h1 className="text-4xl">SQL Injection</h1>
                <div className="my-3 bg-dvma5 py-2 px-4">
                    <form action="" className="my-4" onSubmit={handleSubmit}>
                        <label htmlFor="" className="mx-2">
                            User Id:
                        </label>
                        <input
                            type="text"
                            className="mx-2"
                            onChange={(e) => setuser(e.target.value)}
                        />
                        <button className="btn">Submit</button>
                    </form>
                    {result
                        ? result.map((item) => {
                              return (
                                  <div>
                                      <p>First Name: {item[0]}</p>
                                      <p>Last Name: {item[1]}</p>
                                  </div>
                              );
                          })
                        : ''}
                </div>
            </div>
        </div>
    );
};

export default SqlInjection;
