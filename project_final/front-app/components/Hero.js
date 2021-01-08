import React from 'react'
import './Hero.css'

//import {motion} from 'framer-motion'

const Hero = () =>{
    return(
        <section>
            <div className='container'>
                <div className='columnLeft'>
                    <h1>this is a test</h1>
                    <p>P Tag test!</p>
                    <button>Get Started</button>
                </div>
                <div className='ColumnRight'>
                    Filter
                </div>
            </div>
        </section>
    )
}

export default Hero