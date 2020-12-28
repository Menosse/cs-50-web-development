import React from 'react';
import './App.css';
import Hero from './components/Hero'
//import logo from './logo.svg';
// Import the BrowserRouter, Route and Link components
import { BrowserRouter, Route, Link } from 'react-router-dom'; 
import Projects from './Projects.js'; 
import Articles from './Articles.js'; 
import About from './About.js'; 
import './App.css';
 
function App() {
    return <Hero /> ;

    }
export default App;



/*
function App() {
    return (
    <BrowserRouter>
      <div className="App">
  
        // Set up the Router
        <Route exact path="/" component={Projects} />
        <Route path="/articles" component={Articles} />
        <Route path="/about" component={About} />
  
        <div className="navigation">
         
          <div className="navigation-sub">
                                          
            // Set up the Links
            <Link to="/" className="item">Projects</Link>
            <Link to="/articles" className="item">Articles</Link>
            <Link to="/about" className="item">About</Link>
  
          </div>
        </div>
      </div>
    </BrowserRouter>

  );
}
 
export default App;
*/
