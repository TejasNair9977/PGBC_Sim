import React, {useState} from "react"
import './index.scss'

export const Login = () => {
    const [pubKey, setPubKey] = useState('')
    const [privKey, setPrivKey] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(pubKey)
        // Api Call goes here

    }
    return (
        <div className="auth-form-container">
            <div className="auth-box">
                <form onSubmit={handleSubmit}>
                    <label htmlFor="publickey">Public Key</label>
                    <input value={pubKey} onChange={(e)=>setPubKey(e.target.value)} type="text" placeholder="Your Public Key" id='pubkey' name='pubkey' />
                    <label htmlFor="privatekey">Private Key</label>
                    <input value={privKey} onChange={(e)=>setPrivKey(e.target.value)} type="password" placeholder="Your Private Key" id='privkey' name='privkey' />
                    <button type="submit">Login</button> 
                </form>
            </div>
        </div>
    )
}